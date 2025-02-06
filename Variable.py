# 1. Variables and Data Types

# Definition: Variables are containers for storing data values, 
#somthing like we use boxes to store ingredients before using them we name them to identify what is stored inside 
#also we use different size boxes for different ingredients
#similarly we have data types determine the kind of data (e.g., int, float, string) a variable holds.

# Questions:
# 	1.	Create a variable to store your name and print it.
# 	2.	How would you check the data type of a variable in Python?
# 	3.	Convert a string '123' to an integer.
# 	4.	Write code to store 3.14 in a variable and check its type.
# 	5.	What happens if you assign x = '5' and then x = 5?
# making changes from remote
#1.
FirstName = "Sai Madhav"
SecondName = "Rayabandi"
print("your details are \n FirstName : " +FirstName + "\n SecondName : " +SecondName)

#2.
print(type(FirstName))

#3.
ValueOfTypeString = "123"
print(type(ValueOfTypeString))
ValueOfTypeInt= int(ValueOfTypeString)
print(ValueOfTypeInt)
print(type(ValueOfTypeInt))

#4.
FloatVaribale = 3.14
print(FloatVaribale)
print(type(FloatVaribale))

#5.
x= '5'
print(type(x))  #this is of type string
x=5
print(type(x))  #this is of type int
