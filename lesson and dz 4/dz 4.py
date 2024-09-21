class School:
    rooms = 2
    def __init__(self, rooms):
        super().__init__()
        self.rooms = rooms

class Cabinet1:
    pupils = 8
    def __init__(self, pupils1, rooms):
        super().__init__(rooms)
        self.pupils1 = pupils1

class Cabinet2:
    pupils = 13
    def __init__(self, pupils2, rooms):
        super().__init__(rooms)
        self.pupils2 = pupils2

class Info(School, Cabinet1, Cabinet2):
    def print_info(self):
        print("Rooms - ", self.rooms)
        print("Cabinet1 -", self.pupils1)
        print("Cabinet2 -", self.pupils2)

info = Info
info.print_info()