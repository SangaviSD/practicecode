##1. Write a Python program to print the following string in a specific format (see the output).
##Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
##Output :
##
##Twinkle, twinkle, little star,
##	How I wonder what you are! 
##		Up above the world so high,   		
##		Like a diamond in the sky. 
##Twinkle, twinkle, little star, 
##	How I wonder what you are
##	
##2. Leap Year: Write a program that takes a year as input and determines if it is a leap year. A leap year is divisible by 4, except for century years (those ending in 00), which must be divisible by 400.
##
##3.Positive, Negative, or Zero: Write a program that takes an integer as input and prints whether the number is positive, negative, or zero.
##
##4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
##Sample Output :
##r = 1.1
##Area = 3.8013271108436504
##
##5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
##
##6. Largest of Three Numbers: Write a program that takes three numbers as input and prints the largest of the three.
##
##7. Write a Python program that accepts a filename from the user and prints the extension of the file.
##Sample filename : abc.java
##Output : java
##
##8. Write a Python program to display the first and last colors from the following list.
##color_list = ["Red","Green","White" ,"Black"]
##
##9. Ticket Price: A movie theater charges different prices based on age:
##
##Children (under 12): $5
##
##Teens (12-17): $10
##
##Adults (18-64): $15
##
##Seniors (65 and over): $10
##
##10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
##Sample value of n is 5
####Expected Result : 615
##
##
##
##-------------------------------------------------------1 answer-------------------------------------------


##text='''Twinkle, twinkle, little star,
##	How I wonder what you are! 
##		Up above the world so high,   		
##		Like a diamond in the sky. 
##Twinkle, twinkle, little star, 
##	How I wonder what you are.'''
##print(text)


##--------------------------------------------3  answer-------------------------------------

##num=int(input("Enter the Number:  "))
##if num>0:
##    print("the number is positive")
##elif num<0:
##    print("the number is negative")
##else:
##    print ("the number is zero")

##------------------------------------------8 answer------------------------------------------
##
##color_list = ["Red","Green","White" ,"Black"]
##print(color_list[0])
##print(color_list[3])
##
##-----------------------------------------------------------


##year=int(input("enter the year: "))
##if year%4 ==0:
##    print("the year is leap year")
##elif year%400==0:
##    print("the year is leap year")
##else:
##    print("not a leap year")
##
##--------------------------------------------------------------

n=5
sum=n+n*n+n*n**n
print(sum)
