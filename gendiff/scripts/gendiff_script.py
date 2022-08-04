#!/usr/bin/env python
from gendiff.formatter import stylish
from gendiff.generate_diff import generate_diff
from gendiff.parser import parsers_data


def main():
    args = parsers_data()
    diff = generate_diff(args.first_file, args.second_file)
    if args.format == 'stylish':
        return stylish(diff)


if __name__ == '__main__':
    main()
