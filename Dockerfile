# Use the official Python image as a base image
FROM python:latest

RUN apt-get update && apt-get install -y python3 python3-pip

# Copy your Chalice app files into the container
COPY . /app

WORKDIR /app
# Install your Chalice app's requirements
RUN pip install -r requirements.txt

RUN ls


# Expose the port that Chalice's local server runs on (usually 8000)
EXPOSE 8000

# Set an environment variable to run Chalice in local mode
ENV CHALICE_STAGE=local

# Define the command to start the Chalice local server
CMD ["chalice", "local"]