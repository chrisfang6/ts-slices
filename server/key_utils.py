#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import datetime
import os
import subprocess

from config import *
from utils import *


def create_key(path=None, key_file_name=None):
    if not path: path = default_key_files_path
    if not key_file_name: key_file_name = datetime.datetime.now().strftime(f'{default_key_file_name}')
    make_folder(path)
    print(f"key file will be {path}/{key_file_name}")
    status = os.system('openssl rand 16 > {}'.format(f"{path}/{key_file_name}"))
    if status == 1: raise KeyError


def create_iv():
    out_bytes = subprocess.check_output(['openssl', 'rand', '-hex', '16'])
    vi = out_bytes.decode('utf-8')
    return vi

# def save_key_info(key_url, key_path, key_iv, path=None, key_info_file=None):
#     if not key_url: raise ValueError
#     if not key_path: raise ValueError
#     if not key_iv: raise ValueError
#     if not path: path = default_key_files_path
#     if not key_info_file: key_info_file = datetime.datetime.now().strftime(f'%Y%m%d%H%M%S.key.info')
#     make_folder(path)
#     print(f"key information file will be {path}/{key_info_file}")
#     with open(f"{path}/{key_info_file}", 'w') as file:
#         file.write(f"{key_url}\n")
#         file.write(f"{key_path}\n")
#         file.write(f"{key_iv}\n")
#     file.close()
