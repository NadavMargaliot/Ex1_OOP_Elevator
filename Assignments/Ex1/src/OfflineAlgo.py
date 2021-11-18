from Calls import Calls
from Building import Building
import random
import csv

def reFill(array, times, sizeOfElevs):
    for j in range(0, times):
        for i in range(0, sizeOfElevs):
            array.append(i)

# This function makes a calls array from a csv file.
def fromCsvToArray(csvFile):
    callsList = []
    with open(csvFile) as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            call = Calls(row[0], row[1], row[2], row[3], row[4], row[5])
            callsList.append(call)
    return callsList

# This function makes a csv file from a calls array.
def fromArrayToCsv(callsList):
    filename = 'output.csv'
    all = []
    for i in callsList:
        all.append(i.__dict__.values())
    with open(filename, 'w', newline="") as file:
        csvWriter = csv.writer(file)
        csvWriter.writerows(all)

# This function gets a csv file represents a calls list
# And json file represents a building.
# this function allocates ALL the calls!
def allocateElevator(csvFile, jFile):
    callsList = fromCsvToArray(csvFile)
    building = Building(jFile)
    size = building.numOfElevators
    if size == 1:
        for i in callsList:
            i.bestElevator = 0
        fromArrayToCsv(callsList)
        return
    sizeFloors = abs(int(building.maxFloor) - int(building.minFloor))
    between0To15Floors = sizeFloors > 0 and sizeFloors < 15  # B1 , B2
    moreThan100Floors = sizeFloors > 100  # B3 , B4 , B5
    moreThan8Elevator = size > 8  # B5
    between4To8Elevator = size > 4 and size < 8  # B4
    between2To4Elevator = size > 1 and size < 4  # B2 , B3
    callsAround1000 = len(callsList) >= 999  # b ,c , d
    representElevator = []
    if callsAround1000:
        if moreThan8Elevator:
            reFill(representElevator, 2, size)
        elif between4To8Elevator:
            reFill(representElevator, 4, size)
        elif between2To4Elevator:
            reFill(representElevator, 10, size)
    else:  # calls around 100
        if moreThan8Elevator:
            reFill(representElevator, 1, size)
        elif between4To8Elevator:
            reFill(representElevator, 3, size)
        elif between2To4Elevator:
            reFill(representElevator, 4, size)

    for i in callsList:
        floors = abs(int(i.src) - int(i.dst))
        if len(representElevator) != 0:
            # send the fastest elevator for a big mission
            if between0To15Floors:
                highMission = sizeFloors / 2
            elif moreThan100Floors:
                highMission = sizeFloors / 10
            if floors > highMission and len(representElevator) > 1:
                speedOfElev = 0
                for sp in representElevator:
                    if building.ElevatorList[sp].speed > speedOfElev:
                        speedOfElev = building.ElevatorList[sp].speed
                        chosen = int(building.ElevatorList[sp].id)
                i.bestElevator = chosen
                representElevator.remove(int(chosen))
            else:
                i.bestElevator = random.choice(representElevator)
                representElevator.remove(int(i.bestElevator))
        else:
            if callsAround1000:
                if moreThan8Elevator:
                    reFill(representElevator, 2, size)
                elif between4To8Elevator:
                    reFill(representElevator, 4, size)
                elif between2To4Elevator:
                    reFill(representElevator, 10, size)
            else:  # calls around 100
                if moreThan8Elevator:
                    reFill(representElevator, 1, size)
                elif between4To8Elevator:
                    reFill(representElevator, 3, size)
                elif between2To4Elevator:
                    reFill(representElevator, 4, size)
            i.bestElevator = random.choice(representElevator)
            representElevator.remove(int(i.bestElevator))
    fromArrayToCsv(callsList)

def main():
    calls_d = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_d.csv"
    calls_c = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_c.csv"
    calls_b = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_b.csv"
    calls_a = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv"

    B1 = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B1.json"
    B2 = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B2.json"
    B3 = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B3.json"
    B4 = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B4.json"
    B5 = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B5.json"
    # allocateElevator(calls_d, B5)

if __name__ == '__main__':
    main()
