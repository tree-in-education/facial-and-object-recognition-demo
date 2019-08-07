import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")


while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 113:
        # ESC pressed
        print("q hit, closing camera...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = input('Enter your name : ')
        # User inputs name as string
        cv2.imwrite('/Users/thomasyoung/FacialRecognition/facialImages/' + str(img_name) + '.jpg', frame)
        # Saves picture to directory, named *whatever the user input*.jpg
        # Replace /Users/thomasyoung/FacialRecognition/facialImages/ with your own directory
        print(str(img_name) + " was entered into the database.")

cam.release()

cv2.destroyAllWindows()
#Closes program
