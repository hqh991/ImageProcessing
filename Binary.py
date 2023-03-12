import cv2
from PIL import Image
import numpy as np


filehinh = r'LENA.jpg'
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)
imgPIL = Image.open(filehinh)



binary = Image.new(imgPIL.mode, imgPIL.size)

nguong = 130  #set gia tri nguong
 
width   = binary.size[0]
height = binary.size[1]

for i in range(width):
    for j in range(height):
        R,G,B = imgPIL.getpixel((i,j))
        gray = np.uint8((R+G+B)/3)
        
        
        if (gray<nguong ):
           binary.putpixel((i,j),(0,0,0))
        else:
            binary.putpixel((i,j),(255,255,255))
    
        
        
    
        
        
anhmucxam = np.array(binary)
cv2.imshow('ANH GOC',img)
cv2.imshow('ANH BINARY',anhmucxam)


cv2.waitKey(0)
cv2.destroyAllWindows()
