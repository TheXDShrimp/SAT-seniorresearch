import olympe
import os
import time
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveBy

DRONE_IP = os.environ.get("DRONE_IP", "192.168.42.1")


def test_takeoff():
    drone = olympe.Drone(DRONE_IP)
    drone.connect()
    assert drone(TakeOff()).wait().success()
    time.sleep(10)
    assert drone(Landing()).wait().success()
    drone.disconnect()
    
def move_forward():
    distance = 5
    duration = 2

    drone = olympe.Drone(DRONE_IP)
    drone.connect()
    # Move the drone forward
    assert drone(TakeOff()).wait().success()
    assert drone(moveBy(distance, 0, 0, 0)).wait().success()
    time.sleep(duration)
    assert drone(Landing()).wait().success()
    drone.disconnect()



if __name__ == "__main__":
    test_takeoff()

    move_forward()
