def greet(fx):
    def mfx():
        print("hello Boys today your are going to learn Mathematics and in that too its : ")
        fx()
        print("has been learnt today ")
    return mfx





@greet
def multiplly():
    print("Multiplication",end=" ")
    num=int(input("Enter the number to say the table: "))
    for i in range(10):
        print(f"'{num}' X {i+1} = {num*(i+1)}")
    print("Multiplication ")

def division():
    print("Division",end=" ")
    num=int(input("Enter the number to say the Division Table: "))
    for i in range(10):
        print(f"'{num}' / {i+1} = {num/(i+1)}")
    print("Division ",end=" ")
def divisiion():
    print("Divisiion", end=" ")
    num = int(input("Enter the number to generate the Division Table: "))
    for i in range(10):
        result = num / (i + 1)
        print(f"'{num}' / {i + 1} = {result:0.2f}")
    print("Divisiion ", end=" ")    

multiplly()        
divisiion()        