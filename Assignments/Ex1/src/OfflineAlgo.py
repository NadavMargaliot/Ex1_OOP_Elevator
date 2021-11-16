from Elevator import *
from callForElevator import *
from Calls import *
from ElevatorMissions import *
from Building import *
import random
import functions
import Building
import csv


class OfflineAlgo:
    def __init__(self, building="Building.json", calls="CallsList.csv"):
        self.building = Building(building)
        self.callsList = Calls.fromCsvToArray(calls)
        self.elevatorCalls = []
        for i in range(0, building.numOfElevators):
            self.elevatorCalls.append([])



    def addCallToElevator(self ,elevNum , callSrc , callDst):
        elevCalls = self.elevatorCalls[elevNum]
        if callSrc not in elevCalls:
            elevCalls.append(callSrc)
        if callDst not in elevCalls:
            elevCalls.append(callDst)

    # def removeCallFromElevator(self , elevNum , call):
    #     elevCalls = self.elevatorCalls[elevNum]
    #     elevPos =
    #     elevCalls = elevator.getElevCalls()
    #     elevPos = elevator.getPos()
    #     if call in elevCalls and call == elevPos:
    #         elevCalls.remove(call)




    def allocate(self):
        allocateElevator = self.callsList
        elevatorMissions = self.elevatorCalls
        building = self.building
        for i in allocateElevator:
            if i.src < i.dst:
                for j in building['_elevators']:
                    minTime = j.timeFromSrc()
                    if j.timeFromSrc() < minTime:
                        elevNum = j
                    self.addCallToElevator(elevNum , i.src , i.dst)
                    allocateElevator[i][5] = elevNum
                    # building.getElevator(elevNum).setPos(elevNum)
        return allocateElevator





















        # same size array as the numOfElevators.
        # each index represent the "missions" that the elevator got from the allocate func

    #  missions = []

    # def makeCall(self , csvFile):
    #     callsList = []
    #     with open(csvFile) as file:
    #         csvReader = csv.reader(file)
    #         for row in csvReader:
    #             callsList.append(callForElevator(row))
    #     return callsList

    # def allocate(self ):

    #
    # def totalTime(self, elevatorPos , srcCall , elevator):

    #

    def fromArrayToCsv(callsList):
        filename = 'output.csv'
        all = []
        for i in callsList:
            all.append(i.__dict__.values())
        with open(filename, 'w', newline="") as file:
            csvWriter = csv.writer(file)
            csvWriter.writerows(all)


# file = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv"
# c = OfflineAlgo.makeCall(file)
if __name__ == '__main__':
    import Building
    #
    # # file = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv"
    #  a = Calls()
    # # callsList = a.fromCsvToArray(file)
    # # # print(callsList)
    # #  filename = 'output.csv'
    # #  with open(filename, 'w', newline="") as file:
    # #      csvWriter = csv.writer(file)
    # #      csvWriter.writerows(callsList)
    # # #
    # #
    # # r = OfflineAlgo

    a = Calls()
    file2 = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_d.csv"
    file_json = r"/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/src/B5.json"
    callsList2 = a.fromCsvToArray(file2)

    for i in callsList2:
        i.bestElevator = random.randint(0 , 9)

    r = OfflineAlgo
    # r.fromArrayToCsv(callsList2)
    print("ggg")
    b = Building(file_json)
    g = OfflineAlgo(file_json , file2)
    check = g.allocate()
    g.fromArrayToCsv(check)

    # self.building.getElevator(self, elev).row[2]




