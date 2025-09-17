##------------------------------------------sequential data types------------------------------
##------------------------------------------------listt------------------------------------------------
##inbuilt function

##list1=[1,2,3,4,5,6,4]
##print(list1)
##print(len(list1))
##print(min(list1))
##print(max(list1))
##print(sum(list1))
##print(sorted(list1))

##-----------------------------------indexing-----------------------------------------------

##print(list1[4])
##print(list1[-2])

##-------------------------------------slicing----------------------------

##print(list1[1:])
##print(list1[:3])
##print(list1[1:4])
##print(list1[-1:])
##print(list1[:-4])
##print(list1[-4:-1])

####-------------------------------------------------list operation---------------------------------------------------
##---------------------------------------append/ insert/ extend / remove /pop--------------------------------------------

##list1.append(5)
##print(list1)

##list1.insert(0,1)                     ##insert through indexing 
##print(list1)

##list1.extend([9,10,11])
##print(list1)
##
##list1.remove(1)                   ##only remove the one value specified in this
##print(list1)
##
##list1.pop(2)                         ##to remove through indexing
##list1.pop()                          ## to remove last value
##print(list1)
##
##-------------------------------------------------tuple---------------------------------

##tuple2=(2,3,4,5,7,1)
##print(tuple2)
##print(len(tuple2))
##print(max(tuple2))
##print(min(tuple2))
##print(sorted(tuple2))                 #if sorted change in to [] brackets
##print(sum(tuple2))

##---------------------------------------------------------set------------------------------

##set1={2,3,7,1,9}
##print(set1)
##a={1,7,4,0,2,7}
##b={2,8,4,1,7,4,9}
##print(a.union(b))                            #a union (print all of a and b)
##print(a|b)
##print(a.intersection(b))                  #a intersection (same in both)
##print(a&b)
##print(a-b)
##print(b-a)

##-----------------------------------------------dictionary-------------------------------------

##list2=["orange","guava","kiwi"]
##dict1=dict.fromkeys(list2)                         #convert list into dict key 
##print(dict1)
##dict1["orange"]="orange"
##dict1["guava"]="green"
##dict1["kiwi"]="green"
##print(dict1)
##print(dict1.keys())                              #to print the keys only
##print(dict1.values())                           #to print the values only
##print(dict1.items())
##dict1.popitem()                                     #remove last item from the dict
##print(dict1)

##-----------------------------------------convertion---------------------------

##list3=[1,2,3,3,4,4,4,9]                    #convert list to set to eliminate duplicate
##set2=(set(list3))
##print(set2)
##list5=(list(set2))                            #convert set back to list 
##print(list5)

##---------------------------------------taskk--------------------------------------------

##today=(3,9,2025)
##date=list(today)
##tommorrow=date[0]+1,date[1],date[2]
##print("Today date: ",today)
##print("Tommorrow Date; ",tommorrow)


##today=str(input("enter today date :"))
##date=list(today)
##tommorrow=date[0]+1,date[1],date[2]
##print("Today date: ",today)
##print("Tommorrow Date; ",tommorrow)
          
##------------------------------------------looping---------------------------------
##-----------------------------------for loop----------------------------

##for i in range(1,11):
##    print(i)

##for i in range(0,10,3):                   #(start,stop,step)
##    print(i)
##
##for j in range(20,-10,-2):              #(print in reverse)
##    print(j)

##for a in range(75,49,-1):
##    print(a)
##
##for a in range(50,76,1):
##    print(a)

##word="sangavi"
##for i in word:
##    print(i)
##
##list1=[]
##for i in range(20,30,1):
##    list1.append(i)
##print(list1)

##list1=[]
##list2=[]
##for i in range(20,30,1):
##    if i%2==0:
##        list1.append(i)
##    else:
##        list2.append(i)
##print(list1)
##print(list2)

##--------------------------------------------------task---------------------
##my_list=[1,4,7,8,3]
##a=0
##for i in  my_list:
##    a=a+i                          ###assesment operator(a+=i)
##print(a)
##
##
##my_list=[1,4,7,8,3]
##a=0
##for i in range():                              ##errorrr
##    my_list.append(i)
##    a=a+i
##print(a)

##my_list=[1,4,7,8,3]
##a=1
##for i in  my_list:
##    a=a*i                          ###assesment operator(a+=i)
##print(a)
##
##my_list=["p","y","t","h","o","n"]
##word=""                                             ##empty var so we can add with concadenation
##for i in my_list:
##    word=word+i
##print(word)

##word="battle"
##a=0
##for i in word:
##    if i=="t":
##        a=a+1
##print(a)
        

##for i in range(3):
##    if i<3-1:
##        print("*")
##    else:
##        print("*"*3)
##
##--------------------------------------------------------------------------------------------
##

##for i in range(10):
##    if i==7:
##       break
##    print(i)
##
##for i in range(10):
##    if i==7:
##        continue
##    print(i)

##for i in range(10):
##    if i==7:
##        pass
##print("seven")
##        
##for i in range(10):
##    if i==7:                          
##        print("seven")
##    else:
##        print(i)

##-----------------------------------------------------whilee loop-------------------------

##num=20
##while num<=30:
##    print(num)
##    num+=1

##num=0
##while num<=20:
##     num+=2
##     print(num)

##num=20
##while True:
##    if num==30:
##        break
##    num+=1
##    print(num)

##num=20
##while True:
##    if num==30:
##        break
##    print(num)
##    num+=2

##num=1
##word="python"
##while num<=5:
##    print(word,"is",num)
##    num+=1

##num=1
##while num<=10:
##    print("5*",num,"=",num*5)
##    num+=1

##----------------------------------------------------------------------task------------------------

##num=1
##while num<=50:
##    if num%5==0:
##        num+=1
##        continue
##    print(num)
##    num+=1


##
##
##
##n=int(input("enter the number:"))
##num=1
##i=1
##while i<=n:                                    #factorial
##    num=num*i
##    i+=1
##print(num)


##a=int(input("enter the number:"))
##num=0
##i=1
##while i<=a:
##    num=num+i
##    i+=1
##print(num)


    












