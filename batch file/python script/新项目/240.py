from PIL import Image
import PIL.ImageOps	
import numpy as np
from skimage.io import imsave
import cv2


in_path  = 'sadx.jpg'
out_path = 'new.jpg'


Image = cv2.imread(in_path)
Image = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
Image2 = np.array(Image, copy=True)

white_px = np.asarray([255, 255, 255])
black_px = np.asarray([0  , 0  , 0  ])

(row, col, _) = Image.shape
i=0
jump=0
for r in range(row):
	for c in range(col):
		i=0
		if (Image[r][c][0]>=240):
			i=i+1
		if (Image[r][c][1]>=240):
			i=i+1
		if (Image[r][c][2]>=240):
			i=i+1
		if(jump>0):
			jump=jump-1			
		if(i>=2 or jump >0):
			if i>=2:
				jump=15
			Image2[r][c] = Image[r][c]
		else:
			Image2[r][c] = black_px
imsave(out_path, Image2)