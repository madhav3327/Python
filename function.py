# grinder(list of stuff)
# instruxrtion
# washer(items)



# biryani start

# 1.washer(rice)
# 2.soak rice
# 3.washer(chicken)
# 4.marinate
# 5.grinder(mirchiu, garlic,ginger)
# 6.oil heat
# 7.chicken fry
# 8.grinder(spices)
# biryani done


Students=["madhav","kushal","bhavana"]
products=["mobiles","books","dress"]
prices=[30000,5000,16000]
Discounts=[10,5,8]

def dis(price,discount):
    result=(price/100)*discount
    return result

dis(prices[0],Discounts[0])
#madhav bought mobiles of worth 300000 and got discount of 3000

print(Students[0])
print(products[0])
print(prices[0])
res=dis(prices[0],Discounts[0]);

print(Students[0])
print(products[0])
print(prices[0])
res=(prices[0]*Discounts[0])/100

print(Students[0])
print(products[0])
print(prices[0])
res=(prices[0]*Discounts[0])/100

print(f'{Students[0]} bought {products[0]} of worht {prices[0]} and got a discount of {dis(prices[0],Discounts[0])}')
print(f'{Students[1]} bought {products[1]} of worht {prices[1]} and got a discount of {dis(prices[1],Discounts[1])}')
print(f'{Students[2]} bought {products[2]} of worht {prices[2]} and got a discount of {dis(prices[1],Discounts[2])}')


def Cal(a,b):
    print(a+b)
    print(a-b)
    print(a*b)

num1=23
num2=45
Cal(num1,num2)

num3=89
num4=78
Cal(num3,num4)




#hey madhav how you are doing!
def greet(name):
    print(f'Hey {name} how are you doing!')

greet("madhav")
greet("bhavana")
print("/sdjnksdnb")
print("sdkjcbskdb")

greet("chikky")

