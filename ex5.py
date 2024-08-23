class Vehicle():
    def __init__(self, make, model, year):
        self.make= str(make)
        self.model=str(model)
        self.year= int(year)
class Car(Vehicle):
    doors = 4
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.make=str(make)
        self.model=str(model)
        self.year=int(year)
    def start(self):
        return f"car started: made by {self.make} - model {self.make} - year made {self.make} - Doors: {self.doors}"
    def doors_change(self,new_doors):
        self.type = new_doors
    @classmethod
    def doors_change_totaly(cls,new_doors):
        cls.type = new_doors
class Motorcycle(Vehicle):
    type = "Sport"
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.make=str(make)
        self.model=str(model)
        self.year=int(year)
    def start(self):
        return f"motorcycle started: made by {self.make} - model {self.make} - year made {self.make} - type {self.type}"
    def type_change(self,new_type):
        self.type = new_type
    @classmethod
    def type_change_totaly(cls,new_type):
        cls.type = new_type
car1= Car("Toyota","X32",2018)
m1=Motorcycle("Kavir","X56",2012)
car1.doors_change(2)
m1.type_change("Fast")
print(car1.start())
print(m1.start())
