#!/usr/bin/env python
from gendiff.generate_diff import generate_diff
from gendiff.parser import parsers_data
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def main():
    args = parsers_data()
    if args.format == 'stylish':
        return generate_diff(args.first_file, args.second_file, stylish)
    if args.format == 'plain':
        return generate_diff(args.first_file, args.second_file, plain)


if __name__ == '__main__':
    main()
