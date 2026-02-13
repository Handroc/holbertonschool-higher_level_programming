#!/usr/bin/python3
"""Script that adds command line arguments to a JSON list file."""
import sys
savejson = __import__('5-save_to_json_file').save_to_json_file
loadjson = __import__('6-load_from_json_file').load_from_json_file


my_list = []
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
fname = "add_item.json"
try:
    my_list2 = loadjson(fname)
except Exception:
    my_list2 = []
my_list2.extend(my_list)
savejson(my_list2, fname)
