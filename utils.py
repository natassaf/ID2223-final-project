import os
import datetime
import time
import requests
import pandas as pd
import json
#from geopy.geocoders import Nominatim
#import matplotlib.pyplot as plt
#from matplotlib.patches import Patch
#from matplotlib.ticker import MultipleLocator
#import openmeteo_requests
#import requests_cache
#from retry_requests import retry
import hopsworks
import hsfs
from pathlib import Path


fng_labels_to_numbers_map={"Extreme Fear":0, "Fear":1, "Neutral":2, "Greed":3, "Extreme Greed":4} 
fng_numbers_to_labels_map={0:"Extreme Fear", 1:"Fear", 2:"Neutral", 3:"Greed", 4:"Extreme Greed"} 

def trigger_request(url:str, params:dict):
    response = requests.get(url, params)
    if response.status_code == 200:
        # Extract the JSON content from the response
        data = response.json()
    else:
        print("Failed to retrieve data. Status Code:", response.status_code)
        raise requests.exceptions.RequestException(response.status_code)

    return data


def secrets_api(proj):
    host = "c.app.hopsworks.ai"
    api_key = os.environ.get('HOPSWORKS_API_KEY')
    #print(f"api_key {api_key}")
    conn = hopsworks.connection(host=host, project=proj, api_key_value=api_key)
    return conn.get_secrets_api()
