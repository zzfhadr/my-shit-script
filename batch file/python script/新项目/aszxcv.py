from PIL import Image
import PIL.ImageOps	
import numpy as np
from skimage.io import imsave
import cv2


in_path  = 'whate.bmp'
out_path = 'sadx.jpg'


Image = cv2.imread(in_path)
Image = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
Image2 = np.array(Image, copy=True)

white_px = np.asarray([255, 255, 255])
black_px = np.asarray([0  , 0  , 0  ])

(row, col, _) = Image.shape
i=0
for r in range(row):
	for c in range(col):
		i=0
		if (Image[r][c][0]>=162):
			i=i+1
		if (Image[r][c][1]>=162):
			i=i+1
		if (Image[r][c][2]>=162):
			i=i+1
		if(i>=2):
			Image2[r][c] = Image[r][c]
		else:
			Image2[r][c] = black_px
imsave(out_path, Image2)