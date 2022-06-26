# This code will make a compration between people and cars and trucks
people = 30 # A variable that has a value of an integer number. 30
cars = 40 # A variable that has a value of an integer number. 40
trucks = 15  # A variable that has a value of an integer number. 15

if cars > people: # if cars is greater than people...
	print("We should take the car") # print this
elif cars < people: # if not. If cars is less than people...
	print("We should not take the car") # print this
else: # else, do that
	print("We can't decide") # print this text

if trucks >= cars: # if trucks greater than or equal to cars...
	print("That's too many trucks") # print this text
elif trucks < cars: # if not. if trucks is smaller than cars or cars is greater than trucks...
	print("Maybe we code take the trucks") # print this text
else: # else, do that
	print("We still can't decide") # print this

if people > trucks: # if people is greater than trucks...
	print("Alright, let's just take the trucks") # print this
else: # lese: do that
	print("Fine, let's stay home then.") # print this
# Done!