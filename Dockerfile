FROM ubuntu
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY setup/packagerequirement.txt .

# install pyaudio

RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
RUN pip3 install pyaudio

# install dependencies
RUN pip3 install -r packagerequirement.txt

# copy the content of the local src directory to the working directory

COPY / .
COPY LibrosaAudioCompare.py .
COPY config.py .
COPY setup/ .

# command to run on container start
CMD [ "python3", "app/api.py" ]