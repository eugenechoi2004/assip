import os
import json
import shutil
path='/Users/eugene/Documents/mapillaryText/labels/txt'
folders = []
lines = open('new.txt').readlines()
for line in lines:
    folders.append(line.strip().split(' ')[0])
print(folders)
reader = json.load(open('final.json'))

output = open('output.txt','w')
for element in folders:
    for fileName in os.listdir(path):
        lines = open(os.path.join(path,fileName)).readlines()
        for line in lines:
            if element in line:
                output.write(str(reader[fileName.replace('.txt','')]['geometry']['coordinates']).replace(',','').replace('[','').replace(']',''))
                output.write(' '+element)
                output.write('\n')
                break

output.close()