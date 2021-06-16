#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# https://developer.51cto.com/art/202008/624601.htm

import sqlite3

from config import *
from utils import *


def create_db(db_file_name, path=None):
    if not db_file_name: raise
    if not path: path = default_db_files_path
    make_folder(path)
    conn = sqlite3.connect(f"{path}/{db_file_name}")
    return conn


def create_key_info_table(cursor):
    if not cursor: raise
    cursor.execute(
        f'''
        CREATE TABLE {key_info_table} 
        (
        name TEXT,
        url TEXT,
        path TEXT,
        iv TEXT,
        owner TEXT
        );
        '''
    )


def insert_key(cursor, name, path, iv, owner, url=None):
    if not name: raise
    if not path: raise
    if not iv: raise
    if not owner: raise
    if not url:
        url = f'{default_key_path}{name}'
    if not cursor: raise
    if not check_table_exist(cursor, key_info_table):
        create_key_info_table(cursor)
    data = (name, url, path, iv, owner)
    cursor.execute(
        f'''INSERT INTO {key_info_table} VALUES (?,?,?,?,?);''',
        data
    )


def select_keys(cursor, owner):
    if not cursor: raise
    if not owner: raise
    if not check_table_exist(cursor, key_info_table):
        create_key_info_table(cursor)
    cursor.execute(f'''SELECT name FROM {key_info_table} WHERE owner={owner}''')
    return cursor.fetchall()


def create_file_info_table(cursor):
    if not cursor: raise
    cursor.execute(
        f'''
        CREATE TABLE {file_info_table} 
        (
        name TEXT,
        alias TEXT,
        key_info_id INT,
        filter_info TEXT,
        owner TEXT
        );
        '''
    )


def insert_file_info(cursor, name, alias, key_info_id, filter_info, owner):
    if not name: raise
    if not alias: raise
    if not key_info_id: raise
    if not filter_info: filter_info = ''
    if not owner: raise
    if not cursor: raise
    if not check_table_exist(cursor, key_info_table):
        create_key_info_table(cursor)
    data = (name, alias, key_info_id, filter_info, owner)
    cursor.execute(
        f'''INSERT INTO {file_info_table} VALUES (?,?,?,?,?);''',
        data
    )


def check_table_exist(cursor, table_name):
    if not cursor: raise
    if not table_name: raise
    cursor.execute(
        f'''
        SELECT count(name) 
        FROM sqlite_master 
        WHERE type='table' AND name={table_name}
        '''
    )
    return cursor.fetchone()[0] == 1
