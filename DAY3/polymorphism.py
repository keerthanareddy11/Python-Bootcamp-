class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):  #displays
        return f'{self.name} {self.age}'
class Student(Person):
    def __init__(self,name,roll,age,branch):
        super().__init__(self,name,age)
        self.roll=roll
        self.branch=branch
    perdetails=super().__str__()
    return f'{perdetails} {self.roll} {self.branch}'
obj=Person("keerthi",20)
print(obj)

