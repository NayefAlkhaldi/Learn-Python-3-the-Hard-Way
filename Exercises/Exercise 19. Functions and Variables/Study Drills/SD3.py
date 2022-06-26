def coffee_and_biscuits(amount_of_cups, amount_of_biscuits):

	packs = amount_of_biscuits // 10
	print(f"We have {amount_of_cups} cups of coffee and {round(packs)} packs of biscuits.")
	print(f"That's enough for {amount_of_cups} people.")
	print(f"But {abs(amount_of_cups - packs)} won't get coffee and pack of biscuite together.\n")


# way 1
coffee_and_biscuits(20, 215)

# way 2
amount_of_cups = 5
amount_of_biscuits = 20
coffee_and_biscuits(amount_of_cups, amount_of_biscuits)

# way 3
coffee_and_biscuits(40 - 23, 300 - 10)

# way 4
cups_fell = 10
cracked_biscuits = 90
coffee_and_biscuits(100 - cups_fell, 320 - cracked_biscuits)

# way 5
coffee_and_biscuits(input("Amount of cups: "), input("Amount of biscuits"))

# way 6
from sys import argv
script, amount_of_biscuits, amount_of_cups = argv
coffee_and_biscuits(amount_of_biscuits, amount_of_cups)

# way 7
from my_module import amount_of_cups, amount_of_biscuits
coffee_and_biscuits(amount_of_cups, amount_of_biscuits)

# way 8
file = open("text.txt", 'r')

# run file
exec(file.read())
coffee_and_biscuits(amount_of_cups, amount_of_biscuits)
file.close()

# way 9
# Octal numebers
amount_of_cups = int("\064\060")
amount_of_biscuits = int("\065\060")
coffee_and_biscuits(amount_of_cups, amount_of_biscuits)

# way 10
amount_of_cups = float(14.5)
amount_of_biscuits = float(405.75)
coffee_and_biscuits(amount_of_cups, amount_of_biscuits)

# Done!