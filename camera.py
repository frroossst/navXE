from base64 import decode
import cv2

def decodeAndCaptureQR():

    img = cv2.imread("qrCode.png")

    while True:

        codeStr = None

        detect = cv2.QRCodeDetector()

        val, pts, _ = detect.detectAndDecode(img)
        print(f"[LOG] val : {val} | pts : {pts}")
        print(f"[LOG] codeStr = {codeStr}")

        if pts is None:
            return codeStr
        else:
            return val 

print(decodeAndCaptureQR())