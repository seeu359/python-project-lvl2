import json
import yaml


def convert_data(path):
    file_data, extension = get_file_data(path)
    if extension == 'JSON':
        return json.load(file_data)
    if extension == 'YAML':
        return yaml.safe_load(file_data)


def get_file_data(path):
    file = open(path)
    file_extension = path.split('.')[-1]
    if file_extension == 'json':
        return file, 'JSON'
    if file_extension == 'yaml' or file_extension == 'yml':
        return file, 'YAML'
    file.close()
