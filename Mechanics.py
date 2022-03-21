import tkinter
import tkinter.filedialog
import pandas
from PDFClass import PDF


directory = None


def save_to() -> dir:
    """Choose right dir to save all PDFs"""
    global directory
    directory = tkinter.filedialog.askdirectory(initialdir="/", title='Proszę wybierz folder do zapisu certyfikatów')
    return directory


def header_logo() -> None:
    """Sets top-right logo"""
    pass


def conference_title() -> None:
    """Sets tile in center of PDF"""
    pass


def footer_sponsors() -> None:
    """Sets footer with sponsors"""
    pass


def loadfile() -> None:
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
        full_name = (degree + " " + name)
        file_name = (name + ".pdf")
        conference_image = '/Users/tomek/Desktop/11.jpeg'
        conference_text = 'ktora odbyla sie w dniach 05-06 marca 2022 r. w Instytucie Badan Informacji i ' \
                          'Komunikacji Uniwersytetu Mikolaja Kopernika w Toruniu i wyglosil/a referat, pt.:'

        # PDF FILE
        pdf = PDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(100, 80, '', ln=2, align='C')  # JUST TO SET EMPTY SPACE ABOVE TEXT
        pdf.cell(0, 10, full_name, ln=2, align='C')
        pdf.cell(0, 10, 'uczestniczyl/a w', ln=2, align='C')
        pdf.image(conference_image, w=10, h=10, type='JPEG')
        pdf.multi_cell(0, 10, conference_text , align='C')
        pdf.cell(0, 10, title, align='C')
        pdf.output(file_name, 'F')


def generate() -> None:
    """Probably will be deleted..."""
    pass
