from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        #self.set_font('Arial', 'B', 15)
        self.image('/Users/tomek/Desktop/Certyfikaty/uni.png', x=None, y=1, w=100, h=0, type='', link='')
        #self.cell(80)
        #self.cell(30, 10, 'TEST', 0, 0, 'C')
        #self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'B', 15)
        self.image('/Users/tomek/Desktop/11.jpeg', x = None, y = None, w = 2, h = 2, type = '', link = '')
        self.cell(80)
        self.cell(30, 10, 'TEST', 0, 0, 'C')
