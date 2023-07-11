def greet(fx):
        def mfx(*args,**kwargs):
            
            print("Hello Good Morning")
            fx(*args,**kwargs)
            print("Thak you for using me :) ")
        return mfx    
        
class emp:
    def __init__(self,name,occ,company):
        self.name=name
        self.occ=occ
        self.company=company
    @ greet    
    def Salary_Increment(self,Initial_salary):
        self.Initial_salary=Initial_salary
        self.annualBonus=self.Initial_salary*0.02+self.Initial_salary
        print(f"Salary_Increment of {self.name} in {self.company} at role {self.occ} is {self.annualBonus}!! from {self.Initial_salary}")
    

# def add(a,b):
#     c=a+b
#     print(f"Add of 2 no. is {c}")
# a1=add(2,5)

e1=emp("parth","HR","HCL")
e1.Salary_Increment(100)
# print(e1.name)



            
