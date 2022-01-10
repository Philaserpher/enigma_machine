import tkinter as tk
from enigma import decode

# Create a window object
window = tk.Tk()
window.state('zoomed')
# Create an event handler
message = ""


def handle_keypress(event):
    global message
    enigma_info = decode(event.char)
    message += enigma_info[0]
    for i, rotor in enumerate(rotor_info):
        rotor.configure(text=(enigma_info[1][i]+1))
    text.configure(text=message)
    print(enigma_info[1])
    print(enigma_info[0])


def close(event):
    window.destroy()


rotor_info = [tk.Label(master=window, text="1", font=("Arial", 50)),
              tk.Label(master=window, text="1", font=("Arial", 50)),
              tk.Label(master=window, text="1", font=("Arial", 50))]
for i in rotor_info:
    i.pack()

text = tk.Label(master=window, text="", font=("Arial", 30))
text.pack()

window.bind("<Key>", handle_keypress)
window.bind("<Escape>", close)

# Run the event loop
window.mainloop()
