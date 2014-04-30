import csv

f=open(raw_input('Output file: '),'w')
with open('../data/formatted/data_cleaned.csv', 'rU') as csvfile:
    fp = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in fp:
        state = row[0]
        date = row[1]
        place = row[2]
        description = row[3]
        incident_type = row[4]
        latitude = row[5]
        longitude = row[6]
        number = row[7]

        new_coords = str(latitude), str(longitude)
        lat_coords = str(latitude)
        long_coords = str(longitude)
                    
        csv_row = state + ',' + number + ',' + date + ',"' + place + '","' + description + '",' + incident_type + ',' + lat_coords + ',' + long_coords + ',' +'"<img src=\'http://maps.googleapis.com/maps/api/staticmap?center=' + lat_coords + ',' + long_coords + '&zoom=4&size=150x75&maptype=roadmap&style=feature:road|visibility:on|color:0xc8c8c6&style=feature:poi|element:geometry|visibility:off&style=feature:road|element:labels.icon|visibility:off&style=element:geometry.stroke|color:0x808080|weight:0.8&style=feature:landscape.natural|visibility:simplified|color:0xececed&markers=size:tiny%7Ccolor:0xBA0D0D%7C' + lat_coords + ',' + long_coords + '&sensor=false\' />"'
        print csv_row
         
        print>>f, csv_row
f.close()
