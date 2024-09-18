#Importing QR Code Module(to Create) and Image Creating Module[PILLOW] (to Open)
import qrcode
from PIL import Image

#Gathering Text from user to convert as QR Code Image File
value = str(input("Enter String or Link: "))

#Creates the QR Code
qrImg=qrcode.make(value)

#Saves as "qr-img.jpg" file, whrere near this file
qrImg.save("qr-img.jpg")
print("QR Code saved as 'qr-img.jpg'")

#Opens the Created Image Automatically
img=Image.open("qr-img.jpg")
img.show()
