class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
        self.loved = False
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
        liked = input("Did you like it? ")
    
        if liked.lower() == 'no':
            print("Oh..\n")
            self.loved = False
    
        elif liked.lower() == 'yes':
            print("Glad that you liked it!\n")
            self.loved = True

happy_bday_lyrics = ["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"]

bulls_on_parade_lyrics = ["They rally around the family",
                          "With pockets full of shells"]

old_macdonald_had_a_farm_lyrics = ["Old MacDonald had a farm, E-I-E-I-O",
                                   "And on his farm he had a cow, E-I-E-I-O",
                                   "With a moo-moo here and a moo-moo there",
                                   "Here a moo, there a moo, everywhere a moo-moo"
                                   "Old MacDonald had a farm, E-I-E-I-O."]

apple_rain_lyrics = ["April rain is here again",
                     "Hear it pitter, pitter, patter",
                     "On the leaves and on the trees",
                     "See it spitter, spitter, spatter.",
                     "Rain, oh rain, don't go away",
                     "We need you for flow'rs in May",
                     "Drip, drip, drop and do not stop",
                     "Send a little rain our way."]

happy_bday = Song(happy_bday_lyrics)

bulls_on_parade = Song(bulls_on_parade_lyrics)

old_macdonald_had_a_farm = Song(old_macdonald_had_a_farm_lyrics)

apple_rain = Song(apple_rain_lyrics)


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

old_macdonald_had_a_farm.sing_me_a_song()

apple_rain.sing_me_a_song()

print(happy_bday.loved)
print(bulls_on_parade.loved)
print(old_macdonald_had_a_farm.loved)
print(apple_rain.loved)