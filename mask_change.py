import cv2
import fname_ret as fnr
import os
import numpy as np
# from numba import njit


# Source path of images
sourcePath = 'B3_May_25_2022_16-30_Ashik_Mostofa/'

# destination path where files need to organized
destination = 'reorganized/'

ext = ('png', 'jpg', 'gif')    # Add image formats here

# file type that need to select
files = fnr.filname_ret(rootpath=sourcePath, file_types=ext).fileDirectory

# fnr.filname_ret.showList(files)
# print(len(files))

if os.path.exists(destination) == False:
    try:
        os.makedirs(os.path.join(destination), exist_ok=True)
    except OSError as error:
        print(error)


def returnImageMarkers(sortedlist):
    stkr = sortedlist[-3][0]
    cw = sortedlist[-2][0]
    bg = sortedlist[-1][0]

    return stkr, cw, bg

# @njit(parallel=True)


def mask_change(file_list):
    textfile = open(os.path.join(destination, 'ErrorFileList.txt'), "w")
    for fil in file_list:
        # print(fil)
        print(f"Processing {fil}")
        img = cv2.imread(fil)
        head_tail = os.path.split(fil)
        final_destination = os.path.join(destination, head_tail[0])
        if os.path.exists(final_destination) == False:
            try:
                os.makedirs(os.path.join(final_destination), exist_ok=True)
            except OSError as error:
                print(error)

        (B, G, R) = cv2.split(img)
        equ = cv2.equalizeHist(R)
        un, cnt = np.unique(equ, return_counts=True)
        counted_pixels = dict(zip(un, cnt))
        sortlist = sorted(counted_pixels.items(), key=lambda x: x[1])
        try:
            sticker, cow, background = returnImageMarkers(sortlist)
        except:
            print('Error occoured')
            textfile.write(fil + "\n")
            print(IndexError)
            continue

        imagemap = {
            sticker: 2,
            cow: 1,
            background: 0
        }
        # print(imagemap)
        frame = np.zeros(R.shape, dtype="uint8")
        h, w = frame.shape

        for x in range(w):
            for y in range(h):
                try:
                    frame[y, x] = imagemap[equ[y, x]]
                except:
                    frame[y, x] = imagemap[background]

        frame_name = os.path.join(final_destination, head_tail[1])

        cv2.imwrite(frame_name, frame)
        # print(f"Processed to: {frame_name}")
        print('Done!')
    textfile.close()


mask_change(files)
