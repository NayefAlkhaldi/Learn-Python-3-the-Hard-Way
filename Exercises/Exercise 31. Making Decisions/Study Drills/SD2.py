print("You are lost, it's night now, Someone is following you.\nWhat should you do?\n")

print("1. Run as fast as you can\n")
print("2. Ask him about what he wants\n")
print("3. Call police\n")
print("4. Stay calm and continue walking...\n")
print("5. Try to hide from him\n")

answer = input("> ")

if answer == '1':
	print('You are running')
	print('but he is faster than you.\nHe catchs you and kills you with a knife.')
	print("You died!")

elif answer == '2':
	print("You are saying loudly: what do you want from me?!")
	print("But...", end='')
	print("He is laughing...\n")
	print("*Shoots you*")

elif answer == '3':
	print("He looks afraid???")
	print("*Shoots you*")
	print("You died!")

elif answer == '4':
	print("You are walking now, but he still following you.")
	print("Accidentally, you saw a taxi... you have enough money to take a ride")
	print("You Win!")

elif answer == '5':
	hide = input("You saw a hunted house... would you hide in? (yes, no)")

	if hide =='yes':
		print("He is trying to find you. It's been many hours and you are not sure if he is gone...")
		leave = input("Would you leave the hunted house, yes or no? ")

		if leave == 'yes':
			print("Oh No.. He tricked you!")
			print("*Kills you with a knife*")
			print("You died!")
	
		else:
			leave_c = input("You stayed one hour more, should you leave? (yes or no)? ")

			if leave_c == 'yes':
				print("He is gone...")
				print("You Win!")

			else:
				print("You have stayed more than 5 hours, and a poisonous snake bites you...")
				print("You died!")
	else:
		print("Great job.. you've moved a lot away from people and from the known ways. You're now at a strange street and he has a chance to kill you.")
		print("*Shoots you with a gun*")
		print("You died!")

else:
	print(f"What do you mean by '{answer}'?\n")
	exit()