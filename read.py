import cv2 as cv

# 1. Reading images 
#img1 = cv.imread('./Photos/trunks.jpg')
#cv.imshow('Trunks',img1)

#2. Reading video
#capture = cv.VideoCapture('./Video/gau.mp4')
#while True:
    #isTrue, frame = capture.read()
    #cv.imshow('Video',frame)
    #if cv.waitKey(20) & 0xFF==ord('d'):
        #break
#capture.release()

# 3. Face recogniser

img = cv.imread('./Photos/family.jpg')
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Grayscale image',gray)


haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray ,scaleFactor=1.1, minNeighbors=3)

print(f'The number of faces found is = {len(faces_rect)}')

cv.waitKey(0)