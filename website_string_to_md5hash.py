#!/usr/bin/env python3

import sys
import requests as r
from bs4 import BeautifulSoup
import hashlib as h

def submit_hash_to_form(hash):
    print("submit")

def md5_calc(string_content):
    hash_calc = h.md5(string_content.encode('utf-8')).hexdigest()
    return hash_calc

def parse_for_string(url_content):
    soup = BeautifulSoup(url_content, 'html.parser')
    # print(soup.prettify())
    string = soup.h3.get_text()
    return string

def get_url_content(main_url):
    # sesh = r.Session()
    # url_content = sesh.get(main_url).text
    url_content = r.get(main_url).text
    return url_content

def main():
    url = sys.argv[1]
    content = get_url_content(url)
    # print(content)

    string_to_hash = parse_for_string(content)
    print("String to hash: " + str(string_to_hash))

    md5_hash = md5_calc(string_to_hash)
    print("MD5 hash: " + str(md5_hash))

    submit_hash = submit_hash_to_form(md5_hash)

if __name__ == '__main__':
    main()
