#!/usr/bin/env python3
import requests
import csv
import os
from datetime import datetime, timezone, timedelta

API_URL = "https://dogapi.dog/api/v2/breeds?page[number]=1&page[size]=10"
SAVE_DIR = "/home/cron"
WIB = timezone(timedelta(hours=7))  # UTC+7 timezone

def fetch_data():
    headers = {"Accept": "application/json"}
    response = requests.get(API_URL, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    
    data = response.json().get("data", [])
    breeds = []

    for breed in data:
        attributes = breed.get("attributes", {})
        breeds.append({
            "id": breed.get("id"),
            "name": attributes.get("name"),
            "description": attributes.get("description"),
            "life_max": attributes.get("life", {}).get("max"),
            "male_weight_max": attributes.get("male_weight", {}).get("max"),
            "female_weight_max": attributes.get("female_weight", {}).get("max"),
            "hypoallergenic": attributes.get("hypoallergenic"),
            "breed_group": attributes.get("breed_group"),
            "created_at": attributes.get("created_at"),
            "updated_at": attributes.get("updated_at")
        })

    print(f"Collected {len(breeds)} records")
    return breeds


def save_to_csv(breeds):
    os.makedirs(SAVE_DIR, exist_ok=True)
    now = datetime.now(WIB)
    date_str = now.strftime("%m%d%Y")
    hour_str = now.strftime("%H")
    minute_str = now.strftime("%M")
    filename = f"cron_{date_str}_{hour_str}.{minute_str}.csv"
    filepath = os.path.join(SAVE_DIR, filename)

    fieldnames = [
        "id", "name", "description", "life_max",
        "male_weight_max", "female_weight_max",
        "hypoallergenic", "breed_group",
        "created_at", "updated_at"
    ]

    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(breeds)

    print(f"Data saved to {filepath}")


def main():
    try:
        breeds = fetch_data()
        save_to_csv(breeds)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
