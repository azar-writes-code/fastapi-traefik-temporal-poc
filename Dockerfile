# Use an official Python runtime as a parent image
FROM python:3.11-slim as base

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
    
# Multi-stage build to separate FastAPI and Temporal worker
# FastAPI stage
FROM base as fastapi

# Expose the port that the FastAPI app runs on
EXPOSE 8000

# Command to run FastAPI application
CMD ["python", "main.py"]

# Temporal worker stage
FROM base as worker

# Command to run the Temporal worker
CMD ["python", "internal/worker/run.py"]
