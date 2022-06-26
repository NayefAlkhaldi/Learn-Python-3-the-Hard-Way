print("""You enter a dark room with three doors.
Do you go through door #1 or door #2 or door #3?""")
door = input("> ")

if door == "1":
	print("There's a giant bear eating a cheese cake")
	print("What do you do?")
	print("1. Take the cake.")
	print("2. Scream at the bear")
	print("3. Try to kill the bear")

	bear = input("> ")

	if bear == "1":
		print("The bear eats your face off. Good job!")
	elif bear == "2":
		print("The bear eats your legs off. Good job!")
	elif bear == "3":
		print("The bear cuts your head off. Good job!")
	else:
		print(f"Well, doing {bear} is probably better")
		print("Bear runs away.")

elif door == "2":
	print("You stare into the endless abyss at Cuthulhu's retina.")
	print("1. Blueberries")
	print("2. Yellow jacket clothespins.")
	print("3. Understanding revovers yelling meldoies.")

	insanity = input("> ")

	if insanity == "1" or insanity == "2":
		print("Your body survives powerd by a mind of jello.")
		print("Good job!")
	else:
		print("The insanity rots your eyes into a pool of muck")
		print("Good job!")

elif door == "3":
    print("There's a dracula sucking somebody blood.")
    print("1. Kill him with a gun.")
    print("2. Run away.")
    print("3. Do 'nothin.")

    action = input("> ")

    if action == "1":
        print("You killed him. Good job!")

    elif action == "2" or "3":
        print("He got crazy and sucked all of your blood. Good job!")

    else:
        print(f"Will, doing {action} is probarly better.")
        print("Dracula runs away.")

else:
	print("You stumble around and fall on a knifee and die. Good job!")