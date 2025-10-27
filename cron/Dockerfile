FROM python:3.10-slim

# Install cron
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy project files
COPY --exclude=src/crontab.txt src/ ./
COPY src/crontab.txt /etc/cron.d/dog-cron

# Give execution permissions
RUN chmod 0644 /etc/cron.d/dog-cron && \
    chmod +x /app/collect_dog.py && \
    chmod +x /app/requirements.txt && \
    chmod +x /app/cleanup_old.sh

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Apply cron job
RUN crontab /etc/cron.d/dog-cron

# Create output folder
RUN mkdir -p /home/cron

# Run cron in the foreground
CMD ["cron", "-f"]
