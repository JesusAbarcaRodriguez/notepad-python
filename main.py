import os
from tkinter import *
from tkinter import filedialog, colorchooser, font, ttk
from tkinter.messagebox import *

def new_file():
    window.title("Untitled")
    file = None
    text_area.delete(1.0, END)

def change_color():
    color = colorchooser.askcolor(title="Pick a color")
    if color:
        text_area.config(insertbackground=color[1], fg=color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(), int(font_size.get())))

def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        window.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0, END)
        with open(file, "r") as file_contents:
            text_area.insert(1.0, file_contents.read())

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        with open(file, "w") as file_contents:
            file_contents.write(text_area.get(1.0, END))

def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("Notepad", "Notepad by Python")

def exit():
    window.destroy()

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
color_button = Button(frame, text="Color", command=change_color, bg="#007bff", fg="#ffffff")
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

window.mainloop()
