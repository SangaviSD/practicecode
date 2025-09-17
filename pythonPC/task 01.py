##def fun(b):
##    while b<=50:
##        print(b)
##        b+=1
##fun (1)

        
##def fun(num):
##    while num<=100:
##        if num%2==0:
##            print(num,end=" ")
##            num+=1
##        else:
##            num+=1
##fun(1)

##def fun(num):
##    while num<=100:
##        if num%2==0:
##            print(num,end=" ")
##        num+=1
##
##fun(1)

##def sum1(n):
##    total = 0
##    i = 1
##    while i <= n:
##        total += i
##        i += 1
##    return total
##
##print("Sum =", sum1(5))

##def reverse(n):
##    while n > 0:
##        print(n, end=" ")
##        n -= 1
##
##reverse(10)


##def count1(num):
##    count = 0
##    while num > 0:
##        count += 1
##        num //= 10
##    return count
##
##print("Digits =", count1(98765))

##def count1(num):
##    count = 0
##    while num > 0:
##        count += 1
##        num //= 10
##    return count
##
##print("Digits =", count1(98765))


##for i in range(5,0,-1):
##    print("*"*i)

##for i in range (1,5):
##    print ()
##    for j in range (1,i+1):
##        print (j,end="")
##
##for i in range (1,5):
##    print ()
##    for j in range (1,i+1):
##        print ("*",end="")


##------------------------------pattern---------------------

##n=5
##for i in range(n):    # print n number of star
##    print("*")

##for i in range(5):     # right angle triangle
##    print("*"*i)

##for i in range(5,0,-1):        # reverse triangle
##    print("*"*i)

##for i in range (1,5):
##    print ()
##    for j in range (1,i+1):          # number triangle pattern
##        print (j,end="")

##for i in range (5):
##    print ()                                      #print reverse triangle with nested loop
##    for j in range (i,5):
##        print ("*",end="")
##
##rows = 5
##for i in range(rows, 0, -1):            # start from rows → 1
##    for j in range(i):                      # print i stars
##        print("*", end=" ")
##    print()  # new line


##for i in range (5):                                 #print triangle with nested loop
##    for j in range (i-1):
##        print ("*",end=" ")
##    print()

##n=5
##for i in range(n):                   # print square pattern 
##    for j in range(n):
##        print("*", end="  ")                 # extra space in end will give space bettwen value printed
##    print()                                                # want to give print() so after finishing each loop it will print in order
##       
##
##n=6
##for i in range(n):                   # print y-axis rectangle pattern 
##    for j in range(4):
##        print("*", end="")                 # extra space in end will give space bettwen value printed
##    print()
##
##
##
##n=3
##for i in range(n):                   # print  x-axis rectangle pattern 
##    for j in range(8):
##        print("*", end="")                 # extra space in end will give space bettwen value printed
##    print()


##n=5
##for i in range(n):
##    for j in range(i,n):                      #left angle triangle 
##        print(" ",end=" ")
##    for j in range(i+1):
##        print("*",end="")
##    print()
##
##
##n=5
##for i in range(n):
##    for j in range(i+1):                      #reversed left angle triangle
##        print(" ",end=" ")
##    for j in range(i,n):
##        print("*",end="")
##    print()


##n=5
##for i in range(n):
##    for j in range(i,n):                      #hill pattern
##        print(" ",end=" ")
##    for j in range(i):
##        print("*",end=" ")
##    for j in range(i+1):
##        print("*",end=" ")
##    print()


##n=5
##for i in range(n):
##     for j in range(i+1):                      # reverse hill pattern
##        print(" ",end=" ")
##     for j in range(i,n-1):
##        print("*",end=" ")
##     for j in range(i,n):
##        print("*",end=" ")
##     print()



n=5
for i in range(n-1):
    for j in range(i,n):                      
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
     for j in range(i+1):                      # dimond 
        print(" ",end=" ")
     for j in range(i,n-1):
        print("*",end=" ")
     for j in range(i,n):
        print("*",end=" ")
     print()

    

n=5
for i in range(n-1):
     for j in range(i+1):                      #  reversed dimond 
        print(" ",end=" ")
     for j in range(i,n-1):
        print("*",end=" ")
     for j in range(i,n):
        print("*",end=" ")
     print()
for i in range(n):
    for j in range(i,n):                      
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

















