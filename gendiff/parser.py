import json
import os
import yaml


def get_file_data(path):
    with open(path) as file_data:
        return convert_data(path, file_data)


def convert_data(path, file_data):
    _, extension = os.path.splitext(path)
    if extension == '.json':
        return json.load(file_data)
    if extension == '.yaml' or extension == '.yml':
        return yaml.safe_load(file_data)
