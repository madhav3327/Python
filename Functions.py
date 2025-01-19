# 3. Functions

# Definition: Functions are reusable blocks of code defined using the def keyword, designed to perform specific tasks.
# so, If you think there is a block of code that we want to use it again and again then we will make this a function and every time we call it it works.

# Questions:
# 	1.	Write a function to calculate the sum of two numbers.
# 	2.	How do you return multiple values from a Python function?
# 	3.	Write a function to check if a string is a palindrome.
# 	4.	Create a function with default arguments and explain how it works.
# 	5.	Write a lambda function to calculate the square of a number.

#1.

def sum(num1, num2):
    return num1+num2

# num1= int(input("Enter first number"))
# num2= int(input("Enter second number"))
num1=23
num2=34
result= sum(num1, num2);
print("the result of those numbers is "+ str(result))

#2.

# num3= int(input("Enter first number"))
# num4= int(input("Enter second number"))

num3=34
num4=45
def arith(num3, num4):
    
    add=num3+num4
    sub=num3-num4
    mul=num3*num4
    div=num3/num4
    dict ={"addition":add, "subtraction":sub, "multiplication":mul,"division":div}
    return dict

answer = arith(num3, num4);
print(answer)

#3.

data = "Madhav"
print(data[0])

def ispalindrom(msg):
    n=len(msg)
    print(n)
    i=0
    while(True):
       if(msg[n]!=msg[i]):
        return False
       elif(n<=i):
        return True
       n=n-1
       i=i+1 

result=ispalindrom(data);
print(result)
        
