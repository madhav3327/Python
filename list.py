# 1. List
# 	•	Definition:
# A list is a collection of items that can hold different types of data. Lists are ordered, 
# meaning the items have a specific position, and they can be changed (mutable).
# Example: my_list = [1, 2, "apple", True]
# 5 Problems on Lists:
# 	1.	Create a list with 5 of your favorite fruits and print them.
# 	2.	Add two more fruits to the list and print the updated list.
# 	3.	Remove the second item from the list and print it.
# 	4.	Sort the list in alphabetical order.
# 	5.	Create a list of numbers and calculate their sum.

#1.
fruits=["apple","mango","banana","guava","kiwi"]
print(fruits)

#2.
fruits.append("pineapple")

fruits.append("orange")
print(fruits)

#3.
temp=fruits.pop(1)
print(temp)
print(fruits)

#4.
fruits.sort()
print(fruits)

num=[12,34,567,4,34,78,65]
temp1=sum(num)
print(max(num))
print(min(num))
print(temp1)
