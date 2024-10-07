#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # Read CSV data
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        # Serialize data to JSON and write to data.json
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
