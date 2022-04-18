import cv2

def decodeAndCaptureQR():

    img = cv2.imread("qrCode.png")

    while True:

        codeStr = None

        detect = cv2.QRCodeDetector()

        val, pts, _ = detect.detectAndDecode(img)

        if pts is None:
            return codeStr
        else:
            return val 