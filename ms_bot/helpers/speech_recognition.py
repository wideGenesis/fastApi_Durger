import os
import azure.cognitiveservices.speech as speech_sdk
from pydub import AudioSegment


async def convert_to_wav(member_id: int):
    sound = AudioSegment.from_ogg(f'media/{member_id}_audio.ogg')
    sound.export(f'media/{member_id}_audio.wav', format="wav")

    if os.path.exists(f'media/{member_id}_audio.ogg'):
        os.remove(f'media/{member_id}_audio.ogg')
    else:
        print("The file does not exist")
    return


async def recognize_from_filename(member_id: int):
    speech_key = 'd0fef56cd8044c7f82322c509e208272'
    service_region = 'eastus'
    await convert_to_wav(member_id)

    audio_file_path = f'media/{member_id}_audio.wav'

    speech_config = speech_sdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_recognition_language = "ru-RU"

    audio_input = speech_sdk.AudioConfig(filename=str(audio_file_path))
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    print('Recognizing first result...')

    result = speech_recognizer.recognize_once_async().get()
    if result.reason == speech_sdk.ResultReason.RecognizedSpeech:
        return result.text
        # print('Recognized: {}'.format(result.text))
        # print("Offset in Ticks: {}".format(result.offset))
        # print("Duration in Ticks: {}".format(result.duration))

    elif result.reason == speech_sdk.ResultReason.NoMatch:
        print('No speech could be recognized: {}'.format(result.no_match_details))

    elif result.reason == speech_sdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print('Speech Recognition canceled: {}'.format(cancellation_details.reason))
        if cancellation_details.reason == speech_sdk.CancellationReason.Error:
            print('Error details: {}'.format(cancellation_details.error_details))
    return
