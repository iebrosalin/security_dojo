#!/usr/bin/env python

import socket

connection = socket,socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("server ip", 4444))