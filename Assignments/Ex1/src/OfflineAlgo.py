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
        self.state = 0 # elevator in level state
        self.pos = 0 # elevator will start in 0 floor
        self.elevCalls = []
        self.currTime = 0


# def timeFromSrc(self, callSrc):
#     open = self.openTime
#     close = self.closeTime
#     start = self.startTime
#     stop = self.stopTime
#     df = abs(callSrc - self.pos)
#     speed = self.speed
#     return close + start + (df / speed) + stop + open


def allocateElevator(csvFile , jFile):
    resultCallList = fromCsvToArray(csvFile)
    callsList = fromCsvToArray(csvFile)
    building = Building(jFile)
    size = building.numOfElevators
    minTime = 99999999999

    for j in range(0, 100):
        time = 0
        for i in callsList:
            i.bestElevator = int(random.randint(0 , size - 1))
            elev = building.ElevatorList[i.bestElevator]
            floors = abs(int(i.src) - int(elev.pos))
            speed = elev.speed
            stop = elev.stopTime
            start = elev.startTime
            open = elev.openTime
            close = elev.closeTime
            df = abs(int(elev.pos) - int(i.src))
            time +=  ((floors / speed) + df * (close + open + stop + start))
        if time < minTime:
            resultCallList = callsList
            minTime = time

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
            call = Calls(row[0],row[1], row[2], row[3], row[4],row[5])
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

    a = Calls()
    file2 = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_d.csv"
    file_json = r"/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/src/B5.json"
    callsList2 = fromCsvToArray(file2)



    file = r"/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/src/B5.json"

    # for i in callsList2:
    #     i.bestElevator = random.randint(0, 9)
    #     print(i.bestElevator)
    #
    # fromArrayToCsv(callsList2)


    allocateElevator(file2 , file_json)


if __name__ == '__main__':
    main()




