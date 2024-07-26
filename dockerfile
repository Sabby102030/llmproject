# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Hugging Face Transformers and other dependencies
RUN pip install transformers torch safetensors huggingface_hub

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME SmolLM-360M

# Run app.py when the container launches
CMD ["python", "app.py"]
