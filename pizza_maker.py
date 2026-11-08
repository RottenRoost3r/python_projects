crusts = ['thin', 'deep', 'regular', 'stuffed']
toppings = ['pepperoni', 'sausage', 'ham', 'olives', 'mushrooms']

print ("lets make a pizza...")
print ("what kind of crust do you want?")

while True:
	for item in crusts:
		print (item)
	c_choice = input("what kind of crust do you want?")
	if c_choice != "thin" or "deep" or "regular" or "stuffed":
		print ("hey, that's not on the list")
	else:
break



for item in toppings:
	print (item)
t_choice = input("please pick one topping")

print ("so that's,",c_choice,"crust, and ",t_choice,"on top")

