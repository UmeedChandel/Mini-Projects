'''
PACKAGES
cmake
dlib
face recognition
opencv
'''

import cv2 					 # computer vission liberary
import face_recognition

# STEP 1: load images and convert to RGB as the cv2 lib reads it

img = face_recognition.load_image_file('FUmeed.jpg')  				# load 1st image
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  						# convert to RGB
imgTest = face_recognition.load_image_file('TUmeed1.jpg')  			# load 2nd image
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)  				# convert to RGB

# STEP 2: find faces in loaded images and encodings(128 measurements) the faces

faceLoc = face_recognition.face_locations(img)[0]  										     	 # finding face loaction
encodeImg = face_recognition.face_encodings(img)[0] 											 # encode the detected face [0] 1st element
cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 0, 255), 4)  		 # draw recatngle where face located [img,points,colour,thickness]

faceLocTest = face_recognition.face_locations(imgTest)[0]  										 # same for 2nd image
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (0, 0, 255), 4)

imgS = cv2.resize(img, (0, 0), None, 0.50, 0.50)
imgTestS = cv2.resize(imgTest, (0, 0), None, 0.50, 0.50)

# STEP 3: comparing faces and finding distances b/w them using linear SVM(backend)

results = face_recognition.compare_faces([encodeImg], encodeTest)  														# input list of faces and the comparing image
faceDis = face_recognition.face_distance([encodeImg], encodeTest)  														# how similar to find best match by comparing distance
print(results, faceDis)  																								# lower the distance more similar the face
cv2.putText(imgTestS, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 255), 2)    # displaying txt as "result: face distance"

cv2.imshow('Original', imgS)  # display image
cv2.imshow('Test', imgTestS)  # display image
cv2.waitKey(0)