import json
from typing import Any


class Elevator:
    def __init__(self, dict):
        self.id = int(dict["_id"])
        self.speed = float(dict["_speed"])
        self.minFloor = int(dict["_minFloor"])
        self.maxFloor = int(dict["_maxFloor"])
        self.closeTime = float(dict["_closeTime"])
        self.openTime = float(dict["_openTime"])
        self.startTime = float(dict["_startTime"])
        self.stopTime = float(dict["_stopTime"])
        self.state = 0 # elevator in level state
        self.pos = 0 # elevator will start in 0 floor

    # @classmethod
    # def from_json(cls, json_string):
    #     json_dict = json.loads(json_string)
    #     return cls(**json_dict)

    def __repr__(self):
        return f'Elevator id: {self.id}, speed: {self.speed}, min floor: {self.minFloor},' \
               f' max floor: {self.maxFloor}, close time: {self.closeTime}, open time: {self.openTime},' \
               f' start time: {self.startTime}, stop time: {self.stopTime}, state: {self.state}, pos: {self.pos}\n'

    # def setState(self , state):
    #     self.state = state

    # def goTo(self, floor):

