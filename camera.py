import cv2


def generate():

    a = cv2.VideoCapture(0)

    while True:
        ok, frame = a.read()
        if ok:
            frame = cv2.flip(frame, 1)
            x1 = int(0.5 * frame.shape[1])
            y1 = 0
            x2 = frame.shape[1]
            y2 = int(0.6 * frame.shape[0])
            # Drawing the ROI
            # The increment/decrement by 1 is to compensate for the bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 1)
            # Extracting the ROI
            roi = frame[y1:y2, x1:x2]
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 2)
            th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
            ret, test_image = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            # test_image = cv2.resize(test_image, (300,300))
            cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.resizeWindow('frame', frame.shape[1], frame.shape[0])
            cv2.imshow("frame", frame)

            cv2.namedWindow('test', cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('test', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.resizeWindow('test', roi.shape[1], roi.shape[0])
            cv2.imshow("test", test_image)
            cv2.moveWindow('test', roi.shape[1], 0)

            interrupt = cv2.waitKey(10)
            if interrupt & 0xFF == 27:  # esc key
                break

    a.release()
    cv2.destroyAllWindows()

generate()