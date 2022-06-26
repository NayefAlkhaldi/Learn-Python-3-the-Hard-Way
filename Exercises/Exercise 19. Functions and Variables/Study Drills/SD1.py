def cheese_and_crackers(cheese_count, boxes_of_crackers): # The function cheese_and_crackers has two arguments. Cheese_count and boxes_of_crackers.
	print(f"You have {cheese_count} cheeses!") # we printed here cheese_count argument.
	print(f"You have {boxes_of_crackers} boxes of crackers!") # here also.
	print("Man that's enough for a party!")
	print("Get a blanket.\n")


print("We can just give the function numbers directly:")
# We call cheese_and_crackers function with two numbers. 20 and 30.
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
# We have here two variables.
amount_of_cheese = 10
amount_of_crackers = 50

# We call here cheese_and_crackers function with the two variables.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# The same thing here.
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math")
# We call here cheese_and_crackers function. But this time with amount_of_cheese and amount_of_crackers.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)