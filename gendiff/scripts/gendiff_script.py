#!/usr/bin/env python
from gendiff.generate_diff import generate_diff
from gendiff.parser import parsers_data
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json


def main():
    args = parsers_data()
    if args.format == 'json':
        return generate_diff(args.first_file, args.second_file, json)
    if args.format == 'plain':
        return generate_diff(args.first_file, args.second_file, plain)
    else:
        return generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
