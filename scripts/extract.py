from geopy.geocoders import GoogleV3
import csv
import re

f=open(raw_input('Output file: '),'w')
with open('../data/fy13b.csv', 'rU') as csvfile:
    fp = csv.reader(csvfile, delimiter=',', quotechar='"')
    n = 0
    for row in fp:
        n = n+1
        try:
            date = row[0]
            place = row[1]
            description = row[2]
            incident_type = row[3]
            
            match = re.search(r"\s([A-Z][A-Z])(\s[0-9]*)$", place)
            
            if match:
                state = match.group(1)
                
                geolocator = GoogleV3()
                address, (latitude, longitude) = geolocator.geocode(str(place))
                new_coords = str(latitude), str(longitude)
                lat_coords = str(latitude)
                long_coords = str(longitude)
                
                csv_row = state + ',' + date + ',"' + place + '",' + description + ',' + incident_type + ',' + lat_coords + ',' + long_coords
                print csv_row
                
                print>>f, csv_row
            
        except:
            pass
        
f.close()

