import shutil
import os
import csv
import json
path = "/Users/eugene/Documents/mapillaryText/logos/txt"
total = dict()
reader = json.load(open('final.json'))
fields = ['ImageId', 'Lat','Long', 'Confidence', 'Quality','Feature'] 

def func1(ImageId, Confidence, Feature):
    lat = reader[ImageId]['geometry']['coordinates'][0]
    lon = reader[ImageId]['geometry']['coordinates'][1]
    qs = reader[ImageId]['quality_score']
    return [ImageId, lat, lon, Confidence, qs, Feature]


rows = []

for filename in os.listdir(path):
    name = open(os.path.join(path,filename),'r').readlines()
    for line in name:
        line = line.strip()
        if "bound" not in line:
            temp = line.split(' ')
            obj = ' '.join(temp[0:-1])
            print(temp)
            confidence = float(temp[-1])
            rows.append(func1(filename.replace('.txt',''),confidence,obj))


filename = 'FinalLogos'
    
filename = filename+'.csv'
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)


