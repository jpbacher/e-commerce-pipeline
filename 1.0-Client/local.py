import os
import csv
import json
import requests

PROJ_ROOT = os.path.join(os.pardir)
data_path = os.path.join(PROJ_ROOT, 'data', 'ecommerce.csv')

def read_csv_to_json(filepath, header_row = None):

    """Converts csv file to json doc

    Args:
        filepath (string): file path to the csv
        header_row (Boolean): whether file has header row 
    """

