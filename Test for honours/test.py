import face_recognition
import cv2
import numpy as np
import os

video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('C:\\Users\\Fraser Wilson\\Desktop\\Test for honours\\haarcascade_frontalface_default.xml')

#m_image = face_recognition.load_image_file("C:\\Users\\Fraser Wilson\\Desktop\\Test for honours\\M.jpg")
#m_face_encoding = face_recognition.face_encodings(m_image)[0]

#mo_image = face_recognition.load_image_file("C:\\Users\\Fraser Wilson\\Desktop\\Test for honours\\MO.jpg")
#mo_face_encoding = face_recognition.face_encodings(mo_image)[0]

known_face_encodings = [
    #m_face_encoding,
    #mo_face_encoding
]

known_face_names = [
    #"Fraser",
    #"Mom"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
customer_queue = []

while True:
    
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                customer_queue.append(name)
                temp = []
                for item in customer_queue:
                    if item not in temp:
                        temp.append(item)
                print(temp)
            else:
                img_checker = True
                while img_checker:
                    img_counter = 1

                    
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                    for (x,y,w,h) in faces:
                        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                        roi_gray = gray[y:y+h, x:x+w]
                        roi_color = frame[y:y+h, x:x+w]

                    x = 0
                    y = 20
                    text_color = (0,255,0)
                    image_exists = os.path.isfile('C:\\Users\\Fraser Wilson\\Desktop\\Test for honours\\opencv'+str(img_counter)+'.jpg')
                    if image_exists:
                        new_face_counter = 1
                        new_face_image = face_recognition.load_image_file("C:\\Users\\Fraser Wilson\\Desktop\\Test for honours\\opencv"+str(new_face_counter)+".jpg")
                        new_face_encoding = face_recognition.face_encodings(new_face_image)[0]
                        known_face_encodings.append(new_face_encoding)
                        known_face_names.append("New_Customer_"+str(new_face_counter))
                        new_face_counter += new_face_counter
                        print(known_face_names)
                    else:
                        cv2.imwrite('C:\\Users\\Fraser Wilson\\Desktop\\Test for honours\\opencv'+str(img_counter)+'.jpg',frame)
                        img_counter += img_counter
                        

                    img_checker = False

            face_names.append(name)

    process_this_frame = not process_this_frame
    
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()