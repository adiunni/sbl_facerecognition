import cv2 as cv

# 1. Reading images 
#img1 = cv.imread('./Photos/trunks.jpg')
#cv.imshow('Trunks',img1)

#2. Reading video
capture = cv.VideoCapture('./Video/gau.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

#cv.waitKey(0)