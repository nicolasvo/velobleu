import os
import re
import json
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
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'stations': get_stations()
        }),
        'isBase64Encoded': False
    }
