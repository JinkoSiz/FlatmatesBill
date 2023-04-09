import os
import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, flatmates_bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image('files/house.png', w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        # Insert period, label and value
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=f'{flatmates_bill.period}', border=0, ln=1)

        # Insert name and amount of the first flatmate
        pdf.set_font(family='Times', size=16)
        pdf.cell(w=100, h=25, txt=f'{flatmate1.name}', border=0)
        pdf.cell(w=150, h=25, txt=f'{round(flatmate1.pays(flatmates_bill, flatmate2), 2)}', border=0, ln=1)

        # Insert name and amount of the second flatmate
        pdf.set_font(family='Times', size=16)
        pdf.cell(w=100, h=25, txt=f'{flatmate2.name}', border=0)
        pdf.cell(w=150, h=25, txt=f'{round(flatmate2.pays(flatmates_bill, flatmate1), 2)}', border=0, ln=1)

        # Change directory to files, generate and open PDF
        os.chdir('files')
        pdf.output(self.filename)
        return webbrowser.open(self.filename)
