#!/usr/bin/env python
from gendiff import generate_diff
from gendiff.parser import parsers_data


def main():
    args = parsers_data()
    if args.format == 'json':
        return generate_diff(args.first_file, args.second_file,
                             'json')
    if args.format == 'plain':
        return generate_diff(args.first_file, args.second_file,
                             'plain')
    else:
        return generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
