#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import argparse

parser = argparse.ArgumentParser(description='Test for argparse')
parser.add_argument('-s', '-source', help='source video file 属性，必要参数', required=True)
args = parser.parse_args()

if __name__ == '__main__':
    source_file = args.s

    # get the file ready to be sliced.
    print(f"""
    source video file: {source_file}
    """)

    # Create key file and information

    # Slice the file

    # Save the file information and relevant key information

    # Upload sliced files


