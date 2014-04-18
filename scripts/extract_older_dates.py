from geopy.geocoders import GoogleV3
import csv
import re

f=open(raw_input('Output file: '),'w')
with open('../data/FatalitiesFY10.csv', 'rU') as csvfile:
    fp = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in fp:
        date = row[2]
        place = row[3]
        description = row[4]
        incident_type = 'Unknown'
            
        match = re.search(r"\s([A-Z][A-Z])(\s[0-9]*)$", place)
            
        if match:
            state = match.group(1)
            
            try:
                geolocator = GoogleV3()
                address, (latitude, longitude) = geolocator.geocode(str(place))
                new_coords = str(latitude), str(longitude)
                lat_coords = str(latitude)
                long_coords = str(longitude)
                
                csv_row = state + ',' + date + ',"' + place + '",' + description + ',' + incident_type + ',' + lat_coords + ',' + long_coords
                print csv_row
                
            except:
                pass
                lat_coords = "--"
                long_coords = "--"
            
                csv_row = state + ',' + date + ',"' + place + '",' + description + ',' + incident_type + ',' + lat_coords + ',' + long_coords
                #csv_row = state + ',' + date + ',"' + place + '",' + description + ',' + incident_type 
                print csv_row
                    
            print>>f, csv_row
f.close()
