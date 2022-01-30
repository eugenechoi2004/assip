import cv2
img1 = cv2.imread("imageComparisons/CubbonPark1.jpeg")
img2 = cv2.imread("imageComparisons/blacksoil.jpeg")

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# sift
sift = cv2.xfeatures2d.SIFT_create()

keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

matches = bf.match(descriptors_1, descriptors_2)
matches = sorted(matches, key=lambda x: x.distance)
print(len(matches))
img3 = cv2.drawMatches(img1, keypoints_1, img2,
                       keypoints_2, matches[:50], img2, flags=2)

# save cv2 image img3
cv2.imwrite("imageComparisons/sift.jpeg", img3)
