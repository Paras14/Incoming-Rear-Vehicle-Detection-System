# Incoming-Rear-Vehicle-Detection-System
Alerts Novice driver, and reports the side of Incoming vehicle from rear. (approaching on Road)
Uses Yolov3 object detection to detect Vehicles.
Image feed is taken from a Smartphone(IP Webcam) placed at the rear of the car behind the rear seat.
Draws an outlining box on vehicle detected, and reports side from which it is approaching on the Display.

"yolov3-tiny.weights" file which contains the weights for the Neural network can't be upload due to its size.

Also "[Not Complete]Alerts while taking turn, accelerometer smartphone.py" is not completed yet,
when done it is supposed to alert driver not to turn Left or Right if a vehicle is incoming from that side.
This is achieved with the help of an accelometer, that is built into the Smartphone,
sensor data is sent through an android app (like "PhonePi Sensor Streamer").
Only thing left to do is to tune the data coming from smartphone's accelormeter in such way that False positives are minimized,
and then it could be integrated with the main script ("Vehicle Detection LEFT or RIGHT.py")
