import qrcode
from PIL import Image
value=str(input("Enter String or Link: "))
qrImg=qrcode.make(value)
qrImg.save("qr-img.jpg")
print("QR Code saved as 'qr-img.jpg'")
img=Image.open("qr-img.jpg")
img.show()

