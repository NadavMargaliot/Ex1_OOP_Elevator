import csv
import random


class Calls:
    def __init__(self,someString="", time=0, src=0, dst=0, status=0, bestElev=0):
        self.someString = someString
        self.time = time
        self.src = src
        self.dst = dst
        self.status = status
        self.bestElevator = bestElev

    def getStateOfCall(self):
        if self.src < self.dst:
            return 1
        else:
            return -1

    def __repr__(self):
        # return f'{self.time} {self.src} {self.dst}'
        return f'time: {self.time} src: {self.src} ' \
               f'dst: {self.dst} status:{self.status} best elevator:{self.bestElevator}'

