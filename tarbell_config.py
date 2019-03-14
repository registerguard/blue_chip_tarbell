# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

import csv
import json
with open("secrets.json") as f:
    secrets = json.loads(f.read())

# Google spreadsheet key
# Lane County building permits
# SPREADSHEET_KEY = "1YlfgCOPl2tNLrbcLKLXCtrAaKYeqRZILz_PwIQGtpng"

# Lane County property sales
SPREADSHEET_KEY = secrets['SPREADSHEET_KEY']

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Spreadsheet cache lifetime in seconds. (Default: 4)
# SPREADSHEET_CACHE_TTL = 4

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# Get context from a local file or URL. This file can be a CSV or Excel
# spreadsheet file. Relative, absolute, and remote (http/https) paths can be 
# used.
# CONTEXT_SOURCE_FILE = ""

# EXPERIMENTAL: Path to a credentials file to authenticate with Google Drive.
# This is useful for for automated deployment. This option may be replaced by
# command line flag or environment variable. Take care not to commit or publish
# your credentials file.
# CREDENTIALS_PATH = ""

# S3 bucket configuration
S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
    
    "production": "cloud.registerguard.com/blue_chip_tarbell",
    "staging": "uploads.registerguard.com/blue_chip_tarbell",
}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'blue_chip_tarbell',
    'title': 'Blue Chip real estate data'
}

# Add a new route
from flask import Blueprint, g, render_template, Response

blueprint = Blueprint('blue_chip_tarbell', __name__)

@blueprint.route('/permits/')
def formatted_permits():
    context = g.current_site.get_context()
    content = render_template('permits/index.html',  **context)
    response = Response(content)
    return response

@blueprint.route('/lane_permits/')
def formatted_lane_permits():
    context = g.current_site.get_context()
    content = render_template('lane_permits/index.html',  **context)
    response = Response(content)
    return response

# Let's just go from a local .csv file to flask:
# https://first-news-app.readthedocs.io/en/latest/
# http://2015.compjour.org/homework/flask-app-101/

def get_csv():
    csv_path = './_scripts/cleaned_property_sales.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

@blueprint.route('/property_sales/')
def formatted_property_sales():
    # context = g.current_site.get_context()
    # content = render_template('property_sales/index.html',  **context)
    object_list = get_csv()
    content = render_template('property_sales/index.html',  cleaned_property_sales=object_list)
    response = Response(content)
    return response