import cv2
import numpy as np

img = cv2.imread("src/manipulator/src/image/image.png")


# 히스토그램 평활화


img_arr = np.array(img)
print(img_arr)
print(img_arr.shape)
arr = np.zeros((959, 970, 3))


for i in range(959):
    for j in range(970):
        if (img_arr[i][j] < 120).all():
            arr[i][j] = [0, 0, 0]
        else:
            arr[i][j] = [255, 255, 255]

cv2.imwrite("src/manipulator/src/image/black_only.jpg", arr)

cv2.imshow("Black Only", arr)
cv2.waitKey(0)


img = cv2.imread('src/manipulator/src/image/black_only.jpg')
filtered_img = cv2.medianBlur(img, 5)
cv2.imshow('Filtered Image', filtered_img)

cv2.imwrite("src/manipulator/src/image/final.jpg", filtered_img)
cv2.waitKey(0)



