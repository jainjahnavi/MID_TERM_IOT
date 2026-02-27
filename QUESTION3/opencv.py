import cv2  
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #type: ignore
cap= cv2.VideoCapture(0)

if not cap.isOpened():
    print("couldn't access live webcam")
    exit()

 #infinite loop
while True:
    ret,frame=cap.read()

    if not ret:
        print("can't receive frame!! exiting...")
        break
    resized_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    gray_img=cv2.cvtColor(resized_frame,cv2.COLOR_BGR2GRAY)

    faces= face_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=2) #get the coordinate of faces

    for x,y,w,h in faces:
        cv2.rectangle(frame,(2*x,2*y),(x*2+w*2,y*2+h*2),(0,255,0),3)
    cv2.imshow("live",frame)

    if cv2.waitKey(1) & 0xFF== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()