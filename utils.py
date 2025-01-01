import os
import datetime
import time
import requests
import pandas as pd
import json
import numpy as np
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




def create_sequences(data, time_steps, num_predictions):
    X, y = [], []
    for i in range(len(data) - (time_steps+num_predictions)):
        first_label_row_index = i+time_steps
        row = data[i:first_label_row_index, :-1]
        
        X.append(row) 
        labels = data[first_label_row_index:first_label_row_index+num_predictions, -1]
        labels = [round(l,2) for l in labels]
        y.append(labels)
    return np.array(X), np.array(y)

def train_val_test_split(X, labels, val_size=0.3, test_size=0.2):

    # Calculate split indices
    n_samples = X.shape[0]
    test_split_idx = int(n_samples * (1 - test_size))  
    val_split_idx = int(test_split_idx * (1 - val_size))  

    # Split X
    X_train = X[:val_split_idx] 
    X_val = X[val_split_idx:test_split_idx]  
    X_test = X[test_split_idx:]  #

    # labels
    labels_train = labels[:val_split_idx]
    labels_val = labels[val_split_idx:test_split_idx]
    labels_test = labels[test_split_idx:]


    return (X_train, X_val, X_test, labels_train, labels_val, labels_test)

def move_target_at_the_end(data:pd.DataFrame, target_column:str)->pd.DataFrame:
    # Move 'open_solana' at the end
    columns = [col for col in data.columns if col != target_column] 
    columns.append('open_solana')  
    data = data[columns] 
    return data

# Legacy Functions -to be deleted

# def create_featured_label(data, time_steps, num_predictions):
#     """
#         Creates an extra label that has the percentage change of the next num_predictions days.
#     """
#     percentage_change_label = []
    
#     for i in range(len(data) - time_steps-num_predictions):
#         first_label_row_index = i+time_steps
#         labels = data[first_label_row_index:first_label_row_index+num_predictions, -1]
#         first_price = labels[0]
#         labels = 100*(labels - first_price) / first_price
#         labels = [round(l,2) for l in labels]
#         percentage_change_label.append(labels)
#     return np.array(percentage_change_label)


# def concatenate_labels(labels1, labels2):
#     y = []
#     for i in range(len(labels1)):
#         y.append(np.concatenate((labels1[i],labels2[i])))
#     return np.array(y)
# # y = concatenate_labels(y, y_percentage_change)