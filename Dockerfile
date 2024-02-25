FROM ubuntu
FROM python:3.8-slim-buster

# set the working directory in the container
WORKDIR /code

# copy the content of the local src directory to the working directory
COPY src/ .

# install dependencies
RUN pip3 install -r requirements.txt

# command to run on container start
CMD [ "python3", "app.py" ]