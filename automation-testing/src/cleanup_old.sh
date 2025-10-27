#!/bin/bash
# File: /usr/local/bin/cleanup_cron_csv.sh
# Deletes CSV files in /home/cron older than 30 days (based on filename timestamp)

CRON_DIR="/home/cron"
TZ='Asia/Jakarta'
NOW=$(date +%s)
THRESHOLD_MINUTES=43200 # 43200 is equal to 30 days

shopt -s nullglob
for file in "$CRON_DIR"/cron_*.csv; do
    # Extract timestamp from filename, e.g. 10272025_15.00 → 10 27 2025 15 00
    filename=$(basename "$file")
    if [[ $filename =~ cron_([0-9]{2})([0-9]{2})([0-9]{4})_([0-9]{2})\.([0-9]{2})\.csv ]]; then
        month="${BASH_REMATCH[1]}"
        day="${BASH_REMATCH[2]}"
        year="${BASH_REMATCH[3]}"
        hour="${BASH_REMATCH[4]}"
        minute="${BASH_REMATCH[5]}"
        
        # Parse using same timezone (UTC+7)
        file_time=$(TZ='Asia/Jakarta' date -d "$year-$month-$day $hour:$minute:00" +%s 2>/dev/null)
        
        # Compute age of the file in minutes
        age_minutes=$(( (NOW - file_time) / 60 ))
        
        # Delete the data if older than threshold
        if (( age_minutes > THRESHOLD_MINUTES )); then
            days=$((age_minutes / 1440))
            echo "Deleting $file (age: ${age_minutes} minutes, ${days} days)."
            rm -f "$file"
        fi
    else
        echo "Skipping file $file (unrecognized format)"
    fi
done
