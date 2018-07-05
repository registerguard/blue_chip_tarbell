#! /usr/bin/env python
# coding: utf-8

import csv
import re

# https://codereview.stackexchange.com/questions/145511/performing-a-regex-search-and-saving-results-to-csv

def main():
    cleaned_data = []
    with open('RegisterGuardReports.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            addr = row['Site Address']
            addr = re.sub(r' EUG$', '', addr, 1)
            addr = re.sub(r'DR$', 'DRIVE', addr, 1)
            addr = re.sub(r'LN$', 'LANE', addr, 1)
            addr = re.sub(r' RD', ' ROAD', addr, 1)
            addr = re.sub(r'LP$', 'LOOP', addr, 1)
            addr = re.sub(r'PL$', 'PLACE', addr, 1)
            addr = re.sub(r'ALY$', 'ALLEY', addr, 1)
            addr = re.sub(r' BLDG ', ' BLDG. ', addr, 1)
            addr = re.sub(r'(ST|AVE)$', r'\1.', addr)
            addr = re.sub(r' ([NESW]) ', r' \1. ', addr, 1)
            row['Site Address'] = addr
            cleaned_data.append(row)
            print('{}'.format(row['Site Address']))

        out_file = open('cleaned.csv', 'wb')
        writer = csv.DictWriter(out_file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_data)

if __name__ == "__main__":
    main()
