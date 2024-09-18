# Imports Camera Module(to use Camera and Detect QR Code) and Web Browser Module(to open Link Results)
import cv2, webbrowser

# Gathering Chances from User to get Real-Time Results and In-Directory Image's Results
choice = input("Do You want to use Camera?(Y/N)[Default=No]: ");

# Real-Time to gather QR Code
if choice in 'yY':

    # Creates Video Capturer and QR Code Detector objects
    captures = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    
    # Closes Camera when The Button "Q" is pressed
    print("Press the Button 'q' to EXIT",flush=True)
    while True:
        _, image = captures.read()
        data, _, _ = detector.detectAndDecode(image)
        if data:
            print(str(data),flush=True)
            break
        cv2.imshow("QR Code Scanner by Sudhanex", image)
        if cv2.waitKey(1) == ord('q'):
            break

    # Close Video Capturer and Exits all Camera Modules
    captures.release()
    cv2.destroyAllWindows()

# In-Directory Images to gather QR Code
else:

    # Gathering QR Code Image's Location
    image_path = input("Enter Location of the file: ")

    # Reads and Detects QR Code in Images from Camera Module
    image = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()

    # Decodes the QR Code as "data" variable
    data, _, _ = detector.detectAndDecode(image)

    # Shows the Gathered Data
    if data is not None:
        print(str(data),flush=True)
    else:
        print("No QR code detected in this image.")

#Checks if it is available link and Opens Web Browser using Web Browser Module
if 'http' not in str(data):
    print("Data in this QR Code is shown below\n"+str(data))
else:

    # Confirmation to open provided link
    confirm = input("Did you want Me to open that link which was shown above?(Default=No)[Y/N]: ")
    if confirm in 'yY':
        webbrowser.open(str(data))

# Exits automatically, After Completion
exit(0)
