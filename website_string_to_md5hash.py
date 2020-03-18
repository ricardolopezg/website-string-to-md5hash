#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup
import hashlib

def main():
    # url to parse
    url = sys.argv[1]

    # create session to retrieve content
    sesh = requests.Session()
    url_content = sesh.get(url)

    # parse through content for string
    soup = BeautifulSoup(url_content.text, 'html.parser')
    string = soup.h3.get_text()

    # convert string to md5 hash
    hash_calc = hashlib.md5(string.encode('utf-8')).hexdigest()

    # send POST request with hashed parameter
    params={'hash' : hash_calc}
    post_hash = sesh.post(f'{url}', params)

    # parse html after POST request and print flag
    result = BeautifulSoup(post_hash.text, 'html.parser')
    result_flag = result.p.get_text()
    print(result_flag)

if __name__ == '__main__':
    main()