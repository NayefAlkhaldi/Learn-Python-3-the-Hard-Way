# LOL
people = 12
cars = 12
trucks = 500

if cars >= people:
	print("We should take the car")
elif cars <= people or people != cars and not (people == cars):
	print("We should not take the car")
else:
	print("We can't decide")

# nothing changed. It's same as (if trucks > cars)
if trucks >= cars and trucks != cars:
	print("That's too many trucks")
elif trucks < cars:
	print("Maybe we code take the trucks")
else:
	print("We still can't decide")

if people > trucks:
	print("Alright, let's just take the trucks")
else:
	print("Fine, let's stay home then.")