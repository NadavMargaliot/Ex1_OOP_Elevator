from Elevator import *
from callForElevator import *
from Calls import *
from ElevatorMissions import *
from Building import *

class functions:

    def addCallToElevator(elevator , callSrc , callDst):
        elevator = Elevator
        elevCalls = elevator.getElevCalls()
        if callSrc not in elevCalls:
            elevCalls.append(callSrc)
        if callDst not in elevCalls:
            elevCalls.append(callDst)

    def isElevFinish(elevator):
        elevator = Elevator
        if len(elevator.getElevCalls() == 0):
            return True
        return False

    def removeCallFromElevator(elevator , call):
        elevator = Elevator
        elevCalls = elevator.getElevCalls()
        elevPos = elevator.getPos()
        if call in elevCalls and call == elevPos:
            elevCalls.remove(call)


