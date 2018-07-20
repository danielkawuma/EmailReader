#! /usr/bin/env python
import requests, os

from datetime import date

retrieved_file_dir = '~/TextFiles'
file_name = "renu_" + str(date.today().strftime('%Y%m%d')) + ".txt"
# file_name = 'renu_20180505.txt'

site_url = 'https://renu:b2ef86e451d61912@www.cymru.com/renu/renu_20180505.txt'
file_url = 'https://renu:b2ef86e451d61912@www.cymru.com/renu/'+file_name+''

response = requests.get(file_url)
# print(file_name)
retrieved_file = response.content
# print(retrieved_file)

if bool(retrieved_file):
    filePath = os.path.join(retrieved_file_dir, retrieved_file)
    # open(filePath, 'w')
    print(filePath)
# print(response.headers.get('content-type'))


