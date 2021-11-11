

class callForElevator:

    def __init__(self , row):
        self.someString = str(row[0])
        self.time = float(row[1])
        self.src = int(row[2])
        self.dst = int(row[3])
        self.elevatorStatus = int(row[4])
        self.best = int(row[5])
       # if self.src < self.dst