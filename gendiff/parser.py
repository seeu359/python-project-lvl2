import json
import os
import yaml


def get_file_data(path):
    with open(path) as file:
        file_data = file.read()
    return file_data


def convert_data(file_data, path):
    _, extension = os.path.splitext(path)
    if extension == '.json':
        return json.loads(file_data)
    if extension in ('.yaml', '.yml'):
        return yaml.safe_load(file_data)
