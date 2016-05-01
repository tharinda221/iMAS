import time

from motion import *


class application(object):
    def motionDetector(self, cam):
        # Setup cam capture
        # cam = create_capture(video_src)

        # Setup motion detection
        # md_average needs to be setup with the same type of picture as used in motion detection
        ret, img = cam.read()
        img, gray = preProcess(img)
        flag, gray = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)  # cv2.THRESH_BINARY = 0

        # Motion detection variables
        md_average = np.float32(gray)
        md_result = np.float32(gray)
        md_weight = 0.9

        # Setup default cam window
        # cv2.namedWindow(highgui_name)
        # cv2.createTrackbar("md_weight", highgui_name, int(md_weight*100), 100, md_weight_change)


        # Read and preprocess image
        success, orig_img = cam.read()
        (orig_img, gray) = preProcess(orig_img)

        # Get the new trackbar value
        # md_weight = cv2.getTrackbarPos("md_weight", highgui_name) * 0.01
        #
        # if not success:
        #     print "Cam read error. WTF mate"
        #     break

        # Detect the faces
        faces = detectFaces(gray)

        # Detect motion
        contours = detectMotion(gray, md_average, md_weight)

        # Add all face points aquired
        for (x, y, width, height) in faces:
            cv2.rectangle(orig_img, (x, y), (x + width, y + height), (255, 0, 0), 2)

        # Apply the contours
        for cnt in contours:
            color = np.random.randint(0, 255, (3)).tolist()  # Select a random color. Hippiestyle!
            cv2.drawContours(orig_img, [cnt], 0, color, 2)

        # Add some text
        text_color = (255, 0, 0)  # color as (B,G,R)
        # cv2.putText(orig_img, "Hello world", (45, 20), cv2.FONT_HERSHEY_PLAIN, 1, text_color, thickness=1, lineType=cv2.CV_AA)

        # cv2.imshow(highgui_name, orig_img)

        # if cv2.waitKey(20) == 27:  # Esc pressed
        #     break

        # End
        # cv2.destroyAllWindows()
        return orig_img

    # def FaceDetector(self, cam):
    #     cascPath = "haarcascade_frontalface_default.xml"
    #     faceCascade = cv2.CascadeClassifier(cascPath)
    #     ret, frame = cam.read()
    #
    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #
    #     faces = faceCascade.detectMultiScale(
    #             gray,
    #             scaleFactor=1.1,
    #             minNeighbors=5,
    #             minSize=(30, 30),
    #             flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    #     )
    #
    #     # Draw a rectangle around the faces
    #     text_color = (255, 0, 0)  # color as (B,G,R)
    #     for (x, y, w, h) in faces:
    #         cv2.rectangle(frame, (x, y), (x + w, y + h), text_color, 3)
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     #cv2.putText(frame,str(len(faces)),(10,500), font, 1,(255,255,255),2)
    #
    #     #cv2.putText(frame, str(len(faces)), (45, 20), cv2.FONT_HERSHEY_PLAIN, 1, text_color, thickness=1, lineType=cv2.CV_AA)
    #     return frame

    def EdgeDetector(self, cam):
        ret, frame = cam.read()
        edges = cv2.Canny(np.asarray(frame[:,:]),100,200)
        #cv2.imshow("preview", edges)
        rval, frame = cam.read()
        return edges