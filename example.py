print("hello")
print("1+2")
print(1+2)
a = 1 + 2
print (a)
b = False
print (b)
if b == True:
	print("b is so true")
else:
	print("not true")
c = 7
if c < 7:
	print("so little")
elif c ==7:
	print ("well it's 7")
else:
	print("it's a big number")
first_name = "Isabel"
if first_name == "Griselda":
	print ("Hola")
elif first_name == "Isabel":
	print ("Ola")
else:
	print ("Hello")
l = [1, 2, 3, 4]
print (l)
msg = "my list is {0}".format(l)
print (msg)
# Define a function
def welcome (name, age, country):
	msg = "My name is {0}, I'm {1}, and I come from {2}".format (name, age, country)
	print (msg)
#Call a function
welcome("Griselda", "24", "Spain")
welcome("Isabel", "25", "Portugal")
welcome("Balazs", "27", "Hungary")
def add (num1, num2):
	result = num1 + num2
	print (result)

add ("Yes", "No")

# What does a function
# - return something
# / do a side effect
result = (2 + 3)
print (result)
print (2+3)



















