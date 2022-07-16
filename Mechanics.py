import tkinter
import tkinter.filedialog
import pandas
from PDFClass import PDF


directory = None
header_img = None
conf_title_img = None
footer_img = None


def save_to() -> None:
    """Choose right dir to save all PDFs"""
    global directory
    directory_obj = tkinter.filedialog.askdirectory(initialdir="/", title='Proszę wybierz folder do zapisu certyfikatów')
    directory = directory_obj


def header_logo() -> None:
    """Sets top-right logo"""
    global header_img
    header_img_object = tkinter.filedialog.askopenfile(initialdir="/", title='Proszę wybierz obraz z nazwą konferencji')
    header_img = header_img_object.name


def conference_title() -> None:
    """Sets title in center of PDF"""
    global conf_title_img
    conf_title_object = tkinter.filedialog.askopenfile(initialdir="/", title='Proszę wybierz obraz z nazwą konferencji')
    conf_title_img = conf_title_object.name


def footer_sponsors() -> None:
    """Sets footer with sponsors"""
    global footer_img
    footer_img_object = tkinter.filedialog.askopenfile(initialdir="/", title='Proszę wybierz obraz z nazwą konferencji')
    footer_img = footer_img_object.name


def loadfile() -> None:
    """Loads Excel file, put data into list and generate PFD file"""

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
        full_name = (degree + " " + name)
        file_name = (name + ".pdf")
        conference_image = conf_title_img
        conference_text = 'która odbyla sie w dniach 05-06 marca 2022 r. w Instytucie Badan Informacji i ' \
                          'Komunikacji Uniwersytetu Mikolaja Kopernika w Toruniu i wyglosil/a referat, pt.:'

        # PDF FILE
        pdf = PDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(100, 80, '', ln=2, align='C')  # JUST TO SET EMPTY SPACE ABOVE TEXT
        pdf.cell(0, 10, full_name, ln=2, align='C')
        pdf.cell(0, 10, 'uczestniczyl/a w', ln=2, align='C')
        pdf.image(conference_image, x=-75, w=350, h=0, type='')
        pdf.multi_cell(0, 10, conference_text , align='C')
        pdf.cell(0, 10, title, align='C')
        pdf.output((directory+"/"+file_name), "F")
