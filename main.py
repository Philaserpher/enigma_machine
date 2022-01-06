from rotors import Rotor
from reflector import Reflector
from plugboard import Plugboard

# set up dictionaries for all rotors and reflector. These are based on the
# real enigma rotors, I, II and III, as well as reflector I. The Enigma
# machines had a variation of rotors and reflectors available that could
# be swapped out, but there are always 3 rotors and 1 reflector

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


# create list of three rotors + reflector and plugboard

rotors = [Rotor(CONNECTIONS_1), Rotor(CONNECTIONS_2), Rotor(
    CONNECTIONS_3), Reflector(CONNECTIONS_REFLECTOR)]
plugboard = Plugboard({"H": "R", "R": "H"})


# this function takes a character, a list of rotrs and plugboard and returns
# the character that an enigma machine would produce. The order is plugboard
# -> rotors(1, 2, 3) -> reflector -> rotors(3, 2, 1) -> plugboard -> output
# it is not designed to receive anything other than letters

def get_new_character(character, rotors, plugboard):

    character = plugboard.pass_through(character)
    for i in range(4):
        character = rotors[i].pass_through(character)
    for i in range(2, -1, -1):
        character = rotors[i].pass_through(character)

    character = plugboard.pass_through(character)

    return(character)


# main takes a string and runs all characters through the enigma machine
# spaces are just passed through. After obtaining the string, we rotate
# the first rotor. If it completed a revolution, we rotate the second,
# and similarly the third. To test that this function works, we can set
# the test_string to AAAAAAAA and will obtain MMIUPHZQ

def main(message, rotors, plugboard):
    output_string = ""
    for character in message:
        if character == " ":
            output_string += " "
            continue
        output_string += get_new_character(character, rotors, plugboard)
        if rotors[0].rotate():
            print("A")
            if rotors[1].rotate():
                rotors[2].rotate()
    return(output_string)


if __name__ == "__main__":
    test_string = "Hello world"
    test_string = test_string.upper()
    print(main(test_string, rotors, plugboard))
