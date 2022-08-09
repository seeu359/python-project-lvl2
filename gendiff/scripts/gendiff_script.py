#!/usr/bin/env python
from gendiff import generate_diff
from gendiff.parser import parsers_data
from gendiff.generate_diff import formatter_selection


def main():
    args = parsers_data()
    if args.format == 'json':
        return generate_diff(args.first_file, args.second_file,
                             formatter_selection['json'])
    if args.format == 'plain':
        return generate_diff(args.first_file, args.second_file,
                             formatter_selection['plain'])
    else:
        return generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
