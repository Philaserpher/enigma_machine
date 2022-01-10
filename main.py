import tkinter as tk
from enigma import decode

# Create a window object
window = tk.Tk()
window.state('zoomed')
# Create an event handler
message = ""


def handle_keypress(event):
    global message
    enigma_char = decode(event.char)
    message += enigma_char
    label.configure(text=message)
    print(enigma_char)


label = tk.Label(master=window, textvariable=message, font=("Arial", 30))
label.pack()
window.bind("<Key>", handle_keypress)

# Run the event loop
window.mainloop()
