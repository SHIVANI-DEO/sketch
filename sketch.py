import cv2
x =2
y= 7
img= cv2.imread("sketch/h.jpg")
cv2.imshow("cartoon", img)
cv2.waitKey(0)
img_org = img
for i in range(x):
    img_color = cv2.pyrDown(img_org)
for i in range(y):
    img_color = cv2.bilateralFilter(img_org, d=10,
                                    sigmaColor=9,
                                    sigmaSpace=7)
for i in range(x):
    img_color = cv2.pyrUp(img_org)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_blur = cv2.medianBlur(img_gray, 7)
img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY,
                                 blockSize=9,
                                 C=2)
img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
img_cartoon = cv2.bitwise_and(img_org, img_edge)
cv2.imshow("cartoon", img_cartoon)
cv2.waitKey(0)


