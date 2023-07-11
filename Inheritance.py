class Animal:
    def __init__(self,__num,_name,age):
        self.__num=__num
        self._name=_name
        self.age=age
    def info(self,breed):
        
        self.breed=breed
        return (f"Name of animal with Number {self.__num}! is {self.__name} and his age is {self.age} Years and Breed is {self.breed}")
    def eat(self):
        print("THis is the eat of Animal class")
        self.eatwhateatwhat=input("Enter what does the Animal Eats: ")
        # self.eatwhat=eatwhat
class Human(Animal):
    def __init__(self, __num, _name, age,proffession):
        super().__init__(__num, _name, age)
        self.proffession=proffession
    def AnimalWork(self,working_years):
        self.working_years=working_years
    def __str__(self):
        return f"Name of Human is {self._name} with number {self.__num} and his/her age is {self.age} and working as an {self.proffession} for {self.working_years} Years"
class lady(Human):
    def __init__(self, __num, /, _name, age,Ladyheight,NoOfLegs):
        super().__init__(__num, _name, age)
        self.Ladyheight=Ladyheight           
        self.NoOfLegs=NoOfLegs
    def __str__(self):
        return f"Name of Lady is {self._name} with number {self.__num} and his/her age is {self.age} and having NoOfLegs as {self.NoOfLegs} with height{self.Ladyheight} cm's"
    def eat(self):
        return("This is eat of Lady Class ")

ani=Animal(420,"Hippo",4)   
ani.info()
         
