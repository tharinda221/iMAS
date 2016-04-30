import numpy as np, cv2
import socket

# Binaryzacja obrazu z zadanym progiem
def binarize(img, thresh = 30):
    retval, imgbin = cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)
    return imgbin

# Zmiana na skale szarosci
def grayish(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Diff obrazow
def diffImages(img0,img1,img2):
    diff1 = cv2.absdiff(img2, img1)
    diff2 = cv2.absdiff(img1, img0)
    return cv2.bitwise_and(diff1, diff2)

# Polaczenie 2 obrazow
def mergeImages(img0, img1):
    merged = cv2.addWeighted(img0,0.5,img1,0.6,0.0)
    return merged

# Porownanie do czarnego
def isMovement(img, threshold = 100):
    black = np.zeros((img.shape), np.uint8)
    out = cv2.compare(img,black,cv2.CMP_NE)
    diff = cv2.countNonZero(img)

    if diff < threshold:
        return False
    else:
        return True

# Wykrycie ruchu
def processImages(t0, t1, t2):
    diff = diffImages(t0,t1,t2)
    bin = binarize(diff)
    merged = mergeImages(t1,bin)
    return (isMovement(bin), merged)

# Wyslanie informacji o ruchu
def sendMoveInformation(message, ip = "127.0.0.1", port = 28936):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message, (ip, port))