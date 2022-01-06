class Rotor:

    def __init__(self, connections, position=0):
        self.connections = connections
        self.position = position

    def rotate(self):
        self.position += 1
        if self.position > 25:
            self.position -= 25
            # will return True if it finished its rotation, so that we can
            # rotate the next rotor
            return(True)
        return(False)

    def pass_through(self, letter):
        letter.upper()
        # ensure the letter is uppercase
        # convert letter into a number, a = 0, z = 25
        letter = ord(letter) - 65
        # add the position, to simulate the fact that the rotor connectors
        # move relative to the input terminals, so after 1 rotation
        letter += self.position
        if letter > 25:
            # the letter a goes in through b connector, counts as b
            letter -= 25
        letter = chr(letter + 65)
        # pass the letter through the internalk wiring of the rotor and return
        return(self.connections[letter])
