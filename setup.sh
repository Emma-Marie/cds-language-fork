#!/usr/bin/env bash

<<<<<<< HEAD
#create virtual environment
python3 -, venv spacy_env

# activate virtual environment
source ./spacy_env/bin/activate

#then install requirements
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m spacy download en_core_web_md

#run the code
python3 src/script.py

#close the virtual environment
deactivate
=======
# install hdbscan for BERTopic
sudo apt-get update
sudo apt-get install python3-dev

# requirements
pip install --upgrade pip
pip install --upgrade nbformat
python3 -m pip install -r requirements.txt
>>>>>>> 52da4eb463d16bfca02f995c5dad9056e2bfb02c
