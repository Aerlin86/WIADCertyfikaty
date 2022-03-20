# ALL CODE SOURCE FOR MECHANICS USED IN THIS PROJECT

import os, shutil, tkinter, tkinter.filedialog, re

import pandas
from fpdf import FPDF


directory = None


def loadfile() -> list:
    """Loads Excel file and put data into list"""
    # CHOOSING FILE
    file = tkinter.filedialog.askopenfilename(initialdir="/", title='Proszę wybierz plik z danymi prelegentów')

    # READ AND EXTRACT DATA FROM EXCEL FILE
    db = pandas.read_excel(file, sheet_name='Arkusz1')
    all_data_list = db.values.tolist()
    for element in all_data_list:
        x = type(element[0])
        if x == float:
            degree = ""
        else:
            degree = element[0]
        name = (element[1] + " " + element[2])
        title = (element[3])
        # PDF FILE




def save_to() -> dir:
    """Choose right dir to save all PDFs"""
    global directory
    directory = tkinter.filedialog.askdirectory(initialdir="/", title='Proszę wybierz folder do zapisu certyfikatów')
    return directory


def generate() -> None:
    pass
