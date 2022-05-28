# import glob
# import cv2
# cv_img = []
# for img in glob.glob("B3_May_25_2022_16-30_Ashik_Mostofa/B-3.1/images/*.png"):
#     n= cv2.imread(img)
#     cv_img.append(n)
# print(cv_img)


"""
import cv2
import glob

imdir = 'path/to/files/'
ext = ['png', 'jpg', 'gif']    # Add image formats here

files = []
[files.extend(glob.glob(imdir + '*.' + e)) for e in ext]

images = [cv2.imread(file) for file in files]

"""

# import cv2
# import glob

# imdir = 'B3_May_25_2022_16-30_Ashik_Mostofa/B-3.1/images/'
# ext = ['png', 'jpg', 'gif']    # Add image formats here

# files = []
# [files.extend(glob.glob(imdir + '*.' + e)) for e in ext]

# images = [cv2.imread(file) for file in files]

# print(images)



import cv2
import numpy as np
import os
# from collections import Counter
import matplotlib.pyplot as plt

destination='reorganized/'

path='B3_May_25_2022_16-30_Ashik_Mostofa/B-3.1/images/213_s_141_F.jpg.png'
# path='B3_May_25_2022_16-30_Ashik_Mostofa/B-3.1/images/100_s_207_F.jpg.png'
# path= "B3_May_25_2022_16-30_Ashik_Mostofa/B-3.1/images/1_s_144_F.jpg.png"
# path="B3_May_25_2022_16-30_Ashik_Mostofa/B-3.1/images/465_s_163_M.jpg.png"
# img = cv2.imread("B3_May_25_2022_16-30_Ashik_Mostofa/B-3.1/images/1_s_144_F.jpg.png" , cv2.IMREAD_UNCHANGED)
img = cv2.imread(path , cv2.IMREAD_UNCHANGED)

print(img.shape)
a= np.array(img)
print(img.ndim)
print('Maximum RGB value in this image {}'.format(img.max()))
print('Minimum RGB value in this image {}'.format(img.min()))
(B, G, R) = cv2.split(img)
# test= Counter(R)
# print(test)

print(R.max())
print(R.min())

print(f"type:{type(R)} shape: {R.shape}")


# image= cv2.imread('Tropical-tree.jpg')

# equ = cv2.equalizeHist(img)
equ = cv2.equalizeHist(R)
print(equ.shape)
res = np.hstack((R,equ)) #stacking images side-by-side
# cv2.imwrite('res.png',res)
un, cnt = np.unique(equ, return_counts=True)
counted_pixels= dict(zip(un, cnt))
print(dict(zip(un, cnt)))
print (counted_pixels)

print(un)
print(un.size)



#sort ascending order

sortlist = sorted(counted_pixels.items(), key=lambda x:x[1])
# sortdict = dict(sortlist)
# print(sortdict)
print(sortlist)

def returnImageMarkers(sortedlist):
    stkr=sortedlist[-3][0]
    cw=sortedlist[-2][0]
    bg=sortedlist[-1][0]

    return stkr , cw , bg
textfile = open(os.path.join(destination,'filelist.txt' ), "w")
try:
    sticker, cow , background = returnImageMarkers(sortlist)
except:
    textfile.write(path + "\n")
    textfile.close()
    exit()
    
               
# sticker, cow , background = returnImageMarkers(sortlist)
# print( sticker, cow , background )


imagemap = {
    sticker:2,
    cow:1,
    background:0
}

plt.imshow(cv2.cvtColor(res , cv2.COLOR_BGR2RGB))
plt.show()

# setting cow=2 , sticker =1 , background = 0

frame=np.zeros(R.shape, dtype="uint8")
# frame.shape
h,w = frame.shape

for x in range(w):
    for y in range(h):
        try:
            frame[y,x] = imagemap[equ[y,x]]
        except:
            frame[y,x]=imagemap[background]


head_tail=os.path.split(path)
head_tail[0]
final_destination =os.path.join(destination,os.path.split(path)[0])
print(final_destination)
print(os.path.join(final_destination,head_tail[1]))
print (type(final_destination))

if os.path.exists(final_destination) == False :
    try:
        os.makedirs(os.path.join(final_destination), exist_ok=True)
    except OSError as error:
        print(error)

cv2.imwrite(os.path.join(final_destination,head_tail[1]), frame)        


# equ[0:cY, 0:cX]
# equ[0:700, 0:1000]


plt.imshow(cv2.cvtColor(frame , cv2.COLOR_BGR2RGB))
plt.show()

# cv2.imshow('dsa',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# frame=np.zeros(R.shape, dtype="uint8")
# frame.shape
# def 