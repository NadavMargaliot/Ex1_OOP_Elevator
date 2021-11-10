import csv


class Calls:
    def __init__(self, time=0, src=0, dst=0, status=0, bestElev=0):
        self.time = time
        self.src = src
        self.dst = dst
        self.status = status
        self.bestElevator = bestElev

    # def __init__(self, csvFile, numCall):
    #     # all = []
    #     callsList = []
    #     with open(csvFile) as file:
    #         csvReader = csv.reader(file)
    #         for row in csvReader:
    #             callsList.append(row[1:4])
    #         # all.append(callsList)
    #     self.callsList = callsList
    #     self.time = callsList[numCall][0]
    #     self.src = callsList[numCall][1]
    #     self.dst = callsList[numCall][2]
    #     if callsList[numCall][1] < callsList[numCall][2]:
    #         self.upOrDown = 1
    #     elif callsList[numCall][1] > callsList[numCall][2]:
    #         self.upOrDown = -1

    def fromCsvToArray(self, csvFile):
        callsList = []
        with open(csvFile) as file:
            csvReader = csv.reader(file)
            for row in csvReader:
                call = Calls(row[1], row[2], row[3], row[4], row[5])
                callsList.append(call)
        return callsList

    def __repr__(self):
        # return f'{self.time} {self.src} {self.dst}'
        return f'time: {self.time} src: {self.src} ' \
               f'dst: {self.dst} status:{self.status} best elevator:{self.bestElevator}'


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