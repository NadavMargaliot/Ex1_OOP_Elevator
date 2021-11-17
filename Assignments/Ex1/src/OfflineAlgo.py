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


def allocateElevator(csvFile, jFile):
    resultCallList = fromCsvToArray(csvFile)
    callsList = fromCsvToArray(csvFile)
    building = Building(jFile)
    size = building.numOfElevators
    minTime = 99999999999
    moreThan8 = size > 8
    between4To8 = size > 4 and size < 8
    oneElevator = size == 1
    between2To4 = size > 1 and size < 4
    callsAround1000 = len(callsList) >= 999
    callsAround100 = len(callsList) >= 99
    representElevator = []
    if size < 6:
        for k in range(0,10):
            for i in range(0 , building.numOfElevators):
                representElevator.append(i)
    sizeFloors = abs(int(building.maxFloor) - int(building.minFloor))



    for j in range(0, 100):
        time = 0
        for i in callsList:
            floors = abs(int(i.src) - int(i.dst))
            if building.numOfElevators != 1:
                if len(representElevator) != 0:
                    # send the fastest elevator for a big mission
                    if floors > sizeFloors / 2 and len(representElevator) > 1:
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
                    if size < 6:
                        for d in range(0 , 10):
                            for k in range(0,size):
                                representElevator.append(k)
                    else:
                        for k in range(0, size):
                            representElevator.append(k)
                    i.bestElevator = random.choice(representElevator)
                    representElevator.remove(int(i.bestElevator))
            if size == 1:
                i.bestElevator = 0
            elev = building.ElevatorList[i.bestElevator]
           # elev.count += 1
            speed = elev.speed
            stop = elev.stopTime
            start = elev.startTime
            open = elev.openTime
            close = elev.closeTime
            df = abs(int(elev.pos) - int(i.src))
            elev.setPos(int(i.src))
            time += ((floors / speed) + df * (close + open + stop + start))


        if time / len(callsList) < minTime:
            resultCallList = callsList
            minTime = time / len(callsList)

    fromArrayToCsv(resultCallList)

    # def allocate(self):
    #     allocateElevator = self.callsList
    #     elevatorMissions = self.elevatorCalls
    #     building = self.building
    #     for i in allocateElevator:
    #         if i.src < i.dst:
    #             for j in building['_elevators']:
    #                 minTime = j.timeFromSrc()
    #                 if j.timeFromSrc() < minTime:
    #                     elevNum = j
    #                 self.addCallToElevator(elevNum, i.src, i.dst)
    #                 allocateElevator[i][5] = elevNum
    #                 # building.getElevator(elevNum).setPos(elevNum)
    #     return allocateElevator

    # same size array as the numOfElevators.
    # each index represent the "missions" that the elevator got from the allocate func


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

    calls_d = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_d.csv"
    calls_c = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_c.csv"
    calls_b = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_b.csv"
    calls_a = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv"

    B1 = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B1.json"
    B2 = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B2.json"
    B3 = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B3.json"
    B4 = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B4.json"

    B5 = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B5.json"
    allocateElevator(calls_a, B3)



if __name__ == '__main__':
    main()
