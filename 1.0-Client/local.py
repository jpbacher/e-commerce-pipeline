from os import path, join, pardir
import csv
import json
import requests
from time import sleep

PROJ_ROOT = path.join(pardir)
DATA_PATH = path.join(PROJ_ROOT, 'data', 'ecommerce.csv')
COLUMNS = [
        "InvoiceNo",
        "StockCode",
        "Description",
        "Quantity",
        "InvoiceDate",
        "UnitPrice",
        "CustomerID",
        "Country"   
    ]
URL = "XXXXXXXXX"



def csv_to_json_post_api(filepath, columns, url, header_row=None):

    """Converts csv file to json and posts to API

    Args:
        filepath (string): file path to the csv
        columns (list): column names
        url (string): url to API endpoint
        header_row (Boolean): whether file has header row 
    """

    with open(DATA_PATH, 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=columns)
        if header_row:
            next(reader)
        for i, row in enumerate(reader):
            
            doc = {
                "InvoiceNo" : int(row["InvoiceNo"]),
                "StockCode": row["Code"],
                "Description": row["Description"],
                "Quantity": int(row["Quantity"]),
                "InvoiceDate": row["InvoiceDate"],
                "UnitPrice": float(row["UnitPrice"]),
                "CustomerID": int(row["CustomeID"]),
                "Country": row["Country"]
            }

            if i > 60:
                sleep(3)
            json_doc = json.dumps(doc)
            
            if i > 300:
                break

            response = requests.post(url, json_doc)
            print(response)



def main():

    csv_to_json_post_api(filepath=DATA_PATH, columns=COLUMNS, url=URL, header_row = None)

if __name__ == '__main__':
    main()
