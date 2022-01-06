# this class represents the plugboard of the enigma machine. It contains a
# dictionary, self.connections, which has all the information on which
# letters are connected to which in the plugboard.


class Plugboard:

    def __init__(self, connections={}):
        self.connections = connections

    # the code to add a connection looks a bit tricky. We have to ensure that
    # neither a nor b already have a connection. Furthermore, if either of them
    # do, we have to also remove the entry for the letter corresponding to the
    # one that already exists (if a and c are matched, we must remove
    # ("A" : "C") and ("C" : "A") to add a and b

    def add_connection(self, a, b):
        a = a.upper()
        b = b.upper()
        if a in self.connections:
            temp = self.connections[a]
            self.connections.pop(a)
            self.connections.pop(temp)
        if b in self.connections:
            temp = self.connections[b]
            self.connections.pop(b)
            self.connections.pop(temp)
        self.connections[a] = b
        self.connections[b] = a

    def pass_through(self, letter):
        letter = letter.upper()
        if letter in self.connections:
            return(self.connections[letter])
        return(letter)
