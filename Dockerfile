# Use an official Python image as the base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port your server will run on
EXPOSE 8080

# Define the command to run the server
CMD ["python", "server/main.py"]
