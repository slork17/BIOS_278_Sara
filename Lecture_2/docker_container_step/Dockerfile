# Start from official Python image
FROM python:3.10-slim

# Set metadata labels
LABEL maintainer="your.email@university.edu" \
      version="1.0.0" \
      description="Brain imaging visualization container"

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/

# Create directories for data and results
RUN mkdir -p /data /results

# Set working directory to /data
WORKDIR /data

# Add script to PATH
ENV PATH="/app/src:${PATH}"

# Make scripts executable
RUN chmod +x /app/src/*.py

# Default command - show help
CMD ["python", "/app/src/plot_brain_image.py", "--help"]