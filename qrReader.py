import cv2, webbrowser
choice = input("Do You want to use Camera?(Y/N)[Default=No]: ");
if choice in 'yY':
    captures = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
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
    captures.release()
    cv2.destroyAllWindows()
else:
    image_path = input("Enter Location of the file: ")
    image = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(image)
    if data is not None:
        print(str(data),flush=True)
    else:
        print("No QR code detected in the image.")
if 'http' not in str(data):
    print("Data in this QR Code is shown below\n"+str(data))
else:
    confirm = input("Did you want Me to open that link which was shown above?(Default=No)[Y/N]: ")
    if confirm in 'yY':
        webbrowser.open(str(data))
exit(0)
