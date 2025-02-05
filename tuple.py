# 2. Tuple
# 	•	Definition:
# A tuple is similar to a list, but it cannot be changed (immutable). 
# Once you create a tuple, its values remain fixed.
#  Tuples are useful for data that should not be modified.
# Example: my_tuple = (1, 2, "apple", True)

# 5 Problems on Tuples:
# 	1.	Create a tuple with 5 items and print each item using a loop.
# 	2.	Access the second and fourth items of the tuple.
# 	3.	Try to add an item to the tuple and observe the error.
# 	4.	Convert the tuple into a list, add a new item, and convert it back to a tuple.
# 	5.	Find the length of a tuple.

#1.
fruits=("apple","mango","banana","guava","kiwi")
print(fruits)

print(fruits[1],fruits[3])

# fruits.append("cherry")

templist= list(fruits)
print(fruits)
print(templist)
templist.append("cherry")
fruits=tuple(templist)
print(fruits)

print(len(fruits))




