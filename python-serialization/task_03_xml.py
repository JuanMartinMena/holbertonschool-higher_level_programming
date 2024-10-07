#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    # Create the root element
    root = ET.Element("data")

    # Iterate through the dictionary and create child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Ensure the value is a string

    # Write the XML tree to the specified file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary from the XML elements
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text

        return deserialized_dict
    except (ET.ParseError, FileNotFoundError):
        return None  # Return None if the file is not found or malformed
