import cv2 as cv

img = cv.imread("Photos/park.jpg")
# cv.imshow("Cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)


blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

edge = cv.Canny(blur, 175, 185)
cv.imshow("Canny", edge)

dilated = cv.dilate(edge, (3,3), iterations=1)
cv.imshow("Dilate", dilated)

resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resize", resize)

cropped =

cv.waitKey(0)