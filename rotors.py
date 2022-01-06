# this class represents the rotors of the enigma machine. It contains a
# dictionary that maps every letter in the alphabet to another letter, as
# wellas a position marker that shows its current state of rotation. After
# every keypress, the first wheel rotates, and after every full wheel
# rotation, the next one moves 1 step. So every 26 letters the second
# rotor will move 1 step, and after 26*26 = 676 letters the last rotor will
# move 1 step

class Rotor:

    def __init__(self, connections, position=0):
        self.connections = connections
        self.position = position

    # will rotate the wheel 1 step. If it reset back to the start, it will
    # set it back to 0 and it will return True so that we can rotate the
    # next rotor

    def rotate(self):
        self.position += 1
        if self.position > 25:
            self.position -= 26
            return(True)
        return(False)

    # pass_through takes a letter and returns the connected letter within
    # the reflector. However, it is more complex that in the case of the
    # reflector or the plugboard, as this time we have to consider that an
    # output coming from the A position in the previous rotor will actually
    # come in as A + position

    def pass_through(self, letter):
        letter = letter.upper()
        letter = ord(letter) - 65
        letter += self.position
        if letter > 25:
            letter -= 26
        letter = chr(letter + 65)

        # this part is a bit tricky. We have to get the connected letter,
        # and add to it (26 - position). It is a bit tricky to explain non
        # graphically but this is to compensate for the fact that while the
        # connected letter might be "C", the "C" connector has changed
        # position due to the rotation of the wheel, so it no longer counts
        # as a "C", but as "C" + 26 - position. For example, if position = 0
        # then "C" = "C" + 26 = "C", no change. If position = 1, the rotor
        # will have moved so that "B" is where "A" was, so "C" is where "B"
        # was, so it will count as a "B". So in this case "C" = "C" + 26 - 1
        # which is "C" + 25 which is the same as "C" - 1 = "B". If there are
        # any doubts try drawing a simple wheel with 4 or 5 connectors and
        # rotating it yourself. Took my a while to figure this out
        letter = self.connections[letter]

        # converting to ASCII back and forth isnt too efficient but I already
        # made the dictionaries based on letters and it took to long so
        # sunk cost fallacy it is

        letter = ord(letter) - 65
        letter += (26 - self.position)
        if letter > 25:
            letter -= 26
        return(chr(letter + 65))
