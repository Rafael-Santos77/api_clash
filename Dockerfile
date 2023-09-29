# Use the official Python image as the base image
FROM python:3

# Set the working directory in the container
WORKDIR C:\std\api_c

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# Copy the application files into the working directory
COPY . . 

# Define the entry point for the container
CMD ["python", "manage.py", "runserver"]
