#! /usr/bin/env python
# coding: utf-8

import csv
import re

# https://codereview.stackexchange.com/questions/145511/performing-a-regex-search-and-saving-results-to-csv

def main():
    cleaned_data = []
    with open('LaneCountypermits_June2018.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            addr = row['Situs Address']
            addr = re.sub(r' EUG$', '', addr, 1)
            addr = re.sub(r'DR ?$', 'DRIVE', addr, 1)
            addr = re.sub(r'LN ?$', 'LANE', addr, 1)
            addr = re.sub(r' RD', ' ROAD', addr, 1)
            addr = re.sub(r'LP ?$', 'LOOP', addr, 1)
            addr = re.sub(r'CT ?$', 'COURT', addr, 1)
            addr = re.sub(r'PL ?$', 'PLACE', addr, 1)
            addr = re.sub(r'ALY$', 'ALLEY', addr, 1)
            addr = re.sub(r' BLDG ', ' BLDG. ', addr, 1)
            addr = re.sub(r' HWY ', ' HIGHWAY ', addr, 1)
            addr = re.sub(r'(ST|AVE|BLVD) ?$', r'\1.', addr)
            addr = re.sub(r' HWY$', r' HIGHWAY', addr)
            addr = re.sub(r' ([NESW]) ', r' \1. ', addr, 1)
            row['Situs Address'] = '{}, {}'.format(addr, row['Situs City'])
            print(row['Situs Address'])

            cleaned_data.append(row)

            owner = row['Owner Name']
            owner = re.sub(r' ([A-Z])( |$)', r' \1.\2', owner)
            row['Owner Name'] = owner
            print(row['Owner Name'])

    # write it out to a new file
    with open('cleaned.csv', 'wb') as out_file:
        writer = csv.DictWriter(out_file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_data)

if __name__ == "__main__":
    main()
