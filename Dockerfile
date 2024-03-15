# Use an official Python runtime as a parent image
FROM python:3.11.6

ENV PYTHONUNBUFFERED 1

# Create a new directory in container - django-project
RUN mkdir /django_register

# Set the working directory in the container
WORKDIR /django_register

# add in this directory files
ADD . /django_register/

# Install any needed dependencies specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install mysqlclient
RUN pip install psycopg2-binary

# Copy the current directory contents into the container at /app
COPY . /django_register/

# Copy .env file from directory to the inside our container
COPY .env /django_register/.env