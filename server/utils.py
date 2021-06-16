#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os


def make_folder(path):
    if not path: raise
    if not os.path.isdir(path):
        os.mkdir(path)
