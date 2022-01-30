import io
import os
import json
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw, ImageFont


client = vision.ImageAnnotatorClient()
def drawVertices(image_source, elements,types,path):
    pillow_img = Image.open(io.BytesIO(image_source))
    draw = ImageDraw.Draw(pillow_img)
    color = 'green'
    if types=='logo':
        color='blue'
    elif types=='landmark':
        color=='red'
    for element in elements:
        display_text = element.description.encode('utf-8')
        vertices = element.bounding_poly.vertices
        for i in range(len(vertices) - 1):
            draw.line(((vertices[i].x, vertices[i].y), (vertices[i + 1].x, vertices[i + 1].y)),
                    fill=color,
                    width=5
            )

        draw.line(((vertices[len(vertices) - 1].x, vertices[len(vertices) - 1].y),
                    (vertices[0].x, vertices[0].y)),
                    fill=color,
                    width=5
        )

        font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 12)
        draw.text((vertices[0].x + 10, vertices[0].y),
                    font=font, text=display_text, 
                    fill=(255, 255, 255))
    pillow_img.save(path)


def detectLabel(image,ident,content):
    txtFile = 'labels/txt/'+ident+'.txt'
    jsonFile = 'labels/json/'+ident+'.json'
    response = client.label_detection(image=image)
    labels = response.label_annotations
    if len(labels)!=0:
        data = {}
        f = open(txtFile,'w')
        for label in labels:
            f.write(label.description.encode('utf-8')+' '+str(label.score))
            f.write('\n')
        data[ident]=labels
        '''
        with open(jsonFile, 'w') as outfile:
            json.dump(list(labels), outfile)
        '''
    
    

def detectLandmark(image,ident,content):
    txtFile = 'landmarks/txt/'+ident+'.txt'
    imageFile = 'landmarks/images/'+ident+'.jpg'
    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    if len(landmarks)!= 0:
        data = {}
        f = open(txtFile,'w')
        for landmark in landmarks:
            f.write(landmark.description.encode('utf-8'))
            f.write('\n')
            for location in landmark.locations:
                lat_lng = location.lat_lng
                f.write('Latitude {}'.format(lat_lng.latitude))
                f.write(' Longitude {}'.format(lat_lng.longitude))
                f.write(' '+str(landmark.score))
                f.write('\n')
        data[ident]=landmarks
        drawVertices(content,landmarks,'landmark',imageFile)
        '''
        with open(jsonFile, 'w') as outfile:
            json.dump(data, outfile)
        '''
    

def detectText(image,ident,content):
    txtFile = 'text/txt/'+ident+'.txt'
    imageFile= 'text/images/'+ident+'.jpg'
    response = client.text_detection(image=image)
    texts = response.text_annotations
    if len(texts)!=0:
        data = {}
        f = open(txtFile,'w')
        for text in texts:
            f.write('{}'.format(text.description.encode('utf-8')))
            f.write(' '+str(text.score))
            vertices = (['({},{})'.format(vertex.x, vertex.y)
                        for vertex in text.bounding_poly.vertices])
            f.write(' bounds: {}'.format(','.join(vertices)))
            f.write('\n')
        drawVertices(content,texts,'text',imageFile)
        data[ident]=texts
        '''
        with open(jsonFile, 'w') as outfile:
            json.dump(data, outfile)
        '''

def detectLogo(image,ident,content):
    txtFile = 'logos/txt/'+ident+'.txt'
    imageFile = 'logos/images/'+ident+'.jpg'
    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    if len(logos)!=0:
        f = open(txtFile,'w')
        for logo in logos:
            f.write(logo.description.encode('utf-8'))
            f.write(' '+str(logo.score))
            f.write('\n')
            vertices = (['({},{})'.format(vertex.x, vertex.y)
                        for vertex in logo.bounding_poly.vertices])
            f.write('bounds: {}'.format(','.join(vertices)))
            f.write('\n')
            vertices = logo.bounding_poly.vertices
        drawVertices(content,logos,'logo',imageFile)
    '''
        with open(jsonFile, 'w') as outfile:
            json.dump(logos, outfile)
    '''



if __name__=='__main__':
    path = 'images'
    counter=15610
    for filename in os.listdir(path)[15610:]:
        file_name = os.path.join(path,filename)
        ident = filename.replace('.jpg','')
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content)
        detectLabel(image,ident,content)
        detectLandmark(image,ident,content)
        detectLogo(image,ident,content)
        detectText(image,ident,content)
        counter+=1
        print(counter)




    
