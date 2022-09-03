import argparse


def get_parser_args():
    parser = argparse.ArgumentParser(description='Compares two configuration'
                                                 ' files and shows '
                                                 'a difference. ')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output. Available output formats:'
                             '1. stylish (default formatter); '
                             '2. plain (-f plain); '
                             '3. json (-f json)',
                        default='stylish', choices=['stylish', 'plain', 'json'])
    return parser.parse_args()
