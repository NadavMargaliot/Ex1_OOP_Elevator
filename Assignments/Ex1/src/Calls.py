import csv


class Calls:
    def __init__(self,someString="", time=0, src=0, dst=0, status=0, bestElev=0):
        self.someString = someString
        self.time = time
        self.src = src
        self.dst = dst
        self.status = status
        self.bestElevator = bestElev


    def fromCsvToArray(self, csvFile):
        callsList = []
        with open(csvFile) as file:
            csvReader = csv.reader(file)
            for row in csvReader:
                call = Calls(row[0],row[1], row[2], row[3], row[4],row[5])
                callsList.append(call)
        return callsList

    def getStateOfCall(self):
        if self.src < self.dst:
            return 1
        else:
            return -1


# if self.src < self.dst:
#     self.upOrDown = 1
# elif self.src > self.dst:
#     self.upOrDown = -1

    # def __repr__(self):
    #     # return f'{self.time} {self.src} {self.dst}'
    #     return f'time: {self.time} src: {self.src} ' \
    #            f'dst: {self.dst} status:{self.status} best elevator:{self.bestElevator}\n'


file = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv"

# c = Calls.fromCsvToCallsArray(file)


# all = []
# callsList = []
# with open(file) as listCall:
#     csvReader = csv.reader(listCall)
#     for row in csvReader:
#         c = Calls(time=row[1], src=row[2], dst=row[3])
#         callsList.append(row[1:4])
#         all.append(c)
#
# print(callsList)
# # print(all)
# # print(all[0])
#
# c = Calls(file)
# print(c)
# # print(c.callsList[0])
# # print(c.callsList[0][0])
#
# print(c.dst)
# print(c.time)
# # print(c.upOrDown)
if __name__ == '__main__':
    a = Calls()
    c = a.fromCsvToArray(file)
    for i in c:
        print(i)
