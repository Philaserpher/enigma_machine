# this class represents the reflector of the enigma machine. It contains a
# dictionary that maps every letter in the alphabet to another letter. It
# is very similar to the rotors except it is stationary


class Reflector:

    def __init__(self, connections):
        self.connections = connections

    # pass_through takes a letter and returns the connected letter within
    # the reflector

    def pass_through(self, letter):
        letter = letter.upper()
        return(self.connections[letter])
