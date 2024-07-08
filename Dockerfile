# Use an official Python 3.9 base image with a slim (minimal) version
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies listed in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire content of the current directory to the working directory in the container
COPY . .

# Expose port 8000 to allow access to the application
EXPOSE 8000

# Set the default command to run the application using uvicorn
CMD ["uvicorn", "services.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
