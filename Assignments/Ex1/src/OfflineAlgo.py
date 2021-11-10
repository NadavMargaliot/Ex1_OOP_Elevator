from Elevator import *
from callForElevator import *
import Calls
import Building
import csv

class OfflineAlgo:

    def __init__(self , building):
        # same size array as the numOfElevators.
        # each index represent the "missions" that the elevator got from the allocate func
        missions = []

    def makeCall(self , csvFile):
        callsList = []
        with open(csvFile) as file:
            csvReader = csv.reader(file)
            for row in csvReader:
                callsList.append(callForElevator(row))




    # def allocate(self):
    #
    # def totalTime(self, elevatorPos , srcCall , elevator):
    #
    # def goTo(self):
    #
    # def cmdElevator(self , elev):

