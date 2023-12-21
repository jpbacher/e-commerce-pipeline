import os
import csv
from datetime import datetime
import json
import requests

PROJ_ROOT = os.path.join(os.pardir)
data_path = os.path.join(PROJ_ROOT, 'data', 'ecommerce.csv')

def read_csv_to_json(filepath, columns, header_row = None):

    """Converts csv file to json doc

    Args:
        filepath (string): file path to the csv
        columns (list): column names
        header_row (Boolean): whether file has header row 
    """

    with open(data_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=columns)
        if header_row:
            next(reader)
        for i, row in enumerate(reader):
            doc = {
                "InvoiceNo": int(row["InvoiceNo"]),
                "StockCode": int(row["StockCode"]),
                "Description": row["Description"],
                "Quantity": int(row["Quantity"]),
                "InvoiceDate": datetime(row["InvoiceDate"]),
                "UnitPrice": float(row["UnitPrice"]),
                "CustomerID": int(row["CustomerID"]),
                "Country": row["Country"]
            }
        
