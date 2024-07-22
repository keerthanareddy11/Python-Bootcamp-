'''class Employee:
    def __init__(self):           #without passing parametrs
        self.name='keerthi'   
        self.role='developer'
        self.__salary=85000  # __ for private
    def salary(self):
        return self.__salary
    def display(self):
      print(self.name,self.role)
e1=Employee()
e1.display()'''



class Employee:
    def __init__(self,name,role,salary):           #with  passing parametrs
        self.name=name
        self.role=role
        self.__salary=salary  # __ for private
    def _get_salary(self):    #making protected
        return self.__salary
    def empdisplay(self):
      print(self.name,self.role)
class Company(Employee):
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc
    def Comdisplay(self):
        print(self.cname,self.loc)
    def _hiring(self):
        print("hiring freshers")
cobj=Company("accenture","hyd")
eobj=Employee("keerthi","webdeveloper",85000)
eobj.empdisplay()
print(eobj._get_salary())
print(cobj._hiring())






