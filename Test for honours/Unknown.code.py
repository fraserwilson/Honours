#else:
                #img_checker = True
                #while img_checker:
                    #img_counter = 1

                     # to detect faces in video
                    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    #faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                    #for (x,y,w,h) in faces:
                        #cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                        #roi_gray = gray[y:y+h, x:x+w]
                        #roi_color = frame[y:y+h, x:x+w]

                    #x = 0
                    #y = 20
                    #text_color = (0,255,0)

                    #cv2.imwrite('C:\\Users\\Fraser Wilson\\Desktop\\Test for honours\\opencv'+str(img_counter)+'.jpg',frame)
                    #img_counter += img_counter
                    #new_encoding  = True
                    #while new_encoding:
                        #new_face_counter = 1
                        #new_face_image = face_recognition.load_image_file("C:\\Users\\Fraser Wilson\\Desktop\\Test for honours\\opencv"+str(new_face_counter)+".jpg")
                        #new_face_encoding = face_recognition.face_encodings(new_face_image)[0]
                        #known_face_encodings.append(new_face_encoding)
                        #known_face_names.append("New_Customer")
                        #new_face_counter += new_face_counter
                        #new_encoding = False

                    #img_checker = False