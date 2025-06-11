# Use the official Python base image
FROM python:3.11

# Set work directory
WORKDIR /app

# Copy all code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command (run the pipeline)
CMD ["python", "src/pipeline.py"]
