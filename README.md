💻# Covengers_WCE

WCE Hackathon 2022

Problem Statement ID: PS01

Problem Statement: 🚦Traffic Management in WCE using Video Surveillance 📹

Track: Expert Track



📍Project Name: Traffic Management in WCE using Video Surveillance


📝**Solution:**
A proposed system will be able to detect a vehicle (two wheeler, four wheeler) which is out of the area of parking through video
surveillance. If any of vehicle is seems to have out of the parking slot, then it will capture a number plate. Here, using number capturing system the extracted number from the number plate will be match with the available database. That database will have the details of the vehicle owner, for that owner have to registered themselves to the web portal provided by college itself with the specific details (Name, Mobile No., Vehicle no. plate,). After the verification of the number plate the SMS will sent to the owner of the vehicle (which is out of parking slot). If that particular vehicle owner is not registered to the web portal, then it will report the location to the authority. And authority will take the next step. 

👉For the suspected vehicle detection(which is out of the parking slot) machine learning model will be used.


👉Number plate scanning will be done using OCR(Optical Character Recognition) which scan the image and convert it into text.


👉Reporting a location to the authority using machine learning algorithm.




📍Technology Stack:

 Frontend- HTML, CSS, JavaScript.
 
 
 Backend- Python.
 
 
 Libraries- open-cv, cvzone, EasyOCR, Pickle, matplotlib, numpy
 
 Algorithm- Yolo, CNN.
 
 
📍**Innovativeness:**

👉Automatic Detection and Scanning number plate of vehicle
violating parking rules.

👉Sending text SMS regarding violation will be send to owner of
vehicle


🛑**Show Stoppers:**

👉Damaged and dirty Plate

👉Plate distance from camera: Distance between plate and camera also affects system performance

👉Area ratio: The camera should be mounted in such a way that its maximum focus should be on the Number Plate region

👉Weather Conditions: Image captured by the camera can be in different lighting conditions, in different day time such as in sunlight,
evening time, night time, shadow, glare, and cloudy condition.

