# 2. Control Flow (if-else, loops)

# Definition: Control flow statements like if, for, and while control the execution of code based on conditions or iteration.
# If is used to check whether a condition is true or not where are fro and while are used to repeat few statments again and again

# Questions:
# 	1.	Write a program to check if a number is positive, negative, or zero.
# 	2.	Write a loop to print all even numbers between 1 and 20.
# 	3.	Use a while loop to calculate the factorial of a number.
# 	4.	Write a program that breaks out of a loop if a condition is met.
# 	5.	What is the difference between if-elif-else and nested if?

#1. 
# num = int(input("Enter a number"))
num = 34
if(num>0):
    print(str(num) + " is a Positive number")
elif(num<0):
    print(str(num) + " is a Negative number")
else:
    print(str(num) + " is a Zero")


#2. 
even =[]
for x in range(2,21,2):
    even.append(x)
print(even)

#3.
num =5
fact=1
while num>1:
    fact=fact * num
    num-=1
print("factorial of given number :"+ str(fact))

#4.
#lets break if a numbner divided by 10 from number starting for 1

for x in range(1,50):
    if x%10==0:
        break
    else:
        print(x)


#5.
#both are for condition checking but in different senarios
#if you want to check for one condition out of 3 you can go for if elif els
#but if you want to check for conditions which are depended on each thn we go for nested if
# for example if i ask a person to choose a number and to check whether the number is even or odd i can go for if elif else
# because i can compare with even if yes my job is done if not then i need to check it with off which here is elif
# but if i ask a person to choose a bag and then a number now my seneario is different
# first i need to check the color of bag which he picked then i need to go for another condition 
# so its nested after this is true we check for another condition to be true