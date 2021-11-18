from Calls import *
from Building import *
import random
import Building
import csv


# def addCallToElevator(self, elevNum, callSrc, callDst):
#     elevCalls = self.elevatorCalls[elevNum]
#     if callSrc not in elevCalls:
#         elevCalls.append(callSrc)
#     if callDst not in elevCalls:
#         elevCalls.append(callDst)

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
        self.state = 0  # elevator in level state
        self.pos = 0  # elevator will start in 0 floor
        self.elevCalls = []
        self.currTime = 0

    def setPos(self, newPos):
        self.pos = newPos


# def timeFromSrc(self, callSrc):
#     open = self.openTime
#     close = self.closeTime
#     start = self.startTime
#     stop = self.stopTime
#     df = abs(callSrc - self.pos)
#     speed = self.speed
#     return close + start + (df / speed) + stop + open

def reFill(array, times, sizeOfElevs):
    for j in range(0, times):
        for i in range(0, sizeOfElevs):
            array.append(i)


def addBestToCallAndRemoveFromArray(array, call, best):
    call.bestElevator = best
    array.remove(int(best))


def allocateElevator(csvFile, jFile):
    resultCallList = fromCsvToArray(csvFile)
    callsList = fromCsvToArray(csvFile)
    building = Building(jFile)
    size = building.numOfElevators
    if size == 1:
        for i in callsList:
            i.bestElevator = 0
        fromArrayToCsv(callsList)
        return
    minTime = 99999999999
    sizeFloors = abs(int(building.maxFloor) - int(building.minFloor))
    between0To15Floors = sizeFloors > 0 and sizeFloors < 15  # B1 , B2
    moreThan100Floors = sizeFloors > 100  # B3 , B4 , B5
    moreThan8Elevator = size > 8  # B5
    between4To8Elevator = size > 4 and size < 8  # B4
    oneElevator = size == 1  # B1
    between2To4Elevator = size > 1 and size < 4  # B2 , B3

    callsAround1000 = len(callsList) >= 999  # b ,c , d
    callsAround100 = len(callsList) <= 101  # a
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
                highMission = sizeFloors / 5
            if floors > highMission and len(representElevator) > 1:
                speedOfElev = 0
                for sp in representElevator:
                    if building.ElevatorList[sp].speed > speedOfElev:
                        speedOfElev = building.ElevatorList[sp].speed
                        chosen = int(building.ElevatorList[sp].id)
                # addBestToCallAndRemoveFromArray(representElevator, i ,chosen)
                i.bestElevator = chosen
                representElevator.remove(int(chosen))
            else:
                # addBestToCallAndRemoveFromArray(representElevator, i ,i.bestElevator)
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
            #   addBestToCallAndRemoveFromArray(representElevator, i , i.bestElevator)
            i.bestElevator = random.choice(representElevator)
            representElevator.remove(int(i.bestElevator))
        elev = building.ElevatorList[i.bestElevator]
        speed = elev.speed
        stop = elev.stopTime
        start = elev.startTime
        open = elev.openTime
        close = elev.closeTime
        df = abs(int(elev.pos) - int(i.src))
        elev.setPos(int(i.src))
       # time += ((floors / speed) + df * (close + open + stop + start))

        # if time / len(callsList) < minTime:
        #     resultCallList = callsList
        #     minTime = time / len(callsList)

    fromArrayToCsv(callsList)


def fromCsvToArray(csvFile):
    callsList = []
    with open(csvFile) as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            call = Calls(row[0], row[1], row[2], row[3], row[4], row[5])
            callsList.append(call)
    return callsList


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
    allocateElevator(calls_d, B5)


if __name__ == '__main__':
    main()
