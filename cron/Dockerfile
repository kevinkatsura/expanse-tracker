FROM python:3.10-slim

# Install cron
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy project files
COPY collect_dog.py /app/collect_dog.py
COPY crontab.txt /etc/cron.d/dog-cron
COPY requirements.txt /app/requirements.txt

# Give execution permissions
RUN chmod 0644 /etc/cron.d/dog-cron && \
    chmod +x /app/collect_dog.py && \
    chmod +x /app/requirements.txt
# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Apply cron job
RUN crontab /etc/cron.d/dog-cron

# Create output folder
RUN mkdir -p /home/cron

# Run cron in the foreground
CMD ["cron", "-f"]
