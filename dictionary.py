# 4. Dictionary
# 	•	Definition:
# A dictionary stores data in key-value pairs, where each key is unique. 
# It’s like a real dictionary where you look up a word (key) to find its meaning (value).
# Example: my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# 5 Problems on Dictionaries:
# 	1.	Create a dictionary with your name, age, and favorite color.
# 	2.	Add a new key-value pair for your favorite hobby.
# 	3.	Update the value of the “age” key in the dictionary.
# 	4.	Remove the “city” key from the dictionary.
# 	5.	Print all the keys and values separately.

#1.
bio={"name":"Bhavana","age":26,"color":"blue"}
bio["hobby"]={"reading":"storybooks","watching":"telugu movies","arts":"clay arts"}
bio["age"]=27
bio["city"]="hyd"
print(bio)

bio.pop("city")
print(bio)

print(bio.keys())
print(bio.values())


