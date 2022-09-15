# %%
import cv2
import numpy as np
import os
# from collections import Counter
import matplotlib.pyplot as plt
# %%
destination = 'data/changed_mask_test'
path = 'data/motorbikedata/Screenshot (423).png.png___fuse.png'
# %%
img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
print(img.shape)
# %%
type(cv2.split(img))
sp = cv2.split(img)
len(sp)
# print(sp)
(B, G, R, A) = cv2.split(img)
# %%
# cv2.imshow("Model Blue Image", B)
# cv2.waitKey(0)
# %%
# # plt.imshow(cv2.cvtColor(B , cv2.COLOR_BGR2RGB))
# plt.subplot(2, 2, 1), plt.imshow(B)
# plt.subplot(2, 2, 2), plt.imshow(G)
# plt.subplot(2, 2, 3), plt.imshow(R)
# plt.subplot(2, 2, 4), plt.imshow(A)
# # plt.imshow(B)
# plt.show()
# %%
imagemap = dict(
    moveable=0,
    rider=1,
    myBike=2,
    road=3,
    lanemark=4,
    undriveable=5
)
print(imagemap)
"""
images are in BGR formate in openCV but mappings are in RGB
"""
# colourMap = {
#     'moveable': [ 92, 234, 57 , 255],
#     'rider': [ 6,117, 65, 255 ],
#     'myBike': [226, 144, 74 , 255 ],
#     'road': [155 ,155 ,155 , 255 ] ,
#     'lanemark': [ 28, 231, 248 , 255 ] ,
#     'undriveable': [35 , 245 , 166, 255 ]
# }
print(R.shape)
frame = np.zeros(R.shape, dtype="uint8")
h, w = frame.shape
# %%
print(img[2, 2])
print(type(img[2, 2]))
print(type(list(img[2, 2])))
print(len(list(img[2, 2])))
img[2, 2][0]
# %%
# colourMap = {
#     'moveable': [ 92, 234, 57 , 255],
#     'rider': [ 6,117, 65, 255 ],
#     'myBike': [226, 144, 74 , 255 ],
#     'road': [155 ,155 ,155 , 255 ] ,
#     'lanemark': [ 28, 231, 248 , 255 ] ,
#     'undriveable': [35 , 245 , 166, 255 ]
# }
colourMap = dict(
    moveable=[92, 234, 57, 255],
    rider=[6, 117, 65, 255],
    myBike=[226, 144, 74, 255],
    road=[155, 155, 155, 255],
    lanemark=[28, 231, 248, 255],
    undriveable=[35, 166, 245, 255]
)
colourMap


# function to return key for any value
def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"
# %%
