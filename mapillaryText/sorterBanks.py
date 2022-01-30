import os
import json
import shutil
path='/Users/eugene/Documents/mapillaryText/logos/txt'
folders = []
lines = open('labels.txt').readlines()
key = 'BANK'
f = open('Banks/outputBanks.txt','w')
reader = json.load(open('final.json'))


for fileName in os.listdir(path):
    lines = open(os.path.join(path,fileName),'r').readlines()
    for line in lines[::2]:
        print(line.strip().upper())
        if key in line.strip().upper():
            f.write(str(reader[fileName.replace('.txt','')]['geometry']['coordinates']).replace(',','').replace('[','').replace(']',''))
            f.write('\n')
            print('f')
            shutil.copyfile('/Users/eugene/Documents/mapillaryText/logos/images/'+fileName.replace('txt','jpg'),'/Users/eugene/Documents/mapillaryText/Banks/images/'+fileName.replace('txt','jpg'))
            break

f.close()
