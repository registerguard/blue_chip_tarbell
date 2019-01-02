#! /usr/bin/env python
# coding: utf-8

import csv
import json
import re

with open("../secrets.json") as f:
    secrets = json.loads(f.read())

# https://codereview.stackexchange.com/questions/145511/performing-a-regex-search-and-saving-results-to-csv

def main():
    cleaned_data = []
    # TODO: Use argparse like https://github.com/newsdev/ap-precinct-parser
    with open(secrets['LANE_COUNTY_SALES_DATA_CSV'], 'r') as f:
        # https://stackoverflow.com/questions/27432162/python-how-to-trim-trailing-spaces-in-csv-dictreader-keys#answer-27432264
        header = [h.strip() for h in f.next().split(',')]
        reader = csv.DictReader(f, fieldnames=header)
        for row in reader:
            addr = row['Address']
            addr = re.sub(r' DR,([A-Z])', r' DRIVE,\1', addr, 1)
            addr = re.sub(r' LN,([A-Z])', r' LANE,\1', addr, 1)
            addr = re.sub(r' RD,([A-Z])', r' ROAD,\1', addr, 1)
            addr = re.sub(r' CT,([A-Z])', r' COURT,\1', addr, 1)
            addr = re.sub(r' PL,([A-Z])', r' PLACE,\1', addr, 1)
            addr = re.sub(r' HWY ', ' HIGHWAY ', addr, 1)
            addr = re.sub(r' (ST|AVE|BLVD),([A-Z])', r' \1.,\2', addr)
            addr = re.sub(r' HWY', r' HIGHWAY', addr)
            addr = re.sub(r' ([NESW]) ', r' \1. ', addr, 1)
            addr = re.sub(r',OR?,?[\d-]{0,10},?U?S?A?$', r'', addr, 1)
            addr = re.sub(r',', r', ', addr)
            row['Address'] = addr
            # print(row['Address'])

            owner = row['Seller']
            owner = re.sub(r' ([A-Z])( |$)', r' \1.\2', owner)
            row['Seller'] = owner
            # print(row['Seller'])

            owner = row['Buyer']
            owner = re.sub(r' ([A-Z])( |$)', r' \1.\2', owner)
            row['Buyer'] = owner
            print(row['Buyer'])

            sales_price = row['Sales Price']
            sales_price = sales_price.strip()
            row['Sales Price'] = sales_price

            # Hey! This goes last, after all the clean-ups!
            cleaned_data.append(row)

    # write it out to a new file
    with open('cleaned_property_sales.csv', 'wb') as out_file:
        writer = csv.DictWriter(out_file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_data)

if __name__ == "__main__":
    main()
