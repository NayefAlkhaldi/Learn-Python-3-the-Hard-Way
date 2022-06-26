import lexicon
import remover

class Room(object):
	
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}
		self.death_texts = {}
		self.help_text = None
		self.lock = True

	def parse_paths(self):
		paths = self.paths
		parsed = []

		for path in paths:
			for letter in path:
				if letter != ' ' and (not letter.isalpha() and not letter.isnumeric()):
					path = path.replace(str(letter), '')

			parsed_path = lexicon.scan(path)
			parsed_path = remover.remove(parsed_path, 'stop')
			parsed.append(parsed_path)

		try:
			count = 0
			for key, value in paths.items():
				paths[str(parsed[count])] = paths[key]
				paths.pop(key)
				count += 1
		except RuntimeError:
			pass
		self.paths = paths
	
	def parse_death_texts(self):
		paths = self.death_texts
		parsed = []

		for path in paths:
			for letter in path:
				if letter != ' ' and (not letter.isalpha() and not letter.isnumeric()):
					path = path.replace(str(letter), '')

			parsed_path = lexicon.scan(path)
			parsed_path = remover.remove(parsed_path, 'stop')
			parsed.append(parsed_path)

		try:
			count = 0
			for key, value in paths.items():
				paths[str(parsed[count])] = paths[key]
				paths.pop(key)
				count += 1
		except RuntimeError:
			pass
		
		self.death_texts = paths

	def go(self, direction):
		return self.paths.get(direction, None)

	def add_paths(self, paths):
		self.paths.update(paths)
	
	def add_death_texts(self, text):
		self.death_texts.update(text)

	def add_help_text(self, text):
		self.help_text = text
	
	def remove_path(self, path):
		self.paths.pop(path)
	
	def remove_death_text(self, death_text):
		self.death_texts = {}
		self.death_texts.update(death_text)
	
	def reset(self):
		self.name = self.name
		self.description = self.description
		self.paths = {}
		self.death_texts = {}
		self.help_text = None
		self.lock = True

central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory, put
it in the bridge, and blow the ship up after getting into an escape pod. 

You're running down the central corridor to the Weapons Armory when a
Gothons jumps out, red scaly skin, dark grimy  teeth, and evil clown
costume flowing around his hate filled body. He has a secret code written
on a paper. He's blocking the door to the Armory and about to pull a
weapon to blast you.
""")


laser_weapon_armory = Room("Laser Weapon Armory", 
"""
Lucky for you they made you learn Gothon insults in  the academy. You
tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur fvgf
nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr. The Gothon stops, tries 
not to laugh, then busts out laughing and can't move. While he's lauging
you run up and shoot him square in Weapon Armory door. 

You do a dive roll into the Weapon Armory, crouch and scan the room for
more Gothons that might be hiding. It's dead quiet, too quiet. You
stand up and run to the far side of the room and find the neutron bomb
in its container. There's a keypad lock on the box and you need the
code to get the bomb out. You If you get the code wrong then the
lock closes forever and you can't get the bomb. The code is 3 digits.

What is written on the paper: ΚΩΔΙΚΌς ΕΊΝΑΙ 3 ΨΗΦΊΑ: ΈΝΑ ΤΡΊΑ ΔΎΟ.
""")



the_bridge = Room("The Bridge", 
"""
The container clocks open the seal breaks, letting gas out. You
grab the neutron bomb and run as fast as you can to the bridge where you
must place it in the right spot.

You brust into the Bridge with the netron destruct bomb under your arm 
and surprise 5 Gothons who are trying to take control of the ship. Each
of them has an even uglier clown costume than the last. They haven't 
pulled their weapons out yet, as they see the active bomb under your arm.
""")


escape_pod = Room("Escape Pod",
"""
You point your blaster at the bomb under your arm and the Gothons put
their hands up and start to sweat. You inch backward to the door, open
it, and then carefully place the bomb on the floor, pointing your 
blaster at it. You then jump back through the door, punch the close
button and blast the lock so the Gothons can't get out. Now that the
bomb is placed you run to the escape pod to get off this tin can. 

You rush through the ship desperately trying to make it to the escape
pod before the whole ship explodes. It seems like hardly any Gothons
are on the ship, so your run is clear of interference. You get to the
chamber with the escape pods, and now need to pick one to take. Some of 
them could be damaged but you don't have time to look. There's 5 pods,
which one do you take? 
""")

the_end_winner = Room("The End",
F"""
You jump into pod 2 and hit the eject button. The pod easily slides out 
into space heading to the planet below. As it flies to the planet, you 
look back and see your ship implode then explode like a bright star, 
taking out the Gothon ship at the same time. You won!
""")


the_end_loser = Room("The End",
"""
You jump into a random pod and hit the eject button. The pod escapes 
out into the void of space, then implodes as the hull ruptures, curshing 
your body into jum jelly.
""")

escape_pod.add_paths({
	'1': the_end_loser,
	'2': the_end_winner,
	'3': the_end_loser,
	'4': the_end_loser,
	'5': the_end_loser
})

escape_pod.parse_paths()

escape_pod.add_help_text("Choose one of the five pods.")

death_text = None

generic_death = Room("death", "You died.")

the_bridge.add_paths({
	'throw the bomb': generic_death,
	'slowly place the bomb': escape_pod
})

the_bridge.parse_paths()

the_bridge.add_help_text("Use the bomb under your arm.")

the_bridge.add_death_texts({
	'throw the bomb': 
"""
In a panic you throw the bomb at the group of Gothons
and make a leap for the door.  Right as you drop it a
Gothon shoots you right in the back killing you.  As
you die you see another Gothon frantically try to
disarm the bomb. You die knowing they will probably
blow up when it goes off.
"""
})

the_bridge.parse_death_texts()

the_bridge.parse_death_texts()

laser_weapon_armory.add_paths({
	'132': the_bridge,
	'incorrect': generic_death
})

laser_weapon_armory.parse_paths()

laser_weapon_armory.add_help_text("The paper written in Greek language, so try to figure out what it's saying..")

laser_weapon_armory.add_death_texts({
	'incorrect':
"""
The lock buzzes one last time and then you hear a
sickening melting sound as the mechanism is fused
together.  You decide to sit there, and finally the
Gothons blow up the ship from their ship and you die.
"""
})

laser_weapon_armory.parse_death_texts()

central_corridor.add_paths({
	'shoot!': generic_death,
	'dodge!': generic_death,
	'tell a joke': laser_weapon_armory
})

central_corridor.add_help_text("How about making him laugh?")

central_corridor.parse_paths()

central_corridor.add_death_texts({
	'shoot!':
"""
Quick on the draw you yank out your blaster and fire
it at the Gothon.  His clown costume is flowing and
moving around his body, which throws off your aim.
Your laser hits his costume but misses him entirely.
This completely ruins his brand new costume his mother
bought him, which makes him fly into an insane rage
blast you repeatedly in the face until you are
dead. Then he eats you.
""",

	'dodge!': 
"""
Like a world class boxer you dodge, weave, slip and
slide right as the Gothon's blaster cranks a laser
past your head. In the middle of your artful dodge
your foot slips and you bang your head on the metal
wall and pass out.  You wake up shortly after only to
die as the Gothon stomps on your head and eats you.
"""
})

START = 'central_corridor'

def load_room(name):
	"""
	There is a pontential security problem here.
	Who gets to set name? Can that expose a variable?
	"""
	return globals().get(name)

def name_room(room):
	"""
	Same possible security problem. Can you trust room?
	What's a better solution than this globals lookup?
	"""
	for key, value in globals().items():
		if value == room:
			return key