import argparse
from pathlib import Path

from esdl_parser import parser


arg_parser = argparse.ArgumentParser(
    prog='esdl',
    description='ESDL Data Definition Language Compiler',
    epilog='File issues or star and thank author at https://github.com/chuigda/esdl'
)
arg_parser.add_argument('-i', dest='input', help='input file', required=True, type=Path)
arg_parser.add_argument('-g', dest='generator', help='select code generator', choices=[
    'rs',
    'js',
    'py',
    'cxx'
], default='rs')


if __name__ == '__main__':
    args = arg_parser.parse_args()
    with open(args.input, 'r') as input_file:
        parsed_tree = parser.parse(input_file.read())
        print(parsed_tree)
