# enigma_machine
A simple enigma machine simulator.

An enigma machine is an encryption machine used before and during the Second World War by the Axis to encrypt their communications. Breaking the Enigma machine was key to allied victory, as it allowed them to intercept and read all of the communications from the German Army and Navy. There are three main features of the enigma machine which made it incredibly difficult to crack.

For the purpose of this example we will see what happens when typing the leter "A" twice into the keyboard

When a button is pressed, the signal first goes to the plugboard. Here, we check if the letter pressed is connected to another letter through the plugboard. We can connect any two letters together. If there is a connection, for example, "A" is connected to "C" (and therefore "C" is connected to "A"), then we replace it with "C".

Then the signal, now "C" heads over to the rotors. It goes in through the "C" connector on the first rotor. Every rotor connects an input letter with an output letter. For example, rotor 1 connects "A" to "E", and "B" to "K". However, unlike the plugboard, they dont have to be connected to each other. So although "A" is connected to "E", "E" is connected to "L". So in this case, our "C" signal becomes an "M". When then repeat this process through rotors 2 and 3, making our letter "W" and "B" respectively. There are different rotors, but we always choose 3. For the purpose of this program, rotors I, II and III of the original enigma machine are being used.

We then get to the reflector, which has similar wiring to the rotors. In this case, our letter "B" becomes "J", and it is sent back through rotors 3, 2 and 1 (in that order, reverse of the previous). Our letter therefore becomes "Z", then "E", then "L". 

Finally, we run the letter through the plugboard again. In this case, "L" is not connected to anything, but if it was we would replace it like we did earlier.

So, so far, we've done "A" -> "C" -> "M" -> "W" -> "B" -> "J" -> "Z" -> "E" -> "L". In terms of which components, it was "Keyboard" -> "Plugboard" -> "Rotors(1, 2, 3)" -> "Reflector" -> "Rotors(3, 2, 1)" -> Plugboard. However, even though it looks very complicated, this is just a substitution cypher. If we press "A" again, it'll take the same path, and result in "L" again right?. Well, the enigma machine has one last ace up its sleeve to make it harder to crack. After every button press, the rotors will rotate. To be precise, the 1st rotor will rotate by one letter (1/26th). After a full rotation of the first rotor (or 26 key presses/characters) the second rotor moves one letter, and after 676 characters the 3rd rotor will move by 1. It will take 17576 characters to make the 3rd rotor move a full revolution. The rotors, furthermore, can be initialised to any position, so we can have rotor 1 start at its default position but have rotors 2 and 3 start 3 steps forward.

So if you keep pressing the same letter, you'll get different ones. The rotor connectors move relative to each other, so our "C" input into rotor 1 earlier to goes in as a "D", which connects to "F". However, due to de rotation, the "F" output comes out where the "E" is supposed to be. So the "M" from earlier is now an "E"!!!! (More detail on rotor.py) If we continue this path, we find that the second "A" actually ends as an "E". So the message "AA" becomes "LE".

So if we type in "HHHHHHHH" we actually get "MMIUPHZQ". This made the enigma machine incredibly hard to break at the time. It is interesting to think that such as complex machine that resulted in so many deaths during the Second World War would be laughably easy to crack nowadays, and can be recreated digitally relatively simply as well.
