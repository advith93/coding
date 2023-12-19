import requests
import json
import argparse

# Fetch data from the API
response = requests.get('https://www.travel-advisory.info/api')
data = response.json()

# Save data to a file
with open('data.json', 'w') as f:
    json.dump(data, f)

# Load data from the file
with open('data.json', 'r') as f:
    data = json.load(f)

# Define a function for looking up country names
def lookup_country_name(country_codes):
    for code in country_codes:
        print(data['data'][code]['name'])

# Set up command-line arguments
parser = argparse.ArgumentParser(description='Look up country names by their codes.')
parser.add_argument('--countryCode', nargs='+', help='one or more country codes')

# Parse command-line arguments
args = parser.parse_args()

# Look up country names
lookup_country_name(args.countryCode)
