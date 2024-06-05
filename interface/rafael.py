from tkinter import *

window = Tk()
window.title("Window Execution")
window.geometry("300x100")

message = Label(window, text="Good Morning")
message.pack(pady=10)

button = Button(window, text="Touch on me", command=quit)
button.pack(pady=10)

frame = Frame()

window.mainloop()
