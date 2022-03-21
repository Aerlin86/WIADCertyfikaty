import tkinter as tk
from tkinter import *
from tkinter import ttk
from Mechanics import *

root = tk.Tk()

root.title('WIAD Certificate')
root.resizable(0, 0)

logo = ttk.Frame(root)
logo.grid()

text = Label(logo, text="WIAD Certificate", font=("Helvetica", 20))
text.grid(row=0, column=0)
text = Label(logo, text="Automatyczna generacja certyfikatów", font=("Helvetica", 10))
text.grid(row=1, column=0)

buttons = ttk.Frame(root, padding=(20, 10, 20, 0))
buttons.grid()


choosefile_button = ttk.Button(buttons, text="Wybierz miejsce zapisu", command=save_to)
choosefile_button.grid(row=0, column=0, columnspan=3, sticky=tk.W+tk.E)

choosedir_button = ttk.Button(buttons, text="Wybierz logo", command=header_logo)
choosedir_button.grid(row=1, column=0, columnspan=3, sticky=tk.W+tk.E)

choosedir_button = ttk.Button(buttons, text="Wybierz nazwę konferencji", command=conference_title)
choosedir_button.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)

choosedir_button = ttk.Button(buttons, text="Wybierz sponsorów", command=footer_sponsors)
choosedir_button.grid(row=3, column=0, columnspan=3, sticky=tk.W+tk.E)

choosedir_button = ttk.Button(buttons, text="Wybierz plik z danymi", command=loadfile)
choosedir_button.grid(row=4, column=0, columnspan=3, sticky=tk.W+tk.E)

makedir_button = ttk.Button(buttons, text="GENERUJ", command=generate)
makedir_button.grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E)

quit_button = ttk.Button(buttons, text="Wyjście", command=root.destroy)
quit_button.grid(row=6, column=1)

root.mainloop()
