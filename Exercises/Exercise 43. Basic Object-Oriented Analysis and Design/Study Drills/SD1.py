# Mission #49, killing Castaro
from sys import exit
import random
from random import randint
from textwrap import dedent

player = 'Chris'
crew_power = 0
crew = [player]
on_crew = len(crew)
lose = False

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):
    pass


class The_Castle(Scene):

    def enter(self):
        global crew_power
        global crew
        global lose

        names = ['Kristopher', 'Kinvey', 'Harold',
                 'Eclipse', 'Ulises', 'Jaden',
                 'Thaddeus', 'Lia', 'Jeff', 'Markus']
        total_crew = randint(3, 9)

        for total in range(total_crew):
            member = names.pop(randint(0, len(names) - 1))
            crew.append(member)

        crew_2 = {
            player: randint(10, 100)
        }
        for member in crew:
            crew_2[member] = randint(10, 100)

        crew_power += sum(crew_2.values())
        print(crew_2)

        print(dedent("""
The king of Oak-wood have sent you and your battle partners
to assassinate his biggest enemy "Castaro."
The king gave you a bunch of weapons to choose one of them,
which weapon you think it'll be strong to fight with?
"""))

        weapons = {
            '1': 'Halberd',
            '2': 'Bow & Arrow',
            '3': 'Katana Sword',
        }

        player_weapon = input(f"1. {weapons['1']}\n2. {weapons['2']}\n3. {weapons['3']}\n\n> ")

        print(f"You have chosen {weapons[player_weapon]}")
        return 'The_Two_Roads'


class The_Two_Roads(Scene):

    def enter(self):

        def right():
            global lose
            global Death
            print(dedent("""
after 2 hours of walking, you relized that the way was right.
You finally reached the main gate of Castaro's kingdom! 
But there was two monsters guarding the gate.
What shall you do?

1. Attack the guards
2. Find a way to enter
the city without letting the guards notice
"""))

            choice = input("> ")

            if choice == '1':
                power_ranges = {
                    'weak': 135,
                    'middling': 215,
                    'strong': 365
                }
                guards_power = power_ranges[random.choice(power_ranges.keys())]
                if crew_power >= guards_power:
                    print(dedent("""
You fought the guards... And you won the battle!
"""))               
                    return Castaro_City()
                
                else:
                    print(dedent("""
Oh no, the guards was way stronger than you!
"""))        
                    lose = True
                    return game_over()

            elif choice == '2':
                print(dedent("""
You guys are sneaking right now and... someone
stepped on a rock and a sound of crunch came out.
The monster heard the noise and ate all of you.
"""))           
                lose = True
                return game_over()
            else:
                print("Does not compute!\n")
                lose = True
                return game_over()

        def left():
            global lose

            print(dedent("""
While walking in the jungle, you saw a green dwarf.
he green dwarf says: Hi folks! are you looking for Castaro's castle?
"""))

            c1 = input(dedent("""
1. Yes, why are you asking?
2. Get away annoying dwarf or else...
3. ignore him

> """))
            if c1 == '1':
                print(dedent("""

The green dwarf: Good, cause I can help!
But in return for giving me one of your friends souls.
"""))

                give = input("(y/n)> ")

                if give == 'y':
                    print(dedent("""
Green Dwarf: Alright let's do this!

The green dwarf is reading the spell of extracting
Souls. Looks like he's messing with some kind of
black magic stuff...
"""))

                    soul_given = crew.pop(randint(0, len(crew) - 1))

                    if soul_given == player:
                        print(dedent("""
Green Dwarf: Oh no!! you are the
chosen one.\nThe Green dwarf is taking out Your soul.
"""))
                        print(dedent(f"""
Your friend {soul_given} has died.
"""))
                        print(dedent("""
Green Dwarf is opening a weird portal...
Green Dwarf: by going into this portal, you'll reach
Castaro's castle without facing any monsters. Is it amazing?
"""))
                        print("You entered the portal...")

                        return 'Castaro_Castle'
                elif give == 'n':
                    print("The green dwarf went angry and threw a spell on you and you died.")
                    lose = True
                    return game_over()
        
            elif c1 == '2':
                print(dedent("""
Green Dwarf: what would you do, little kid?
The dwarf slaps you on your face and you die.
"""))           
                lose = True
                return game_over()

            elif c1 == '3':
                print(dedent("""
You do didn't give him any interest, and the dwarf went angry.
You continued walking until you saw a river blocking the road
with lots of alligators. You have two choices.
"""))

                action = input(dedent("""
1. jumping on alligators until the end of the river.
2. Fight them.

> """))

                if action == '1':
                    print(dedent("""
You jumped on all alligators. But unluckily one of them
ate your left leg.
"""))               
                    lose = True
                    return game_over()

                elif action == '2':
                    print(dedent("""
You killed all the alligators and the river went red.
You swimmed to the another side and saw the king of alligators.
Crocodile king: What are you doing here?

1. I killed all the alligators.
2. Do you know where is Castaro's castle?
"""))
                    answer = input("> ")
                    if answer == '1':
                        print(dedent("""
The king of alligator went crazy and ate you and
some of your crew. The other ran.
"""))                           
                        lose = True
                        return game_over()
    
                    elif answer == '2':
                        print(dedent("""
King of alligators: yes It's just over there. But be careful
and don't trust anybody. I told you!
"""))
                        input("> ")
                        print(dedent("""
While the adventure, You and your crew really
faced a lot of monsters and some of the crew died.
But finally, you reached Castaro's castle and
the time to fight him.
"""))

        print(dedent("""
The king gave you a map to know where should you go. 
After two hours of walking, and on what the map says
there are two ways, and you must wisely choose one of them.
First is a very long road, you might meet a lot of monsters
and it could make your supplies lack, and it's the only way
to reach Castaro's castle without letting the guards see
you. The second road is short but it faces the gate with
the guards so you have a very little chance to survive.
Both are dangerous. You must choose one direction: (right/left)?
"""))

        road = input("> ")

        if road == 'left':
            left()
            return 'Castaro_City'

        elif road == 'right':
            right()
            return 'Castaro_City'


class Castaro_City(Scene):

    def enter(self):
        global lose
        print(dedent("""
You entered Castaro's city attacking all the monsters
and they were afraid of you until you heard a very loud noise.
everyone was looking at that monster with the three eyes and 
big hands, with two ugly horns over his head, his teeth was
too sharp. Castaro said screaming: who's messing with me?
Castaro attacked you and he was extremely powerful.
But your team won the battle again and justice appears again.
The king of Oak-wood honered you and your crew with a golden swords.
After this incident, everyone lived in peace.
"""))

        return 'finished'



def game_over():
    if lose:
        print('You lose!\n')
        exit()


class Finished(Scene):

    def enter(self):
        print("\nYou won! Good job.")
        return 'finished'


class Map(object):
    scenes = {
        'The_Castle': The_Castle(),
        'The_Two_Roads': The_Two_Roads(),
        'Castaro_City': Castaro_City(),
        'death': game_over(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    @staticmethod
    def next_scene(scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)



a_map = Map('The_Castle')
a_game = Engine(a_map)
a_game.play()