from pyzbar.pyzbar import decode
import cv2

def decodeAndCaptureQR():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)

    while True:

        ret, frame = cap.read()

        for code in decode(frame):
            codeStr = str(code.data)

        cv2.imshow("Test Frame", frame)
        cv2.waitKey(1)

        if codeStr != "":

            cv2.destroyAllWindows()
            return codeStr