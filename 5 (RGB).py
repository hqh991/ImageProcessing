import cv2
from PIL import Image
import numpy as np

import matplotlib.pyplot as plt #thu vien ve bieu do




#tINH HISTOGRAM

def CalculateHistogram(imgPIL):
    histogramR = np.zeros(256)
    histogramG = np.zeros(256)
    histogramB = np.zeros(256)
    
#DUNG MANG 2 CHIEU CHUA TT HISTOGRAM CAC KENH  R,G,B
# Each pixel has value from 0-255 -> have to define an array of 256 values

# Image size
    width = imgPIL.size[0]
    height = imgPIL.size[1]
    
    for x in range(width):
        for y in range(height):
            # Get the gray value at (x,y)
            gR, gG, gB = imgPIL.getpixel((x, y))
            
            
            # The output gray value calculated is the "gray" element in the histogram defined before
            # Increase the count of "gray" element to 1
            
            histogramR[gR] += 1
            histogramG[gG] += 1
            histogramB[gB] += 1
            
    return histogramR,histogramG,histogramB


# Draw histogram using matplotlib library

def DrawHistogram(histogramR,histogramG,histogramB):
    width = 5
    height = 4
    plt.figure("RGB Image Histogram", figsize=(width, height), dpi=100)
    X_axis = np.zeros(256)
    X_axis = np.linspace(0, 256, 256)
     
    
    plt.plot(X_axis, histogramR, color= 'red')
    plt.plot(X_axis, histogramG, color = 'green')
    plt.plot(X_axis, histogramB, color= 'blue')
    
    plt.title("Histogram")
    plt.xlabel("Value")
    plt.ylabel("Points that have the same gray value")
    
    plt.show()

filehinh = r'LENA.jpg'                         #KHAI BAO DUONG DAN 

img = cv2.imread(filehinh, cv2.IMREAD_COLOR)  # DOC ANH MAU BANG TV OPENCV

imgPIL = Image.open(filehinh)   #DOC ANH MAU BANG TV PIL, ANH PIL DUNG THUC HIEN  CAC TAC VU XU LI VA TINH TOAN THAY OPENCV

histogramR,histogramG,histogramB = CalculateHistogram(imgPIL)


cv2.imshow('ANH GOC',img)

DrawHistogram(histogramR,histogramG,histogramB)


cv2.waitKey(0)

cv2.destroyAllWindows()
