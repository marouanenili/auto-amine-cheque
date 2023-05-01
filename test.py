import requests
import json
import csv

# Define the bounding box for Albania
bbox = (19.180228, 39.644862, 21.057318, 42.661259)

# Construct the OverPass API query to fetch all the addresses in the bounding box
url = 'https://overpass-api.de/api/interpreter'
query_template = '''
[out:json];
node[%s](%f,%f,%f,%f);
out;
'''

query = query_template % ('"addr:street"|"addr:city"|"addr:postcode"', bbox[1], bbox[0], bbox[3], bbox[2])
print(query)
# Make the request to the OverPass API
response = requests.post(url, data=query)
print(response.text)
# Parse the response as JSON
data = json.loads(response.text)

# Save the addresses to a CSV
with open('addresses.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['streetname', 'city', 'postcode', 'region', 'latitude', 'longitude'])
    for element in data['elements']:
        # Only process nodes with address information
        if 'tags' in element and 'addr:street' in element['tags']:
            streetname = element['tags']['addr:street']
            city = element['tags'].get('addr:city', '')
            postcode = element['tags'].get('addr:postcode', '')
            region = element['tags'].get('addr:region', '')
            latitude = element['lat']
            longitude = element['lon']
            writer.writerow([streetname, city, postcode, region, latitude, longitude])