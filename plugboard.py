class Plugboard:

    def __init__(self, connections={}):
        self.connections = connections

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
