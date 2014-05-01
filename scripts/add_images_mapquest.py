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
        
        try:
            float_long = float(long_coords)
            float_lat = float(lat_coords)
        
            long_sub = float_long - .9
            lat_sub = float_lat - .3
            add_one = long_sub + 1
            add_one_b = lat_sub + 1
        
            long_fix = str(long_sub)
            lat_fix = str(lat_sub)
            bumpedView = str(add_one)
            bumpedView_b = str(add_one_b)
         
            csv_row = state + ',' + number + ',' + date + ',"' + place + '","' + description + '",' + incident_type + ',' + lat_coords + ',' + long_coords + ',' +'"<div class=\'image-cropper\'><img class=\'right\' src=\'http://www.mapquestapi.com/staticmap/v4/getmap?size=150,100&zoom=4&type=map&xis=www2.psd100.com%2Fppp%2F2013%2F10%2F0501%2FMap-of-the-red-pushpin-icon-1005121630.png,1,C,' + lat_fix + ',' + long_fix + ',&scale=6770&center=' + bumpedView_b + ',' + bumpedView + '&declutter=true&imagetype=JPEG&projection=sm&key=Fmjtd%7Cluur2qa7nl%2C85%3Do5-9abx5z\' /></div>"'
            print csv_row
        
        except:
            pass
         
            csv_row = state + ',' + number + ',' + date + ',"' + place + '","' + description + '",' + incident_type + ',' + lat_coords + ',' + long_coords
            print csv_row
         
        print>>f, csv_row
f.close()


