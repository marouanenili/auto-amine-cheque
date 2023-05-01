from reportlab.pdfgen import canvas
from num2words import num2words


def draw_lines(pdf):
    pdf.setFont('Helvetica', 8)
    y_start = 50
    y_end = 800
    x_start = 50
    x_end = 550
    y_gap = (y_end - y_start) / 10
    x_gap = (x_end - x_start) / 10

    for i in range(11):
        # Draw vertical lines
        x = x_start + (i * x_gap)
        pdf.line(x, y_start, x, y_end)
        pdf.drawString(x - 5, y_start - 15, str(x))

        # Draw horizontal lines
        y = y_start + (i * y_gap)
        pdf.line(x_start, y, x_end, y)
        pdf.drawString(x_start - 25, y + 2, str(y))
def write_check_date(pdf,x,y,date,font_size=10):
    pdf.setFont('Helvetica', font_size)
    pdf.drawString(x, y, date)
def write_check_montant(pdf,x,y,amount,font_size=10):
    pdf.setFont('Helvetica', font_size)
    pdf.drawString(x, y, str(amount)+" Dhs")
def write_check_name(pdf,x,y,name,font_size=10):
    pdf.setFont('Helvetica', font_size)
    pdf.drawString(x, y, name)
def write_check_amount_in_letters(pdf,x,y,amount_in_letters,font_size=10):
    pdf.setFont('Helvetica', font_size)
    string = amount_in_letters + " dirhams"
    words = string.split()
    max_line_length = 20
    line_spacing = 20
    current_line = ""
    for word in words:
        if len(current_line + word) <= max_line_length:
            current_line += word + " "
        else:
            pdf.drawString(x, y, current_line.strip())
            current_line = word + " "
            y -= line_spacing
        if len(current_line) > 0:
            pdf.drawString(x, y, current_line.strip())
def write_check_lieu_et_date(pdf,x,y,lieu_et_date,font_size=10):
    pdf.setFont('Helvetica', font_size)
    pdf.drawString(x, y, lieu_et_date)
def write_check_cause(pdf,x,y,cause,font_size=10):
    pdf.setFont('Helvetica', font_size)
    string_to_print = ""
    string_list = cause.split()
    for string in string_list:
        string_to_print += string + " "
        if len(string_to_print) < 30:
            continue
        else:
            pdf.drawString(x, y, string_to_print)
            string_to_print = ""
            y -= 20
    if len(string_to_print) > 0:
        pdf.drawString(x, y, string_to_print)

def write_string(pdf,x,y,string,font_size=10):
    pdf.setFont('Helvetica', font_size)
    pdf.drawString(x, y, string)
class check_auto_amine():
    def __init__(self, name, amount, date_echeance, lieux_et_date ,cause):
        self.name = name
        self.amount = amount
        self.date = date_echeance
        self.amount_in_letters = num2words(int(amount), lang='fr')
        self.lieu_et_date = lieux_et_date
        self.cause = cause
        self.taille = 10
        self.x_date = 460
        self.y_date = 825
        self.x_montant = 450
        self.y_montant = 800
        self.x_name = 350
        self.y_name = 760
        self.x_amount_in_letters = 430
        self.y_amount_in_letters = 735
        self.x_lieu_et_date = 250
        self.y_lieu_et_date = 730
        self.x_cause = 250
        self.y_cause = 700


    def write_all(self):
        pdf = canvas.Canvas("check.pdf")

        write_check_date(pdf,self.x_date,self.y_date,self.date)
        write_check_montant(pdf,self.x_montant,self.y_montant,self.amount)
        write_check_name(pdf,self.x_name,self.y_name,self.name)
        write_check_amount_in_letters(pdf,self.x_amount_in_letters,self.y_amount_in_letters,self.amount_in_letters)
        write_check_lieu_et_date(pdf,self.x_lieu_et_date,self.y_lieu_et_date,self.lieu_et_date)
        write_check_cause(pdf,self.x_cause,self.y_cause,self.cause)
        pdf.save()

class effet_marpia():
    def __init__(self, name, amount, date_echeance, lieux_et_date ,cause):
        self.name = name
        self.amount = amount
        self.date = date_echeance
        self.amount_in_letters = num2words(int(amount), lang='fr')
        self.lieu_et_date = lieux_et_date
        self.cause = cause
        self.taille = 10
        self.x_name = 250
        self.y_name = 760
        self.x_date_et_lieu = 250
        self.y_date_et_lieu = 735
        self.x_cause = 250
        self.y_cause = 710
        self.x_montant = 450
        self.y_montant = 715
        self.x_amount_in_letters = 430
        self.y_amount_in_letters = 685
        self.x_date = 460
        self.y_date = 735

    def write_all(self):
        pdf = canvas.Canvas("check.pdf")

        write_check_name(pdf,self.x_name,self.y_name,self.name)
        write_check_lieu_et_date(pdf,self.x_date_et_lieu,self.y_date_et_lieu,self.lieu_et_date)
        write_check_cause(pdf,self.x_cause,self.y_cause,self.cause)
        write_check_montant(pdf,self.x_montant,self.y_montant,self.amount)
        write_check_amount_in_letters(pdf,self.x_amount_in_letters,self.y_amount_in_letters,self.amount_in_letters)
        write_check_date(pdf,self.x_date,self.y_date,self.date)
        pdf.save()

class check_marpia():
    def __init__(self, name, amount, date, lieu):
        self.name = name
        self.amount = amount
        self.amount_in_letters = num2words(int(amount), lang='fr')
        self.taille = 10
        self.date = date
        self.lieu = lieu
        self.x_name = 220
        self.y_name = 770
        self.x_montant = 350
        self.y_montant = 820
        self.x_lieu = 210
        self.y_lieu = 740
        self.x_date = 350
        self.y_date = 740

    def write_all(self):
        pdf = canvas.Canvas("check.pdf")
        write_check_name(pdf,self.x_name,self.y_name,self.name)
        write_string(pdf,self.x_lieu,self.y_lieu,self.lieu)

        write_check_montant(pdf,self.x_montant,self.y_montant,self.amount)
        write_check_date(pdf,self.x_date,self.y_date,self.date)
        pdf.save()

