import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def new_file():
    pass
def change_color():
    color = colorchooser.askcolor(title="Pick a color")
    text_area.config(fg=color[1])
def change_font(*args):
    pass
def open_file():
    pass
def save_file():
    pass
def cut_text():
    pass
def copy_text():
    pass
def paste_text():
    pass
def about():
    pass
def exit():
    pass

window = Tk()
window.title("Note Pad")
file = None

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("20")

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (int((screen_width / 2) - (window_width / 2)))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

text_area = Text(window, font=(font_name.get(), int(font_size.get())))
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)

frame = Frame(window)
frame.grid()
color_button = Button(frame, text="Color",command=change_color)
color_button.grid(row=0, column=0)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

window.mainloop()
