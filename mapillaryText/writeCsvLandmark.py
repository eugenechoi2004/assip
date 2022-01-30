import csv 
import os
import json
# field names 
fields = ['ImageId', 'Lat','Long', 'Confidence', 'Quality','Feature'] 

reader = json.load(open('final.json'))
label = [['park','square'], ['museum'], 'Fence', 'Recreation', 'Advertising']
labelDir = '/Users/eugene/Documents/mapillaryText/labels/txt'


rows = []

def func1(ImageId, Confidence, Feature):
    lat = reader[ImageId]['geometry']['coordinates'][0]
    lon = reader[ImageId]['geometry']['coordinates'][1]
    qs = reader[ImageId]['quality_score']
    return [ImageId, lat, lon, Confidence, qs, Feature]
    

for filename in os.listdir(labelDir):
    element = open(os.path.join(labelDir,filename),'r')
    element = [line.rstrip('\n') for line in element]
    for i in label:
        if i in str(element):
            for line in element:
                if i in line:
                    #Feature
                    f = line.split(' ')[0]
                    #confidence
                    c = float(line.split(' ')[1])
                    #image id
                    Iid = filename.replace('.txt','')
                    rows.append(func1(Iid,c,f))






filename = 'landmark'
    
filename = filename+'.csv'
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)
