# Use an existing base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the code to the working directory
COPY . /app

# Install required packages
RUN pip install -r requirements.txt

# Set the environment variable
ENV FLASK_APP=app.py

# Expose the port for the Flask app
EXPOSE 8080

# Start the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
