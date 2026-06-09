# Base image — official Python 3.13 slim (minimal size)
FROM python:3.13-slim

# Who maintains this image
LABEL maintainer="digensclub@gmail.com"
LABEL description="DevOps Lab Webapp — Learning container"

# Set working directory inside container
WORKDIR /app

# Copy requirements.txt into container
COPY requirements.txt .

# Installing required packages
RUN pip install --no-cache-dir --requirement requirements.txt

# Copy app code into container
COPY app.py .

# Expose port 8000 to outside world
EXPOSE 8000

# Command to run when container starts
CMD ["python", "app.py"]