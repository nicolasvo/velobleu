import os
import re
import json5
import requests

def get_stations():
    r = requests.get('https://www.velobleu.org/en/nos-stations/')
    site = r.text.replace('\n', '')
    find = re.compile(r"var stations([^;]+)")
    r = re.search(find, site)
    string = r.group().replace('var stations = ', '')
    stations = json5.loads(string)
    return stations

def handler(event, context):
    return { 
        'stations' : get_stations()
    }
