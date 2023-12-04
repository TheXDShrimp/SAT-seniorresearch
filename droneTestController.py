import olympe
import time
from olympe.messages.skyctrl.CoPiloting import setPilotingSource
from olympe.messages.ardrone3.Piloting import TakeOff, moveBy, Landing

SKYCTRL_IP = "192.168.53.1"

def main():
    drone = olympe.Drone(SKYCTRL_IP)
    drone.connect()
    drone(setPilotingSource(source="Controller")).wait().success()
    
    try:
        assert drone(TakeOff()).wait().success()
        time.sleep(3)
        
        assert drone(moveBy(1, 1, 0, 0)).wait().success()
        time.sleep(1)
        
        assert drone(moveBy(-1, -1, 0, 0)).wait().success()
        time.sleep(1)
        
    finally:
        assert drone(Landing()).wait().success()
        drone.disconnect()
    
if __name__ == "__main__":
    main()