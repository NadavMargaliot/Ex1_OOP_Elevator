
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


    def __repr__(self):
        return f'Elevator id: {self.id}, speed: {self.speed}, min floor: {self.minFloor},' \
               f' max floor: {self.maxFloor}, close time: {self.closeTime}, open time: {self.openTime},' \
               f' start time: {self.startTime}, stop time: {self.stopTime}, state: {self.state}, pos: {self.pos}\n'

    def getElevCalls(self):
        return self.elevCalls

    def getPos(self):
        return self.pos

    def getCloseTime(self):
        return self.closeTime

    def getOpenTime(self):
        return self.openTime

    def getSpeed(self):
        return self.speed

    def getStartTime(self):
        return self.startTime

    def getStopTime(self):
        return self.stopTime

    def timeFromSrc(self , callSrc):
        open = self.openTime
        close = self.closeTime
        start = self.startTime
        stop = self.stopTime
        df = abs(callSrc - self.pos)
        speed = self.speed
        return close + start + (df / speed) + stop + open

    def didElevatorPassUp(self, callSrc):
        if callSrc > self.pos:
            return True
        return False

    def didElevatorPassDown(self, callSrc):
        if callSrc < self.pos:
            return True
        return False

    def setPos(self , newPos):
        self.pos = newPos

    def addCallToElevator(self , callSrc , callDst):
        elevCalls = self.elevCalls
        if callSrc not in elevCalls:
            elevCalls.append(callSrc)
        if callDst not in elevCalls:
            elevCalls.append(callDst)