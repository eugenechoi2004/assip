import os
import json
import shutil
path='/Users/eugene/Documents/mapillaryText/labels/txt'
folders = []
lines = open('labels.txt').readlines()
for line in lines:
    folders.append(line.strip().split(' ')[0])

for element in folders:
    os.mkdir('labelOutputs/'+element)
    os.mkdir('labelOutputs/'+element+'/images')
    os.mkdir('labelOutputs/'+element+'/txt')
    for filename in os.listdir(path):
        lines = open(os.path.join(path,filename),'r').readlines()
        for line in lines:
            if element in line.strip():
                shutil.copyfile(os.path.join(path,filename),'labelOutputs/'+element+'/txt/'+filename)
                shutil.copyfile('images/'+filename.replace('txt','jpg'),'labelOutputs/'+element+'/images/'+filename.replace('txt','jpg'))
                break

