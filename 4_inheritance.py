class Animal:
    def __init__(self, num, name, age):
        self.__num = num
        self._name = name
        self.age = age

    def info(self, breed):
        self.breed = breed
        return f"Name of animal with Number {self.__num} is {self._name} and its age is {self.age} years. Breed is {self.breed}"

    def eat(self):
        self.eatwhateatwhat = input("Enter what does the Animal eat: ")
        print(f"The animal eats {self.eatwhateatwhat}")


class Human(Animal):
    def __init__(self, num, name, age, profession):
        super().__init__(num, name, age)
        self.profession = profession

    def __str__(self):
        return f"Name of Human is {self._name} with number {self._Animal__num} and their age is {self.age}. They work as a {self.profession}"
    def eat(self):
        super().eat()
        return("This is eat of Human Class ")

class Lady(Human):
    def __init__(self, num, name, age, height, no_of_legs):
        super().__init__(num, name, age, "Lady")
        self.height = height
        self.no_of_legs = no_of_legs

    def __str__(self):
        return f"Name of Lady is {self._name} with number {self._Animal__num}, their age is {self.age}. They have {self.no_of_legs} legs and a height of {self.height} cm."
    # def eat(self):
    #     super().eat()
    #     return("This is eat of Lady Class ")


# ani = Animal(420, "Hippo", 4)
# print(ani.info("Giant Hippo"))  # Provide the breed as an argument

# human = Human(123, "John", 30, "Engineer")
# print(human)

lady = Lady(456, "Jane", 25, 160, 2)
print(lady.eat())


