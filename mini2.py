import cv2                       #thu vien open cv

import numpy as np                  # thu vien toan hoc
# doc anh mau dung thu vien open cv

img = cv2.imread('Lena.jpg', cv2.IMREAD_ANYCOLOR)
#LAY KICH THUOC ANH
height = len(img[0])
width = len(img[1])
#khai bao 3 bien de chua 3 hinh kenh RGB
red = np.zeros((width, height, 3),np.uint8) # so 3 la 3 kenh RGB , moi kenh 8 bit
green = np.zeros((width, height, 3),np.uint8)
blue = np.zeros((width, height, 3),np.uint8)
# ban dau set zero cho tta ca cac diem anh co trong ca 3 kenh moi hih

red[:]=[0,0,0]

green[:]=[0,0,0]

blue[:]=[0,0,0]

#moi hinh LA 1 MA TRAN 2 CHIEU, DUNG VONG FOR DOC HET TAT CA CAC DIEM ANH(PIXEL ) CO TRONG HINH
for  x in range(width):
    for y in range(height):
        R = img[x,y,2]                # lay gia tri diem anh tai vi tri x,y
        G = img[x,y,1]
        B = img[x,y,0]
        # thiet lap mau cho cac kenh
        red[x, y, 2] = R
        green[x, y, 1] = G
        blue[x, y, 0] = B

# HIEN THI HINH DUNG OPENCV
cv2.imshow('HINH GOC',img)
cv2.imshow('Red',red)
cv2.imshow('green',green)
cv2.imshow('blue',blue)
#DUNG PHIM BAT KY DONG CUA SO HIEN THI HINH
cv2.waitKey(0)
#GiAI PHONG BO NHO DA CAP PHAT CHO CCAC CUA SO
cv2.destroyAllWindows()