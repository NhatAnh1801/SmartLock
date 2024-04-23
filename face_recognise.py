# # import the required libraries
# import cv2
# import pickle
#
# video = cv2.VideoCapture(0)
# cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#
# # Loaading the face recogniser and the trained data into the program
# recognise = cv2.face.LBPHFaceRecognizer_create()
# recognise.read("trainner.yml")
#
# labels = {} # dictionary
# # Opening labels.pickle file and creating a dictionary containing the label ID
# # and the name
# with open("labels.pickle", 'rb') as f:##
#     og_label = pickle.load(f)##
#     labels = {v:k for k,v in og_label.items()}##
#     print(labels)
#
# while True:
#     check,frame = video.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     face = cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
#     #print(face)
#
#     for x,y,w,h in face:
#         face_save = gray[y:y+h, x:x+w]
#
#         # Predicting the face identified
#         ID, conf = recognise.predict(face_save)
#         #print(ID,conf)
#         if conf >= 20 and conf <= 115:
#             #HERE
#             print(ID)
#             print(labels[ID])
#             cv2.putText(frame,labels[ID],(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX ,1, (18,5,255), 2, cv2.LINE_AA )
#         frame = cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,255),4)
#
#     cv2.imshow("Video", frame)
#     key = cv2.waitKey(1)
#     if(key == ord('q')):
#         break
#
# video.release()
# cv2.destroyAllWindows()

# import the required libraries
import cv2
import pickle
import serial
import time

#port = serial.Serial('COM7', 9600)
PIN_Code = '1234'
#time.sleep(2)
def unlock_with_pin():
    user_pin = input("Enter the PIN code to unlock: ")
    if user_pin == PIN_Code:
        print("Unlocking with PIN...")
        #port.write(b'1')  # Simulate unlocking action
        time.sleep(1)  # Delay to simulate the unlock process
        return True
        exit(0)
    else:
        print("Incorrect PIN. Access Denied.")
        return False

while True: #port.isOpen()
    video = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Loaading the face recogniser and the trained data into the program
    recognise = cv2.face.LBPHFaceRecognizer_create()
    recognise.read("trainner.yml")

    labels = {} # dictionary
    # Opening labels.pickle file and creating a dictionary containing the label ID
    # and the name
    with open("labels.pickle", 'rb') as f:##
        og_label = pickle.load(f)##
        labels = {v:k for k,v in og_label.items()}##
        print(labels)

    while True:
        unlock_with_pin()
        check,frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face = cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
        #print(face)

        for x,y,w,h in face:
            face_save = gray[y:y+h, x:x+w]

            # Predicting the face identified
            ID, conf = recognise.predict(face_save)
            #print(ID,conf)
            if conf >= 20 and conf <= 115:
                print(ID)
                print(labels[ID])
                cv2.putText(frame,labels[ID],(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX ,1, (18,5,255), 2, cv2.LINE_AA )
                #port.write(b'1')
                time.sleep(1)
                frame = cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,255),4)
            #else:
                #port.write(b'0')

        cv2.imshow("Video", frame)
        key = cv2.waitKey(1)
        if(key == ord('q')):
            break

video.release()
cv2.destroyAllWindows()
