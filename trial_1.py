class employee:
    def __init__(self,name,age,occ):
        self.name=name
        self.age=age
        self.occ=occ
    def show(self):
        print(f"[PARENT CLASS] name of employee is : {self.name} is of age : {self.age} and working in Proffesion {self.occ}")
class human(employee):
    def __init__(self,name,age,occ,lang,college):
        super().__init__(name,age,occ)
        self.lang=lang
        self.college=college
        print(f" The child is learning {self.lang} in college {self.college}")
    def show(self):
        print(f"[CHILD CLASS] name of employee is : {self.name} is of age : {self.age} and working in Proffesion {self.occ}")
        super().show()
emp=human("parth",18,"SD","english","SIT")
emp.show()