# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 12:56:10 2023

@author: einck
"""

# Requires "requests" to be installed (see python-requests.org)
import requests
import os
import re
path = os.getcwd()
doc_list1 = os.listdir(path)
pattern_image = '.*\.(png|jpg|jpgs)'
pattern_image = re.compile(pattern_image)
key = input("Please input key:")
for item in doc_list1:
    image_name = re.search(pattern_image, item)
    if not image_name:
        continue
    path_temp = path+'\\'
    path_temp+=image_name.group()
    Nobg_name = 'NoBG'+image_name.group()
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(path_temp, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': key},
        )
    if response.status_code == requests.codes.ok:
        with open(Nobg_name, 'wb') as out:
           out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)
print("Complete!!!")