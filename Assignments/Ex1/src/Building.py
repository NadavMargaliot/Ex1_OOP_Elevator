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

    def getNumOfElevators(self):
        return self.numOfElevators







file = r"/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/src/B5.json"
file2 = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B2.json"

b5 = Building(file)
b2 = Building(file2)
# for i in b.ElevatorList:
#     print(i.__str__())
# print(b5.minFloor)
# print(b5.numOfElevators)
# print(b5.getElevator(9))
#
# print(b2.numOfElevators)
# print(b2.minFloor)
# print(b2)
# for i in b5.ElevatorList:
# #     print(i.__str__())
#
# print(b5.ElevatorList)
# print(b5.numOfElevators)
# print(b5.minFloor)


