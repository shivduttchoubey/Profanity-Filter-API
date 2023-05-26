#Deriving the latest base image
FROM python:latest


#Labels as key value pair
LABEL Maintainer="profanity filter"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /home/ubuntu/profapi

#to COPY the remote file at working directory in container
COPY prof_filter.py ./
COPY requirements.txt ./
# Now the structure looks like this '/usr/app/src/test.py'

EXPOSE 80

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.
RUN pip install -r requirements.txt
CMD [ "python", "./prof_filter.py"]
