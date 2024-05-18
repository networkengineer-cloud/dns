# Create a Dockerfile to run the dns.py script

# Use the official Python image

FROM python:3.11

# Set the working directory in the container

WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app

COPY . /usr/src/app

# Install any needed packages specified in requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Run dns.py when the container launches

CMD ["python", "./dns.py"]

