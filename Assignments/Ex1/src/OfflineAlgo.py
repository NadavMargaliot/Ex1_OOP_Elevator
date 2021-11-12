from Elevator import *
from callForElevator import *
from Calls import *
from ElevatorMissions import *
from Building import *

import Building
import csv


class OfflineAlgo:
    def __init__(self, building="Building.json", calls="CallsList.csv", opCsv="output.csv"):
        self.building = Building("Building.json")
        self.callsList = Calls.fromCsvToArray("Calls.csv")
        self.elevatorCalls = []
        for i in range(0, building.numOfElevators):
            self.elevatorCalls.append([])

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

    def totalTime(self , src , elevator):
        self.elev = Elevator
        elevator

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
    file = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv"
    a = Calls()
    callsList = a.fromCsvToArray(file)
   # print(callsList)
   #  filename = 'output.csv'
   #  with open(filename, 'w', newline="") as file:
   #      csvWriter = csv.writer(file)
   #      csvWriter.writerows(callsList)
   #



    r = OfflineAlgo
    r.fromArrayToCsv(callsList)

    #print(len(callsList))


