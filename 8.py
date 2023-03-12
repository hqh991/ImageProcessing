import cv2
from PIL import Image
import numpy as np
import math

# Khai báo file hình
filehinh = r'Lena.jpg'
# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)

# Đọc ảnh bằng PIL để thao tác tính toán
imgPIL = Image.open(filehinh)

# Tạo ảnh để chứa kết quả có cùng Mode và kích thước với ảnh imgPIL
Hue = Image.new(imgPIL.mode, imgPIL.size)
Saturation = Image.new(imgPIL.mode, imgPIL.size)
Value = Image.new(imgPIL.mode, imgPIL.size)
HSVImg = Image.new(imgPIL.mode, imgPIL.size)

# Lấy kích thước ảnh
width = imgPIL.size[0]
height = imgPIL.size[1]

for x in range(width):
    for y in range(height):
        # Lấy giá trị điểm ảnh tại vị trí (x, y)
        R, G, B = imgPIL.getpixel((x, y))
        
        # t1 là phần tử số của công thức 
        t1 = np.uint8(((R - G) + (R - B)) / 2)

        # t2 là phần mẫu số của công thức tính góc theta 
        t2 = np.uint8((R - G) * (R - G) + np.sqrt((R - B) * (G - B)))

        # Kết quả trả về là radian
        theta = np.uint8(np.radians(t1 / t2))
        
        H = 0

        # Nếu mà Blue <= Green thì Hue = theta 
        if (B <= G):
            H = np.uint8((theta)* 180/np.pi)
        else: # Ngươc lại thì Hue tính theo công thức H = 360 - theta  
            H = np.uint8((2*np.pi - theta)* 180/np.pi) # Do theta là radian tính ở trên nên thay vì dùng 360 thì dùng PI
        # Chuyển đổi giá trị H từ radian sang degree 
        
        # Công thức tính giá trị kênh Saturation
        # Do giá trị tính ra của S sẽ nằm trong khoảng [0, 1], cần phải chuyển S sang khoảng giá trị [0,255]
        # Công thức dưới giúp chuyển đổi từ rank [0,1] sang rank [0,255]
        S = np.uint8((1 - 3 * min(R, G, B) / (R + G + B))*255)
            
        # Công thức tính giá trị kênh Itensity
        V = np.uint8(max(R, G, B))

        # Set giá trị pixel đọc được cho các hình chứa các kênh màu tương ứng 
        Hue.putpixel((x,y),(H, H, H))
        Saturation.putpixel((x,y),(S, S, S))
        Value.putpixel((x,y),(V, V, V))
        HSVImg.putpixel((x,y),(V, S, H))

# Chuyển ảnh từ PIL sang OpenCV
anhH = np.array(Hue)
anhS = np.array(Saturation)
anhV = np.array(Value)
anhHSV = np.array(HSVImg)

# Hiển thị ảnh bằng OpenCV
cv2.imshow('Kenh Hue', anhH)
cv2.imshow('Kenh Saturation', anhS)
cv2.imshow('Kenh Value', anhV)
cv2.imshow('Kenh HSV', anhHSV)

# Bấm phím bất kỳ để đóng cửa sổ hiển thị 
cv2.waitKey(0)
# Giải phóng bộ nhớ cho cửa sổ hiển thị 
cv2.destroyAllWindows()