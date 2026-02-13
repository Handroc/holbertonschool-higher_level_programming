#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(csv_file):
    """Converts a CSV file to a JSON file."""
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open("data.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (FileNotFoundError, IOError, csv.Error, json.JSONDecodeError) as e:
        # In a real app, you might log the error: print(f"Error: {e}")
        return False
