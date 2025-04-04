# Dockerfile.rl
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables (optional)
ENV TRANSFORMERS_CACHE=/app/cache

# Launch the RLHF training script
CMD ["python", "qstar/reinforcement/train_rlhf.py"]
