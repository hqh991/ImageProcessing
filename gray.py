import cv2
from PIL import Image
import numpy as np


filehinh = r'LENA.jpg'
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)
imgPIL = Image.open(filehinh)



average = Image.new(imgPIL.mode, imgPIL.size)

width   = average.size[0]
height = average.size[1]

for i in range(width):
    for j in range(height):
        R,G,B = imgPIL.getpixel((i,j))
        gray = np.uint8((R+G+B)/3)
        
        average.putpixel((i,j),(gray,gray,gray))
        
        
anhmucxam = np.array(average)
cv2.imshow('ANH GOC',img)
cv2.imshow('ANH MUC XAM AVERAGE',anhmucxam)


cv2.waitKey(0)
cv2.destroyAllWindows()
