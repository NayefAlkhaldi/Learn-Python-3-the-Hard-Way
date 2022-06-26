from sys import argv

script, username = argv


def home():
    """ The story. """
    print("Muffled noises wake you up in the middle of the night.")
    print("Someone is trying to get into your home.")
    print("The issue that you live in the woods, no one can assist you.")
    print("You three choices. Type 1 or 2 or 3:\n")

    print("1. Hide in the closet.")
    print("2. Take a gun and face him.")
    print("3. Act like you're sleeping.\n")

    """ Here's where we'll take the user input to take decisions."""
    action = input("> ")

    """User has 3 choices."""
    if action in ['1', '3']:
        dead("You hear steps on the floor until the bear eats you.")

    elif action == "2":
        print("You slowly sneaked until you saw a bear eating the honey on the table.")
        print("The bear goes insane and tries to attack you.")
        print("The bear tries to smash your face but fails.")
        print("Your turn now.\n")
        print("1- Smash.")
        print("2. Run.")
        print("3. Kick him.\n")

        attack = input("> ")

        if attack in ['1', '3']:
            print("The bear gets dizzy and fall to the ground.")
            """ if user chose the write answer. """
            outdoor()

        else:
            """ Here's where we call the function dead."""
            dead("The bear tries smashes your face and you get dizzy and died.")


def outdoor():
    print("You got out of your house and noticed that your house is on fire. Who did that?\n")
    print("You must find fire extinguisher quickly or the forest will all burn!")
    print("There's 3 places. You're not sure where did you put the fire extinguisher. You can only guess 2 times.\n")
    print("1. The store.")
    print("2. In the kitchen.")
    print("3. Balcony.\n")
    """ The user only have 2 guesses to guess where the fire extinguisher is."""
    guesses = 2

    while True:
        """ What's going on here? It's a loop. The loop reads this block everytime he finshed reading it. 
        It's like a cycle. So if a True value here detected then dead function will be called."""
        if guesses == 0:
            dead("Your house and the whole place burned.")

        choice = input("> ")

        if choice == "1":
            print("The store has nothing.\n")
            guesses -= 1

        elif choice == "2":
            break

        elif choice == "3":
            print("There's nothing in Balcony.\n")
            guesses -= 1

    win("Correct! After that, you took the fire extinguished and you put out the hole fire.\n")


def dead(reason):
    print(reason, "You kinda suck at this.\n")
    exit(0)


def win(how):
    print(how, "Good job!\n")
    save()
    with open(
            "C:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard "
            "Way\\Exercise 36. Designing and Debugging\\Game\\saving.txt", 
            'r') as file_1:
        wins = int(file_1.read())
        print("Winning times: {}".format(wins))
        file_1.close()


def save():
    with open(
            "C:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard "
            "Way\\Exercise 36. Designing and Debugging\\Game\\saving.txt", 
            'r') as file_1:
        wins = int(file_1.read())
        wins += 1
        file_1.close()
        with open(
                "C:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard "
                "Way\\Exercise 36. Designing and Debugging\\Game\\saving.txt", 
                'w') as file_2:
            file_2.write(str(wins))
            file_2.close()

def start():
    return home()


""" That means if the file is the main, then run the function start. """
if __name__ == '__main__':
    print(f"Enjoy playing game, {username}!\n\n")
    start()