# To Start installing required packages
Run setup.sh

# For analysis for sample files
update value of testfilelocation in the config.py found under Config folder

# Librosa analysis
run librosaTest.py file

# pydub analysis
run pydubTest.py file

# use api to get librosa analysis
execute following in terminal
cd app
python3 api.py
send request to http://127.0.0.1:105/api/audio

# example of how to send file via api

see sendFileViaApi.py in the test folder

