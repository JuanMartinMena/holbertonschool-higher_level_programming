#!/usr/bin/python3
"""
5-text_indentation.py

Contains the `text_indentation` function that processes and prints a text with 
two new lines after each '.', '?', and ':'.
"""

def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'.
    
    Args:
        text (str): The text to process.
        
    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    length = len(text)
    i = 0

    while i < length:
        print(text[i], end="")
        if text[i] in {'.', '?', ':'}:
            print("\n")
            while i + 1 < length and text[i + 1] == ' ':
                i += 1
                if i + 1 < length and text[i + 1] not in {'.', '?', ':'}:
                    print("\n", end="")
        i += 1
