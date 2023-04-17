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



class check_marpia():
    def __init__(self, name, amount, date_echeance, lieux_et_date ,cause):
        self.name = name
        self.amount = amount
        self.date = date_echeance
        self.amount_in_letters = num2words(int(amount), lang='fr')
        self.lieu_et_date = lieux_et_date
        self.cause = cause


    def write_check(self):
        pdf = canvas.Canvas("check.pdf")
        pdf.setFont('Helvetica', 8)
        pdf.drawString(50, 50, self.name)
        pdf.drawString(50, 100, self.amount)
        pdf.drawString(50, 150, self.date)
        pdf.save()
    def write_check_date(self,pdf):
        pdf.setFont('Helvetica', 14)
        pdf.drawString(460, 825, self.date)
       # pdf.save()
    def write_check_montant(self,pdf):
        pdf.setFont('Helvetica', 14)
        pdf.drawString(460, 810, self.amount+" DHS")
       # pdf.save()
    def write_check_name(self,pdf):
        pdf.setFont('Helvetica', 14)
        pdf.drawString(350, 760, self.name)
       # pdf.save()
    def write_check_amount_in_letters(self,pdf):
        pdf.setFont('Helvetica', 14)
        string = self.amount_in_letters +" Dirhams"
        string_list = string.split()
        string_to_print = ""
        print(string)
        y = 730
        for string in string_list:
            string_to_print += string + " "
            if len(string_to_print) < 20:
                continue
            else:
                pdf.drawString(450, y, string_to_print)
                string_to_print = ""
                y -= 20
        if len(string_to_print) > 0:
            pdf.drawString(450, y, string_to_print)
    def write_check_lieu_et_date(self,pdf):
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 725, self.lieu_et_date)
    def write_check_cause(self,pdf):
        pdf.setFont('Helvetica', 14)
        string_to_print = ""
        string_list = self.cause.split()
        y = 700
        for string in string_list:
            string_to_print += string + " "
            if len(string_to_print) < 30:
                continue
            else:
                pdf.drawString(230, y, string_to_print)
                string_to_print = ""
                y -= 20
        if len(string_to_print) > 0:
            pdf.drawString(230, y, string_to_print)


# Create a new PDF file
pdf = canvas.Canvas("lines.pdf")

# Draw the lines
#draw_lines(pdf)

marpia = check_marpia( "el maati tijani", "113643", "04/15/2023", "Marrakech, le 15/04/2023", " Paiement de la facture N° 113643 bla bla bla ")
marpia.write_check_date(pdf)
marpia.write_check_montant(pdf)
marpia.write_check_name(pdf)
marpia.write_check_amount_in_letters(pdf)
marpia.write_check_lieu_et_date(pdf)
marpia.write_check_cause(pdf)
# Save the PDF file
pdf.save()
