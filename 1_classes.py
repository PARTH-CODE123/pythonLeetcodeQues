class Person():
    def __init__(self,name,occ):
        self.name=name
        self.occ=occ
    def info(self):
        print(f"{self.name} is a {self.occ}")    
a=Person("parth","HR")
b=Person("Sunita","Accountant")
a.info()
b.info()
