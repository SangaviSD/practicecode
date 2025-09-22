##-------------------------------function---------------------
##def Add(a,b):
##    result=a+b
##    return result
##print(Add(5,7))
##print(Add(7,5))


##def sim(p,n,r):
##    result=p+n+r//100
##    return result
##print(sim(5,6,9))
##

##list1=[1,2,3]
##a=" "
##for i in list1:
##    a=a+str(i)
##print(a)
##
##list2=[1,2,3]
##for i in list2:
##    print(list2,end=' ')


##a=10
##b=0
##c=1
##for i in range(a):
##    print(c,end=" ")
##    b,c=c,b+c
    
##----------------------------------------------------oops-----------------------------------------

##class Calculator:
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##    def add(self):
##        return self.a+self.b
##    def sub(self):
##        return self.a-self.b
##    def mul(self):
##        return self.a*self.b
##
##obj=Calculator(4,6)
##print(obj.add())
##print(obj.sub())
##print(obj.mul())
##
##class Dog:
##    def __init__(self,name,color):
##        self.name=name
##        self.color=color
##    def bark(self):
##         print(f"The barking {self.name} is {self.color} in color")
##    def play(self):
##        print(f"The dog Playing is {self.name}")
##
##a=str(input("enter dog name:"))
##b=str(input("enter dog color:"))
##obj=Dog(a,b)
##print(obj.bark())
##print(obj.play())
    
##class cal:
##    def __init__(self,amont,balance):
##        self.amont=amont
##        self.balance=balance
##    def withdraw(self):
##        if self.amont<=self.balance:
##            self.balance-=self.amont
##            print(f"the balance is {self.balance}")
##        else:
##            print("insufficient balance")
##    def deposit(self):
##         if self.amont>=0:
##            self.balance+=self.amont
##            print(f"the balance is{self.balance}")
##         else:
##            print("invalid amont")
##            
##obj=cal(200,1000)
##print(f"the balance is {self.balance}",obj.withdraw())
##print(f"the balance is{self.balance}"obj.deposit())


class cal:
    def __init__(self,ac_name,balance=0):
        self.balance=balance
        self.ac_name=ac_name

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return (f"the new balance is{self.balance}")
        else:
            return ("invalid amont")

    def withdraw(self,amount):
        if  amount<=self.balance:
            self.balance-=amount
            return (f"the balance is {self.balance}")
        else:
            return ("insufficient balance")



    
obj=cal("sangavi",5000)
print(obj.withdraw(1000))
print(obj.deposit(2000))

#------------------------------------------------//Inheritance//-------------------------
#----------------------------------------------------------Single Inheritance-----------------
##
##class arth:
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##        self.calc=input("Enter Calculation Function: ")
##    def add(self):
##        if calc=="add":
##            return (f"self.a+self.b")
##        elif calc=="sub":
##            return (f"self.a-self.b")
##        elif calc=="mul":
##            return (f"self.a*self.b")
##        elif calc=="div":
##            return (f"self.a/self.b")
##        else:
##            return ("invalid function")
##
##class adv(arth):
##    def expoA(self):
##        return self.a**2
##    def expoB(self):
##        return self.b**2
##
##a=int(input("Enter Number 1: "))
##b=int(input("Enter Number 2: "))
##obj=arth(a,b)
##print(obj.add())
    
#------------------------------------------------multilevel inheritance-------------------
##
##class arth:
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##    def add(self):
##        return self.a+self.b
##    def sub(self):
##        return self.a-self.b
##class adv_math (arth):
##    def expo(self):
##        return self.a**2
##class sci_math(adv_math):
##    def root(self):
##        return self.b**0.5
##
##obj=adv_math(4,2)
##print(obj.expo())
##obj=sci_math(4,2)
##print(obj.root())


##------------------------------------------------------taskkk-----------------------------------------

##class org:
##    def __init__(self,name,idd,brand):
##        self.name=name
##        self.idd=idd
##        self.brand=brand
##class employee(org):
##    def emp(self):
##        return (f"Employee name is {self.name}")
##class number(employee):
##    def num(self):
##        return (f"Employee ID is{self.idd}")
##class laptop(number):
##    def lap(self):
##        return (f"Allocated Laptop is {self.brand}")
##
##obj=employee("sangavi",12,"lenova")   
##print(obj.emp())
##obj=number("sangavi",12,"lenova")
##print(obj.num())
##obj=laptop("sangavi",12,"lenova")       
##print(obj.lap())
-----------------------------------------------------------------------------------


















        









































