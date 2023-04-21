import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "sun", (20,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img, "mercury", (100,250), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img, "venus", (190,180), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img, "earth", (285,265), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img, "mars", (380,180), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img, "jupiter", (560,380), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img, "saturn", (770,100), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img, "uranus", (965,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img, "neptune", (1100,120), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imshow("img", img)

cv2.waitKey(0)