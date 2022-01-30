import os
import json
import collections
path = '/Users/eugene/Documents/mapillaryText/labels/txt'
keys = {}
for filename in os.listdir(path):
    filename = os.path.join(path,filename)
    lines = open(filename,'r').readlines()
    for line in lines:
        line = line.strip().split(' ')
        if line[0] not in keys:
            keys[line[0]]=1
        else:
            keys[line[0]]+=1
        
sort_orders = sorted(keys.items(), key=lambda x: x[1], reverse=True)

f = open('labels.txt','w')
for i in list(sort_orders):
    f.write(i[0]+' '+str(i[1])+'\n')
f.close()

