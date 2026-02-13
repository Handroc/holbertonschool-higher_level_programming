#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Returns the XML string representation of an object."""
    data = ET.Element("root")
    for key, value in dictionary.items():
        child = ET.SubElement(data, key)
        child.text = str(value)
    tree = ET.ElementTree(data)
    tree.write(filename)

def deserialize_from_xml(filename):
    """Returns the Python object represented by an XML string."""
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
