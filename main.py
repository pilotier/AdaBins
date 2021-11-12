#import utils

#utils.generate_video_from_imgs("sim", ".jpeg")
#utils.generate_video_from_imgs("D:/8th_Avenue_Stereo/RGB/R", ".jpeg")

import cv2
import numpy as np
img = cv2.imread("C:/Users/Ibrahim/Projects/AdaBins/sim2/196.png")
img2 = cv2.imread("C:/Users/Ibrahim/Projects/AdaBins/sim2/000196.png")

m = np.max(img[:,:,2])

img2[:,:,0] = m-img[:,:,2]
img2[:,:,1] = m-img[:,:,2]
img2[:,:,2] = m-img[:,:,2]

cv2.imwrite("C:/Users/Ibrahim/Projects/AdaBins/sim2/X196.png", img2)
