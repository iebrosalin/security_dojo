#!/usr.bin/env python

import requests

class DNSbroot:
    target_url = "source_url"
    def request(url):
        try:
            return requests.get("https://" + url)
        except requests.exception.ConnectionError:
            pass
    

    def urls():
        with open("word_list_path", "r") as word_list_file:
            for line in wordlist_file:
                word = line.strip()
                test_url = target_url + "/" + word
                response = request = request(test_url)
                if response:
                    print("[+] Discovering URL --> " + test_url)


