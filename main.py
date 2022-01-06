from rotors import Rotor
from reflector import Reflector

# set up dictionaries for all rotors and reflector
CONNECTIONS_1 = {"A": "E", "B": "K", "C": "M", "D": "F", "E": "L", "F": "G",
                 "G": "D", "H": "Q", "I": "V", "J": "Z", "K": "N", "L": "T",
                 "M": "O", "N": "W", "O": "Y", "P": "H", "Q": "X", "R": "U",
                 "S": "S", "T": "P", "U": "A", "V": "I", "W": "B", "X": "R",
                 "Y": "C", "Z": "J"}
CONNECTIONS_2 = {"A": "E", "B": "K", "C": "M", "D": "F", "E": "L", "F": "G",
                 "G": "D", "H": "Q", "I": "V", "J": "Z", "K": "N", "L": "T",
                 "M": "O", "N": "W", "O": "Y", "P": "H", "Q": "X", "R": "U",
                 "S": "S", "T": "P", "U": "A", "V": "I", "W": "B", "X": "R",
                 "Y": "C", "Z": "J"}
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


def pass_through_rotors(letter, rotor):
    return rotor.pass_through(letter)


def main(test_string, rotors):
    for x in range(7):
        print(x)


if __name__ == "__main__":
    test_string = "Hello"
    main(test_string, rotors)
