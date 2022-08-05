# Python 3.8
# file: cam.py
# requirements: apt-package (python3-opencv) or pip-package (opencv-python). Warn: conflict.
# author: steve.jeong

import cv2

def main():
  cam = cv2.VideoCapture(0)
  while True:
    check,frame = cam.read()
    cv2.imshow("Live",frame)
    if (cv2.waitKey(1) == 'q'):
        break
    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
  main()

# vim: ft=python ts=2 sw=2 sts=2 et
