#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/user/<username>")
def hello_user(username):
    return f"<p>Hello, World!{username}</p>"
