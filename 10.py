import cv2
from PIL import Image
import numpy as np

# Khai báo đường dẫn file hình
filehinh = r'Lena.jpg'

# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)

# Đọc ảnh bằng PIL để thao tác tính toán
imgPIL = Image.open(filehinh)

# Tạo ảnh để chứa kết quả có cùng Mode và kích thước với ảnh imgPIL
YImg = Image.new(imgPIL.mode, imgPIL.size)
CrImg = Image.new(imgPIL.mode, imgPIL.size)
CbImg = Image.new(imgPIL.mode, imgPIL.size)
YCrCbImg = Image.new(imgPIL.mode, imgPIL.size)

# Lấy kích thước ảnh
width = imgPIL.size[0]
height = imgPIL.size[1]

# Đọc các điểm ảnh (pixel) có trong ảnh
for x in range(width):
    for y in range(height):
        # Lấy giá trị điểm ảnh tại vị trí (x, y)
        R, G, B = imgPIL.getpixel((x,y))

        # Sử dụng các công thức tính giá trị Y, Cr, Cb
        Y = np.uint8(16 + 65.738 * R / 256 + 129.057 * G / 256 + 25.064 * B / 256)
        Cr = np.uint8(128 - 37.945 * R / 256 - 74.494 * G / 256 + 112.439 * B / 256)
        Cb = np.uint8(128 + 112.439 * R / 256 - 94.154 * G / 256 - 18.285 * B / 256)

        # Gắn giá trị Y, Cr, Cbvừa tính cho hình
        YImg.putpixel((x, y), (Y, Y, Y))
        CrImg.putpixel((x, y), (Cr, Cr, Cr))
        CbImg.putpixel((x, y), (Cb, Cb, Cb))
        YCrCbImg.putpixel((x, y), (Cb, Cr, Y))

# Chuyển ảnh từ PIL sang OpenCV để hiển thị
anhY = np.array(YImg)
anhCr = np.array(CrImg)
anhCb = np.array(CbImg)
anhYCrCb = np.array(YCrCbImg)

# Hiển thị hình dùng thư viện OpenCV
cv2.imshow('Kenh Y', anhY)
cv2.imshow('Kenh Cr', anhCr)
cv2.imshow('Kenh Cb', anhCb)
cv2.imshow('Kenh YCrCb', anhYCrCb)

# Bấm phím bất kỳ để đóng cửa sổ hiển thị ảnh
cv2.waitKey(0)
# Giải phóng bộ nhớ đã cấp phát cho các cửa sổ
cv2.destroyAllWindows()