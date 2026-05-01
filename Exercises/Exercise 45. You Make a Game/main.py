from sys import exit
from time import sleep
from random import randint
from random import choice
from ast import literal_eval
from textwrap import dedent

from textcut import cut_line, intext, check_data, write_data



class Entity(object):
    def __init__(self, health, ap): # ap -> attack power
        self.health = health
        self.max_health = health
        self.ap = ap
    
    def attack(self, health):
        damage = round(health - self.ap)
        print(f"YOUR HEALTH: {damage}")
        return damage

    def heal(self, method):
        print(f"ENEMY HEALS BY: {method}..")
        if self.health < self.max_health-self.ap:
            self.health += round(self.ap/2)
        else:
            self.health = self.max_health
        print(f"CURRENT ENEMY'S HEALTH: {self.health}")


class Room(object):
    def scenario(self, scenario): # print scenario
        print(dedent(scenario + '\n'))
    
    def death(self):
        mockeries = [
            "I have a little puppy who is better at this.",
            "What were you thinking?",
            "Can you even use your brain?",
            "Even a two-year-old can beat this game.",
            "You have no common sense."
        ]
        print(dedent("YOU DIED! " + choice(mockeries)))
        input("Wanna play again? If yes, press enter.\n>")
        play()



class level_0(Room):
    def enter(self):
        self.scenario("""\n\n
        You woke up in a dark room with no lights. You don't
        know how you got here. You stand up and see a door with a keypad next
        to it. This looks like the only way to get out of here. The room
        has a narrow window, a fork, and a scrap of paper. What do you do?""")

        code = randint(100, 999)
        door = False # closed

        while True:
            choice = cut_line(input("> "))
            if not door:
                if intext(choice, "read paper", mode='check_all'):
                    self.scenario(f"You grab the paper. It reads: {code}")
                
                elif intext(choice, "take fork", "grab fork", "use fork", mode='check_one'):
                    self.scenario("The fork does nothing.")
                
                elif intext(choice, "open window", mode='check_all'):
                    self.scenario("The window is sealed.")
                
                elif intext(choice, "open door", mode='check_all') and door != True:
                    self.scenario("The door is locked.")
                
                elif intext(choice, "go", "door", mode='check_one'):
                    self.scenario("You stand in front of the door. Perhaps there is a code?")
                
                elif intext(choice, f"enter {code}", f"try {code}", mode='check_one'):
                    self.scenario("The door unlocks.")
                    door = True
                else:
                    self.scenario("That's not something useful you could do right now.")

            elif intext(choice, "go in", "enter", mode='check_one'):
                break
            
            else:
                self.scenario("Just go in. It is unlocked now.")
            
        
class level_1(Room):
    def __init__(self):
        self.inventory = []

    def enter(self):
        self.scenario("""
                You step in and you take a glimpse of a big broken machine that
                looks like a portal. Something tells you to make it work. Howeve-
                r, you need power source, lever, and wires. There are three doors.
                Which door would you take first? 1/2/3""")

        while not unlock:
            unlock = 'wires' in self.inventory and \
                     'power source' in self.inventory and \
                     'lever' in self.inventory

            if not unlock:
                choice = cut_line(input("> "))

            if intext(choice, "1", "one", mode='check_one'):
                if not 'wires' in self.inventory:
                    self.door1()
                else:
                    self.scenario("That's not necessary.")
            
            elif intext(choice, "2", "two", mode='check_one'):
                if not 'lever' in self.inventory:
                    self.door2()
                else:
                    self.scenario("That's not necessary.")
            
            elif intext(choice, "3", "three", mode='check_one'):
                if not 'power source' in self.inventory:
                    self.door3()
                else:
                    self.scenario("That's not necessary.")

            else:
                self.scenario("That's not something useful you could do right now.")

        self.scenario("""You finally go back and assemble all the parts in the machine.
                the machine starts and it teleports you to a room full of holes.
                ***PART 2 COMING SOON...*** THANKS FOR PLAYING!""")

        check_data('ex45 - Room Escape/data.txt')
        write_data('ex45 - Room Escape/data.txt')

        exit(0)

    def door1(self):
        self.scenario("""You enter and see an angry dog chewing on some wires.""")
        while True:
            choice = cut_line(input("> "))
            if intext(choice, "bark", mode='check_one'):
                self.scenario("The dog gets angry and bites your face until it gets distorted.")
                self.death()

            elif intext(choice, "pet", mode='check_one'):
                self.scenario("IT IS NOT FRIENDLY!")

            elif intext(choice, "scream", mode='check_one'):
                self.scenario("He gets scared and runs away. You quickly grab the wires and leave.")
                self.inventory.append('wires')
                break
            
            elif intext(choice, "get out", "exit", mode='check_one'):
                self.scenario("You leave the room.")
                break

            else:
                self.scenario("That's not something useful you could do right now.")
        
    def door2(self):
        self.scenario("""You step in and see a witch and she offers you an apple.""")

        while True:
            choice = cut_line(input("> "))
            if intext(choice, "eat", mode='check_one'):
                self.scenario("You get poisoned and die.")
                self.death()

            elif intext(choice, "punch", mode="check_all") or \
                intext(choice, "kill", mode="check_all"):
                self.scenario("She dies and drops a lever. You take the lever and leave.")
                self.inventory.append('lever')
                break

            elif intext(choice, "flirt", "kiss", mode='check_one'):
                self.scenario("She is an old hag.")

            else:
                self.scenario("That's not necessary.")
            
        
    def door3(self):
        wolf = Entity(scale*100, scale*50)
        self.scenario(f"""
            You step in and see a wolf which is guarding a battery. He notices you and gets
            angry. Wolf's health: {round(wolf.health)}. Your health: {round(player.health)}.""")
        
        sleep(2)

        while player.health > 0:
            attack = choice([True, False])
            if attack:
                player.health -= round(wolf.ap)
                self.scenario(f"""
            Wolf attacks you! Your health: {round(player.health)}""")
                
            else:
                self.scenario(f"""
            Wolf gets scared.""")
    
            move = input("ATTACK/RUN AWAY> ")
            if intext(move, "attack", "punch", mode='check_one'):
                wolf.health -= round(player.ap)
                self.scenario(f"""
                    You attack the wolf with martial arts. Wolf's health: {round(wolf.health) if wolf.health > 0 else 0}""")

                if wolf.health < 0:
                    self.scenario(f"""
                        Wolf has fallen to the ground. You finally get the battery.""")
                    self.inventory.append('power source')
                    break
            elif intext(move, "run", "run away", mode='check_one'):
                self.scenario(f"""The wolf follows you and kills you.""")
                self.death()
            else:
                self.scenario(f"""I don't think that '{move}' is useful right now.""")
                    
        else:
            self.scenario("""You die because of blood loss.""")
            self.death()


def game(mode):
    global scale
    global player

    player = Entity(100, 50)
    levels = {'level 0': level_0(),
              'level 1': level_1()}

    mode_scales = {'easy': 1/3, 'normal': 0.5, 'hard': 1}
    scale = mode_scales[mode]

    levels['level 0'].enter()
    levels['level 1'].enter()


def screen_title():
    check_data('ex45 - Room Escape/data.txt')
    file = open('ex45 - Room Escape/data.txt', 'r')
    data = literal_eval(file.read())
    file.close()

    input(dedent(f"""
        Room Escape all rights reserved © 2026
        Press Enter to start | CTRL+C to exit - Your visits so far: {data['visits']}
        > """))

    while True:
        choice = cut_line(input(dedent("""
            Choose your game mode (E/N/H)
            > """)))

        if intext(choice, "e", "easy", mode="check_one"):
            print("YOU HAVE CHOSEN EASY MODE!")
            choice = 'easy'
            break

        elif intext(choice, "n", "normal", mode="check_one"):
            print("YOU HAVE CHOSEN NORMAL MODE!")
            choice = 'normal'
            break

        elif intext(choice, "h", "hard", mode="check_one"):
            print(f"YOU HAVE CHOSEN HARD MODE!")
            choice = 'hard'
            break

        # if not then ignore 'break' and display this
        print("THAT IS NOT A MODE!")
        sleep(1)

    sleep(2)
    game(choice)

def play():
    try:
        screen_title()
    except KeyboardInterrupt:
        print("\nEXITTING AND SAVING...")
        exit(0)
    
if __name__ == '__main__':  
    play()