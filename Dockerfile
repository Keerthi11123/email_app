# Use official Python base image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask default port (change if using FastAPI)
EXPOSE 5000

# Default command (can be overridden by docker-compose)
CMD ["python", "app.py"]
