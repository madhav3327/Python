# 	•	Definition:
# A set is a collection of unique items (no duplicates allowed).
#  Sets are unordered, meaning the items don’t have a specific position.
# Example: my_set = {1, 2, 3, "apple"}

# 5 Problems on Sets:
# 	1.	Create a set with 5 unique numbers and print it.
# 	2.	Add two new numbers to the set.
# 	3.	Remove one number from the set.
# 	4.	Check if a specific number exists in the set.
# 	5.	Find the union and intersection of two sets.

#1.
set1={1,2,3,4,5}
print(set1)
set2={1,4,2,3,6}
print(set2)

#2.
set1.add(8)
set1.add(12)
print(set1)

#3.
set1.pop()
print(set1)

set1.remove(4)
print(set1)

#4.
specific=8
if(specific in set1):
    print(f'true {specific}  exists')
    
else:
    print(f'no {specific} doesnt exists')

set2={2,4,5}
print(set1.union(set2))
print(set1.intersection(set2))