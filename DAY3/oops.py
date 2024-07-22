'''class Student:
    def __init__(self,name,roll,branch,address,email):
        self.name=name
        self.roll=roll
        self.branch=branch
        self.address=address
        self.email=email
    def show(self):
        print("name is",self.name)
        print("roll no is",self.roll)
        print("branch",self.branch)
        print("address is",self.address)
        print("email is",self.email)
obj=Student("keerthi",100,"CSE","itikyal","keerthi@gmail.com")   #obj is creating
obj.show()'''

#BAnk details
'''class Bank:
    def __init__(self,name,accountno,address,mobileno):
        self.name=name
        self.accountno=accountno
        self.address=address
        self.mobileno=mobileno
    def dispaly(self):
        print("name of account holder is",self.name)
        print("account number is",self.accountno)
        print("Address is",self.address)
        print("mobile number is",self.mobileno)
b=Bank("keerthi")'''



'''class Student:
    #static 
    branch="CSE"
    def __init__(self,name,roll,address,email):
        self.name=name
        self.roll=roll
        
        self.address=address
        self.email=email
    def show(self):
        print("name is",self.name)
        print("roll no is",self.roll)
        print("branch",Student.branch)#creating with classname
        print("address is",self.address)
        print("email is",self.email)
obj=Student("keerthi",100,"itikyal","keerthi@gmail.com")   #obj is creating
obj.show()'''


'''class Bank:
    ifsc=15790
    def __init__(self,name,accountno,address,mobileno):
        self.name=name
        self.accountno=accountno
        self.address=address
        self.mobileno=mobileno
    def display(self):
        print("name of account holder is",self.name)
        print("account number is",self.accountno)
        print("Address is",self.address)
        print("mobile number is",self.mobileno)
        print("ifsc code is",Bank.ifsc)
b=Bank("keerthi",1901000234,"itikyal",6301222627)
b.display()'''


#without using display()

'''class Bank:
    ifsc=15790
    def __init__(self,name,accountno,address,mobileno):
        self.name=name
        self.accountno=accountno
        self.address=address
        self.mobileno=mobileno
    def __str__(self):
        return f'name is {self.name} account number is {self.accountno} {self.address} {self.mobileno} {Bank.ifsc}'
        
b=Bank("keerthi",1901000234,"itikyal",6301222627)
print(b)'''

#INHERITANCE
'''class Vehicle:
    def brake():
        print("brake adhists movement of a vehicle")
    def clutch():
        print("this is clutch")
    def accelerator():
        print("increases speed")
    def tyre():
        print("this is tyre")
class bike(Vehicle):
    def handle():
        print("turns the bike")
    def horn():
        print("makes sound")
bobj=bike
bobj.handle()
bobj.horn()
bobj.clutch()
bobj.tyre()
vobj=Vehicle'''
#
# vobj.handle()  #cannot inherit from bike class because Vehicle

#MUTIPLE INHERITANCE
#ABSTRACTION
'''from abc import ABC
class Mobile(ABC):
    def storage():#abstract methood
        pass
    def calling():#non abstract method
        print("hey iam calling")
class Samsung(Mobile):
    def storage():
        print("samsung has 128gb storage")
    def camera():#non abstract
        print("50mp")
class iphone(Mobile):
    def storage():
        print("iphone has 258gb storage")
class vivo(Mobile):
    def storage():
        print("vivo has 64gb")
samobj=Samsung
samobj.storage() #displays only samsung storage
samobj.camera()
iphoneobj=iphone
iphoneobj.storage()
vivoobj=vivo
vivoobj.storage()
vivo.calling()'''


    