import json
from Elevator import *

class Building:
    def __init__(self, j_file):
        with open(j_file, 'r') as json_file:
            jsonLoad = json.load(json_file)
            self.minFloor = jsonLoad['_minFloor']
            self.maxFloor = jsonLoad['_maxFloor']
            elevatorList = []
            for e in jsonLoad['_elevators']:
                elevatorList.append(Elevator(e))
            self.ElevatorList = elevatorList
            self.numOfElevators = len(elevatorList)
        json_file.close()

    def getElevator(self, i):
        if i >= 0 and i < self.numOfElevators:
            return i

    def getNumOfElevators(self) -> int:
        return self.numOfElevators
