import cv2  
import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"
port = 1883
topic = "home/alert"

client = mqtt.Client(
    client_id="Publisher",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1 #type: ignore
)

client.connect(broker, port)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #type: ignore
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("couldn't access live webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    resized_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    gray_img = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

    if len(faces) > 0:
        msg = "A face is detected!!"
        client.publish(topic, msg)
        print(msg) 
    

    for x, y, w, h in faces:
        cv2.rectangle(frame, (2*x, 2*y), (x*2+w*2, y*2+h*2), (0, 255, 0), 3)

    cv2.imshow("live", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() 
cv2.destroyAllWindows() #release and destroy the windows
client.disconnect() # close the MQTT connection