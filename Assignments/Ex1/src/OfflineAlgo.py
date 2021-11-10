from Elevator import *
from callForElevator import *
from Calls import *

import Building
import csv

class OfflineAlgo:

    def __init__(self , bJson = "Building.json" ,callsCsv = "Calls.csv" , opCsv = "output.csv"):
        self.bJson = Building("Building.json")
        self.callsCsv = Calls.fromCsvToArray("Calls.csv")




        # same size array as the numOfElevators.
        # each index represent the "missions" that the elevator got from the allocate func
      #  missions = []

    def makeCall(self , csvFile):
        callsList = []
        with open(csvFile) as file:
            csvReader = csv.reader(file)
            for row in csvReader:
                callsList.append(callForElevator(row))
        return callsList

    # def allocate(self):
    #
    # def totalTime(self, elevatorPos , srcCall , elevator):
    #
    # def goTo(self):
    #
    # def cmdElevator(self , elev):
    #


file = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv"
c = OfflineAlgo.makeCall(file)