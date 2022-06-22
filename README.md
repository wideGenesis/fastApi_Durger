sudo docker build --no-cache -t mycintainerregistry.azurecr.io/hr_bot_server:latest .

sudo docker run -d --name hr_bot -p 50500:8000 \
        rndnlpregistry.azurecr.io/hr_bot_server:latest

sudo docker run -it --name hr_bot -p 50500:8000 \
        rndnlpregistry.azurecr.io/hr_bot_server:latest /bin/bash

sudo docker run -it --name bot_hr_server -p 80:80 \
        mycintainerregistry.azurecr.io/bot_hr_server:latest /bin/bash


sudo docker exec -it hr_bot bash

When running in Azure Web App consider increasing WEBSITES_CONTAINER_START_TIME_LIMIT up to 600-1200.
Also only 1 worker must be running in container in Azure.

For adding new model to interface: 
1. add option to select in template
2. add LABELS_CLASSES_MAP, CLASSES_LABELS_MAP dicts
3. add new model and tokenizer loading
4. add if statement for new option with new models and maps in core.classify_text.