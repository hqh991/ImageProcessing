import cv2
from PIL import Image
import numpy as np

# Khai báo đường dẫn file hình
filehinh = r'Lena.jpg'

# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)

# Đọc ảnh màu dùng thư viện PIL. Ảnh PIL này chúng ta sẽ dùng
# để thực hiện các tác vụ xử lý & tính toán thay vì dùng OpenCV
imgPIL = Image.open(filehinh)

# Tạo một ảnh có cùng kích thước và cùng mode với ảnh PIL 
# Ảnh này dùng để chứa kết quả chuyển đổi RGB sang Grayscale
KX = Image.new(imgPIL.mode,imgPIL.size)
KY = Image.new(imgPIL.mode,imgPIL.size)
KZ = Image.new(imgPIL.mode,imgPIL.size)
XYZimg = Image.new(imgPIL.mode,imgPIL.size)

# Lấy kích thước ảnh
width = imgPIL.size[0]
height = imgPIL.size[1]

# Mỗi ảnh là một ma trận 2 chiều nên sẽ dùng 2 vòng for để 
# đọc hết các điểm ảnh (pixel) có trong ảnh
for x in range(width):
    for y in range(height):
        # Lấy giá trị điểm ảnh tại vị trí (x, y)
        R,G,B = imgPIL.getpixel((x,y))
        # Sử dụng các công thức tính giá trị X,Y,Z
        X = np.uint8(0.4124564*R + 0.3575761*G + 0.1804375*B)
        Y = np.uint8(0.2126729*R + 0.7151522*G + 0.0721750*B)
        Z = np.uint8(0.0193339*R + 0.1191920*G + 0.9503041*B)

        # Gắn giá trị X,Y,Z vừa tính cho hình
        KX.putpixel((x,y),(X,X,X))
        KY.putpixel((x,y),(Y,Y,Y))
        KZ.putpixel((x,y),(Z,Z,Z))
        XYZimg.putpixel((x,y),(Z,Y,X))

# Chuyển ảnh từ PIL sang OpenCV để hiển thị
anhX = np.array(KX)
anhY = np.array(KY)
anhZ = np.array(KZ)
anhXYZ = np.array(XYZimg)

# Hiển thị hình dùng thư viện OpenCV
cv2.imshow('Anh mau RGB goc',img)
cv2.imshow('Kenh X',anhX)
cv2.imshow('Kenh Y',anhY)
cv2.imshow('Kenh Z',anhZ)
cv2.imshow('Kenh XYZ',anhXYZ)

# Bấm phím bất kỳ để đóng cửa sổ hiển thị ảnh
cv2.waitKey(0)

# Giải phóng bộ nhớ đã cấp phát cho các cửa sổ
cv2.destroyAllWindows()



