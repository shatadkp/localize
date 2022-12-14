import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./drive/my Drive/Colab Notebooks/Image2.png')

image = cv2.imread('/content/sample_data/Image2.png')
fig = plt.figure(figsize = (5, 5))
plt.imshow(image)
plt.xticks([])
plt.yticks([])

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny_edges = cv2.Canny(gray_image, 30, 200)
M = cv2.moments(canny_edges)
cx = int(M['m10'] / M['m00'])
cy = int(M["m01"] / M["m00"])

circle = cv2.circle(image,(cx,cy),5,(255,255,255),-1)
cv2.putText(image,"centroid",(cx-25,cy-25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)

fig=plt.figure(figsize=(5,5))
plt.imshow(image)
plt.xticks([])
plt.yticks([])
