class Reflector:

    def __init__(self, connections):
        self.connections = connections

    def pass_through(self, letter):
        letter = letter.upper()             # ensure the letter is uppercase
        return(self.connections[letter])    # return the reflected letter
