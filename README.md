There are 2 questions.
question 3rd has 3 files.
--> 1st is opencv.py, it contains the live webcam code.
--> 2nd part is publisher_mqtt.py. It contains the combined publisher and mqtt code which prints an alert message when message is printed.
--> 3rd part is subscriber.py , with lelp of mqtt broker, it receives alert messages on the topic which it subscribed.

questtion 2 has 2 parts: 
It is a multi chat system, which uses multi threading.
the server.py has rec_connection, which connects the clients, then there is a handle clients and brodcast message, which broadcasts all the messages.
client.py receives messages from others and can send messsaages.
