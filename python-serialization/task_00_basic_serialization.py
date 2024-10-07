#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file into a Python dictionary."""
    with open(filename, 'r') as file:
        return json.load(file)
