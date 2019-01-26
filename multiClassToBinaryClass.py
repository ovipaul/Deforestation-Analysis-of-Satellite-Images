import cv2
import os
import numpy as np
from tqdm import tqdm

load_dir ="label"
img_dir = "F:/Workspace/test/"+load_dir

progressbar = tqdm(os.listdir(img_dir))

for image in progressbar:
    progressbar.set_description('Processing element: {}'.format(image))
    img = cv2.imread(os.path.join(load_dir, image),1)
    file_name, file_ext = os.path.splitext(image)
    row = img.shape[0]
    col = img.shape[1]
    cha = img.shape[2]
    proc_img = np.zeros((row,col,cha))
    proc_img = np.array(proc_img)
    for i in tqdm(range(row)):
        for j in range(col):
            if img[i, j, 0] == 255 and img[i, j, 1] == 255:
                proc_img[i, j, 0] = 255
                proc_img[i, j, 1] = 0
                proc_img[i, j, 2] = 0
            else:
                proc_img[i, j, 0] = 0
                proc_img[i, j, 1] = 0
                proc_img[i, j, 2] = 255
    cv2.imwrite('binaryLabel/' + file_name + file_ext, proc_img)