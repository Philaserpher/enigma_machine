from rotors import Rotor
from reflector import Reflector
from plugboard import Plugboard

# set up dictionaries for all rotors and reflector
CONNECTIONS_1 = {"A": "E", "B": "K", "C": "M", "D": "F", "E": "L", "F": "G",
                 "G": "D", "H": "Q", "I": "V", "J": "Z", "K": "N", "L": "T",
                 "M": "O", "N": "W", "O": "Y", "P": "H", "Q": "X", "R": "U",
                 "S": "S", "T": "P", "U": "A", "V": "I", "W": "B", "X": "R",
                 "Y": "C", "Z": "J"}
CONNECTIONS_2 = {"A": "A", "B": "J", "C": "D", "D": "K", "E": "S", "F": "I",
                 "G": "R", "H": "U", "I": "X", "J": "B", "K": "L", "L": "H",
                 "M": "W", "N": "T", "O": "M", "P": "C", "Q": "Q", "R": "G",
                 "S": "Z", "T": "N", "U": "P", "V": "Y", "W": "F", "X": "V",
                 "Y": "O", "Z": "E"}
CONNECTIONS_3 = {"A": "E", "B": "K", "C": "M", "D": "F", "E": "L", "F": "G",
                 "G": "D", "H": "Q", "I": "V", "J": "Z", "K": "N", "L": "T",
                 "M": "O", "N": "W", "O": "Y", "P": "H", "Q": "X", "R": "U",
                 "S": "S", "T": "P", "U": "A", "V": "I", "W": "B", "X": "R",
                 "Y": "C", "Z": "J"}
CONNECTIONS_REFLECTOR = {"A": "E", "B": "J", "C": "M", "D": "Z", "E": "A",
                         "F": "L", "G": "Y", "H": "X", "I": "V", "J": "B",
                         "K": "W", "L": "F", "M": "C", "N": "R", "O": "Q",
                         "P": "U", "Q": "O", "R": "N", "S": "T", "T": "S",
                         "U": "P", "V": "I", "W": "K", "X": "H", "Y": "G",
                         "Z": "D"}

rotors = [Rotor(CONNECTIONS_1), Rotor(CONNECTIONS_2), Rotor(
    CONNECTIONS_3), Reflector(CONNECTIONS_REFLECTOR)]
plugboard = Plugboard()
# create list of three rotors + reflector and plugboard


def pass_through_rotors(letter, rotor):
    return rotor.pass_through(letter)


def main(test_string, rotors):
    output_string = ""
    for x in test_string:
        character = x
        if character == " ":
            output_string += " "
            continue
        for i in range(4):
            character = rotors[i].pass_through(character)
        for i in range(2, -1, -1):
            character = rotors[i].pass_through(character)
        output_string += character
    return(output_string)


if __name__ == "__main__":
    test_string = "Hello World"
    print(main(test_string, rotors))
