

# Official Python runtime
FROM python:3.9-slim

# Project work directorty
WORKDIR /usr/src/app

# Copy the local project directory to the container
COPY . .

# Install module dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make migrations, as described in the install tutorial from the original repository
RUN python manage.py makemigrations && python manage.py migrate

# Expose the port for public access
ENV DJANGO_DEV_SERVER_PORT 8000
EXPOSE $DJANGO_DEV_SERVER_PORT

# Set the default command to run the Django dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

