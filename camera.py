from pyzbar.pyzbar import decode
import cv2

def decodeAndCaptureQR():

    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)

    while True:

        codeStr = None

        ret, frame = cap.read()

        for code in decode(frame):
            codeStr = str(code.data.decode())

        if codeStr is None:
            cv2.imshow("Camera Capture", frame)
            cv2.waitKey(1)
        else:
            cv2.destroyAllWindows()
            return codeStr