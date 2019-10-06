from firebase import firebase
import time
fire = firebase.FirebaseApplication('https://proj1-6f30a.firebaseio.com/',None)
data = fire.get("/macs", None)
print(data)
while True:
    real_data = data
    time.sleep(6)
    data = fire.get("/macs", None)
    if real_data != data:
        print(data)


