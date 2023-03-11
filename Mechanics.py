import tkinter
import tkinter.filedialog
import pandas
from fpdf import FPDF as PDF


directory = None
header_img = None
conf_title_img = None
footer_img = None


def save_to() -> None:
    """Choose right dir to save all PDFs"""
    global directory
    directory_obj = tkinter.filedialog.askdirectory(initialdir="/", title='Proszę wybierz folder do zapisu certyfikatów')
    directory = directory_obj


def conference_title() -> None:
    """Sets title in center of PDF"""
    global conf_title_img
    conf_title_object = tkinter.filedialog.askopenfile(initialdir="/", title='Proszę wybierz obraz z nazwą konferencji')
    conf_title_img = conf_title_object.name


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
        uni = (element[4])
        full_name = (degree + " " + name)
        file_name = (name + ".pdf")
        conference_image = conf_title_img

        # PDF FILE
        pdf = PDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.add_font('Lato-BoldItalic', 'B', 'Lato-BoldItalic.ttf', uni=True)
        pdf.add_font('Lato-Italic', 'I', 'Lato-Italic.ttf', uni=True)
        pdf.set_font('Lato-BoldItalic', 'B', 24)
        pdf.image(conference_image, x=0, y=0, w=210, h=297, type='')
        pdf.cell(100, 40, '', ln=2, align='C')  # JUST TO SET EMPTY SPACE ABOVE TEXT
        pdf.cell(0, 10, full_name, ln=2, align='C')
        pdf.set_font('Lato-Italic', 'I', 14)
        pdf.multi_cell(0, 10, uni, align='C')
        pdf.cell(100, 100, '', ln=2, align='C') # ANOTHER SPACER
        pdf.set_font('Lato-Italic', 'I', 24)
        pdf.multi_cell(190, 10, title, align='C')
        pdf.output((directory+"/"+file_name), "F")
