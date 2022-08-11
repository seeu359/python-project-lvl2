#!/usr/bin/env python
from gendiff.trying.gen_diff import generate_diff
from gendiff.trying.parser import parsers_data


def main():
    args = parsers_data()
    if args.format == 'json':
        print(generate_diff(args.first_file, args.second_file,
                            'json'))
    elif args.format == 'plain':
        print(generate_diff(args.first_file, args.second_file,
                            'plain'))
    elif args.format == 'stylish':
        print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
