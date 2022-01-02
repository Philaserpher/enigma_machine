class Rotor:

    def __init__(self, connections, position = 0):
        self.connections = connections
        self.position = position

    def rotate(self):
        self.position += 1
        if self.position > 25:
            self.position -=25

    def getvalue(self, letter):
        return(self.connections[letter])

    def pass_through(self, letter):
        letter = ord(letter) - 65                       # convert letter into a number, a = 0, z = 25
        letter += self.position()                       # add the position, to simulate the fact that the rotor connectors move relative to the input terminals, so after 1 rotation
        if letter > 25:                                 # the letter a would go in through the b connector, so it would count as a b
            letter -= 25                                        