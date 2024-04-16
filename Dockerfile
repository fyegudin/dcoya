# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire test directory into the container at /usr/src/app
COPY tests/coffe_soft/ ./tests/coffe_soft/

# Set environment variables
ENV PYTHONPATH=/usr/src/app

# Define the command to run your tests
CMD ["pytest", "tests"]

# Use follow commands:
# Bild docker:
# docker build -t my-python-tests .
# docker run my-python-tests


