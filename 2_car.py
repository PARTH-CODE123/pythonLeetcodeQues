class car():
    def __init__(self,name,mileage,speed,time):
        self.name=name
        self.mileage=mileage
        self.speed=speed
        self.time=time
    def distance(self):
        self.dist = self.speed*self.time
        print(f"total distance {self.name} can travel with speed {self.speed}KM/Hr in time {self.time} Hr's will be: {self.dist}KM!!! and will give mileage {self.mileage}KM/L")
a=car("BMW",18,60,4)
a.distance()
        

