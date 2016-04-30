import numpy as np, cv2
from functions import processImages, sendMoveInformation, grayish
from libs.camera import Camera


# Pobieramy kamere
# cam = cv2.VideoCapture(0)

class MotionDetector(object):
    def test(self):
        while True:
            move = True
            if move:
                yield "return Test Test"

    def motion_detector(self, cam):
        # winName = "winName"
        # cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

        # Odczytujemy 3 obrazy
        t_minus = grayish(cam.read()[1])
        t = grayish(cam.read()[1])
        t_plus = grayish(cam.read()[1])

        while True:
            # Wyswietlamy przetworzony obraz
            (move, img) = processImages(t_minus, t, t_plus)
            # cv2.imshow(winName, img)

            # Wysylamy informacje o wykrytym ruchu
            if move:
                # sendMoveInformation("Wykryto ruch!")
                print "move"
            # Odczytujemy kolejny obraz
            t_minus = t
            t = t_plus
            t_plus = grayish(cam.read()[1])
            frame = self.movingImageGenarating()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            # Esc = wyjscie
            # key = cv2.waitKey(10)
            # if key == 27:
            #     cv2.destroyWindow(winName)
            #     break

    # motion_detector(Camera().getCam())

    def movingImageGenarating(self):
        img = np.zeros((100, 150, 3), np.uint8)

        # Write some Text
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Moving!', (10, 50), font, 1, (255, 255, 255), 2)
        ret2, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tostring()
