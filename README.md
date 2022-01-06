# enigma_machine
A simple enigma machine simulator.

An enigma machine is an encryption machine used before and during the Second World War by the Axis to encrypt their communications. Breaking the Enigma machine was key to allied victory, as it allowed them to intercept and read all of the communications from the German Army and Navy. There are three main features of the enigma machine which made it incredibly difficult to crack.

For the purpose of this example we will see what happens when typing the leter "A" twice into the keyboard

When a button is pressed, the signal first goes to the plugboard. Here, we check if the letter pressed is connected to another letter through the plugboard. We can connect any two letters together. If there is a connection, for example, "A" is connected to "C" (and therefore "C" is connected to "A"), then we replace it with "C".

Then the signal, now "C" heads over to the rotors. It goes in through the "C" connector on the first rotor. Every rotor connects an input letter with an output letter. For example, rotor 1 connects "A" to "E", and "B" to "K". However, unlike the plugboard, they dont have to be connected to each other. So although "A" is connected to "E", "E" is connected to "L". So in this case, our "C" signal becomes an "M". 








LE