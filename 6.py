import cv2                       #thu vien open cv

import numpy as np                  # thu vien toan hoc

from PIL  import Image
# doc anh mau dung thu vien open cv

img = cv2.imread('Lena.jpg', cv2.IMREAD_COLOR)
imgPIL = Image.open('Lena.jpg')

# tạo ảnh  có cùng mode và kich thước 

C=Image.new(imgPIL.mode,imgPIL.size)

M =Image.new(imgPIL.mode,imgPIL.size)
Y =Image.new(imgPIL.mode,imgPIL.size)
K=Image.new(imgPIL.mode,imgPIL.size)



#lay kich thuoc
w = imgPIL.size[0]
h = imgPIL.size[1]
# moi anh la 1 ma tran 2 chieu , dung 2 vong lap for de doc het các pixel
for x in range(w):
    for y in range(h):
        R,G,B = imgPIL.getpixel((x,y))
        #tiep theo, tron cac kenh mau cho ra CMYK
        C.putpixel((x,y),(B,G,0  ))   #xanh duong = G+B, R= 0
        M.putpixel((x,y),(B,0,R))    # mau tim
        Y.putpixel((x,y),(0,G,R )) # mau vang
        
        
        # mau den= min(R,G,B)
        Min= min(R,G,B)
        black = Min
        K.putpixel((x,y),(black,black,black))
 

ANHC = np.array(C)
ANHM= np.array(M)
ANHY= np.array(Y)
ANHK= np.array(K)

#HIEN THI ANH DUNG THU VIEN OPEN CV
cv2.imshow("ANH RGB GOC",img)

cv2.imshow("KENH CAYN",ANHC)

cv2.imshow("KENH MAGETAN",ANHM)
cv2.imshow("KENH YELLOW",ANHY)
cv2.imshow("KENH K (BLACK )",ANHK)

#DUNG PHIM BAT KY DONG CUA SO HIEN THI HINH
cv2.waitKey(0)
#GiAI PHONG BO NHO DA CAP PHAT CHO CCAC CUA SO
cv2.destroyAllWindows()