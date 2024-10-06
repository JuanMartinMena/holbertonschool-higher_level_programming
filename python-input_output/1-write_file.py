#!/usr/bin/python3

def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
