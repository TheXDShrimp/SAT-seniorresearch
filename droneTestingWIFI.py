import olympe
import time
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveBy
from olympe.messages.ardrone3.PilotingState import (
    PositionChanged,
    AlertStateChanged,
    FlyingStateChanged,
    NavigateHomeStateChanged,
)

class FlightListener(olympe.EventListener):

    @olympe.listen_event(FlyingStateChanged() | AlertStateChanged() |
        NavigateHomeStateChanged())
    def onStateChanged(self, event, scheduler):
        print("{} = {}".format(event.message.name, event.args["state"]))

    @olympe.listen_event(PositionChanged())
    def onPositionChanged(self, event, scheduler):
        print(
            "latitude = {latitude} longitude = {longitude} altitude = {altitude}".format(
                **event.args
            )
        )


drone = olympe.Drone("192.168.42.1")
with FlightListener(drone):
    drone.connect()
    drone(
        FlyingStateChanged(state="hovering")
        | (TakeOff() & FlyingStateChanged(state="hovering"))
    ).wait()
    time.sleep(1)
    drone(moveBy(1, 0, 0, 0)).wait()
    drone(Landing()).wait()
    drone(FlyingStateChanged(state="landed")).wait()
    drone.disconnect()
