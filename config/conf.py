import logging
import os
from typing import Optional, Union

from pydantic import BaseSettings

IS_LOCAL_ENV = 0


class ProjectConfig(BaseSettings):
    # ########## Global logger settings ########## #
    LOG_TO: int = 0
    LOGGER_LEVEL: Union[int, str] = logging.DEBUG

    # ########## Global logger settings ########## #
    MAIL_PORT: Union[int, str] = '587'
    MAIL_SERVER: str = 'smtp.gmail.com'
    MAIL_USER: str = '@gmail.com'
    MAIL_PASSWORD: str = ''


PROJECT_CONF = ProjectConfig()


class AzureConfig(BaseSettings):
    # ########## Azure Storage settings ########## #
    STORAGE_ACCOUNT_NAME: str = 'mlnwazurestorage'
    STORAGE_CONNECTION_STRING: str = 'DefaultEndpointsProtocol=https;AccountName=mlnwazurestorage;AccountKey=DBq05xUIg2lK9ANXGTB+2GKysD0UJmg9gq0kuYAsGAbK72lA+JR3LJ+rijft5Z9yueJpMBGtnRhd+ASt6uUAwQ==;EndpointSuffix=core.windows.net'
    STORAGE_KEY: str = 'DBq05xUIg2lK9ANXGTB+2GKysD0UJmg9gq0kuYAsGAbK72lA+JR3LJ+rijft5Z9yueJpMBGtnRhd+ASt6uUAwQ=='
    BLOB_CONTAINER_NAME: str = 'bot'
    BLOB_CONTAINER_NAME_MEDIA: str = 'media'

    # ########## Azure Bot settings ########## #
    BOTAPPID: str = '165a647d-c616-4eb5-8ede-81ad309c1743'
    BOTAPPPASSWORD: str = '7kA8Q~ADSDlUHA6e81S~knL2tKfjLZpDtlvxYbG.'
    PORT: int = 3978
    MAINTENANCE: int = 0

    # ########## Azure App Insights settings ########## #
    APP_INSIGHTS_INSTRUMENTATION_KEY: str = ''


AZURE_CONF = AzureConfig()


class FastApiConfig(BaseSettings):
    # ########## FastApi settings ########## #
    # HOST: str = 'localhost'
    HOST: str = '0.0.0.0'
    # PORT: int = 3978
    PORT: int = 8000

    DB_URL: str = "sqlite:///sqlite.db"

    JWT_SECRET: str = os.environ.get('JWT_SECRET', '')
    JWT_ALGO: str = 'HS256'
    JWT_EXPIRES_S: int = 3600


FAST_API_CONF = FastApiConfig()

TAGS_META = [
    {
        'name': 'Bot messages exchange',
        'description': 'Bot messages exchange',
    },
    {
        'name': 'Bot notification exchange',
        'description': 'Bot notification exchange',
    },
]
