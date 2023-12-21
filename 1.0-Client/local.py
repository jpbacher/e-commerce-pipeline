import os
import csv
from datetime import datetime
import json
import requests

PROJ_ROOT = os.path.join(os.pardir)
DATA_PATH = os.path.join(PROJ_ROOT, 'data', 'ecommerce.csv')
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



def csv_to_json_post_API(filepath, columns, url, header_row = None):

    """Converts csv file to json doc

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

            if i > 6:
                break
            json_doc = json.dumps(doc)

            response = requests.post(url, json_doc)
            print(response)



def main():

    csv_to_json_post_API(filepath=DATA_PATH, columns=COLUMNS, url=URL, header_row = None):

if __name__ == '__main__':
    main()
