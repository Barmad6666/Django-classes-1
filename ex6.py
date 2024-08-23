from abc import abstractmethod, ABC 
class MarineAnimal():
    def __init__(self, name, habitat):
        self.name = str(name)
        self.habitat = str(habitat)
    @abstractmethod
    def move():
        pass
    @abstractmethod
    def eat():
        pass
class Fish(MarineAnimal):
    def __init__(self, fin_type, swim_speed,name,habitat):
        super().__init__(name,habitat)
        self.name=name 
        self.habitat= habitat
        self.fin_type = fin_type
        self.swim_speed = swim_speed
    def move(self):
        return f"this Fish swims in speed of {self.swim_speed}"
    def eat(self):
        return f"Fish eat sea plants or plangtons"
class Crustacean(MarineAnimal):
    def __init__(self, shell_type , crawl_speed ,name ,habitat):
        super().__init__(name,habitat)
        self.name=name 
        self.habitat= habitat
        self.shell_type  = shell_type 
        self.crawl_speed  = crawl_speed 
    def move(self):
        return f"this Crustacean crawls in speed of {self.crawl_speed}"
    def eat(self):
        return f"Crustaceans eat smaller animals or sea grasses"
def calling(*a):
    for aa in a:
        print(aa.move())
        print(aa.eat())
F1=Fish("Gold Fish","the Caspian Sea","long","1 metter per second")
C1=Crustacean("Snail","In Farms","Mediem-Big","0.01 metter per second")
calling(F1,C1)