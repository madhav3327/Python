#varibales are boxes or containers to store data



firstname="bhavana"
age=26
gender ="female"
phone=1234567890

#Hi bhavana i think your age is 26 and you are female and i got your number which is 1234567890
print("Hi bhavana i think your age is 26 and you are female and i got your number which is 1234567890")

print("Hi "+firstname+" i think your age is "+str(age)+" and you are "+gender+" and i got your number which is "+str(phone))
print(f'Hi {firstname} i think your age is {str(age)} and you are {gender} and i got your number which is {str(phone)}')

# String, int , float, boolen, 
name="madhav"
age=26
gpa=3.8
ispass=True

print(type(name))
print(type(age))
print(type(gpa))
print(type(ispass))


# A company is planning to distribute bonuses to its employees based on their performance. 
# Each employee has a performance score (out of 100), and the bonus amount depends on the score and their salary. 
# Here’s the formula:
# 	•	If the score is 90 or above, they receive a bonus of 20% of their salary.
	# If the score is between 70 and 89, they receive a bonus of 15% of their salary.
# If the score is between 50 and 69, they receive a bonus of 10% of their salary.



score = int(input("what is the score of this employee"))


if(score>=90):
    salary=int(input("what is the salary"))
    bonus=(salary*20)/100
    total=bonus+salary
    print(f'you will get a bonus of amount {bonus} and your account will be credited with {total}')
elif(score>=70 and score <=89):
    salary=int(input("what is the salary"))
    bonus=(salary*15)/100
    total=bonus+salary
    print(f'you will get a bonus of amount {bonus} and your account will be credited with {total}')
elif(score>=50 and score <=69):
    salary=int(input("what is the salary"))
    bonus=(salary*10)/100
    total=bonus+salary
    print(f'you will get a bonus of amount {bonus} and your account will be credited with {total}')
else:
    print("sorry you dont have any bonus")