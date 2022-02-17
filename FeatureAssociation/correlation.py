import cv2
import os


def compare(img1Path, img2Path, id1, id2):
    print(id1, id2)
    img1 = cv2.imread(img1Path)
    img2 = cv2.imread(img2Path)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # sift
    sift = cv2.xfeatures2d.SIFT_create()
    keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)
    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
    matches = bf.match(descriptors_1, descriptors_2)
    matches = sorted(matches, key=lambda x: x.distance)
    img3 = cv2.drawMatches(img1, keypoints_1, img2,
                           keypoints_2, matches[:50], img2, flags=2)
    cv2.imwrite("correlations/"+str(id1)+'+'+str(id2)+'.jpg', img3)
    return str(id1)+'+'+str(id2), str(len(matches))


comp = open('compare.txt', 'w')
# reading from a file without the new lines
banks = [line.strip() for line in open('output.txt', 'r').readlines()]
rootPath = '/Users/eugene/Documents/GitHub/assip/mapillaryText/images'
for index, bank in enumerate(banks):
    firstPath = os.path.join(rootPath, bank)
    for index1, bank1 in enumerate(banks):
        secondPath = os.path.join(rootPath, bank1)
        if (bank != bank1):
            name, matches = compare(firstPath, secondPath, index, index1)
            comp.write(name+' '+matches+'\n')

comp.close()
