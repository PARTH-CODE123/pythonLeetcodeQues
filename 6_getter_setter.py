class Myclass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"value is {self._value}")

    def ten_value(self):
        return 10* self._value        
    
obj= Myclass(10)
print(obj.ten_value)
obj.show()