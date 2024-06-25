from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import calendar, datetime
import csv
import locale
from reportlab.lib import colors
locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
NOW = datetime.datetime.now()

nombre = ""
empresa = ""
departamento = ""
festivos = ["25/12/2024","01/01/2024", "29/03/2024","01/05/2024","15/08/2024","12/10/2024","01/11/2024","06/12/2024"]

with open('data/data.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for linea in csv_reader:
        pass
with open('data/data2.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for linea2 in csv_reader:
        pass
with open('data/data3.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for linea3 in csv_reader:
        pass
with open('data/data4.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for linea4 in csv_reader:
        if len(linea4) > 0:
            nombre = str(linea4[0])

# Read data from data5.csv
with open('data/data5.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for linea5 in csv_reader:
        if len(linea5) > 0:
            empresa = str(linea5[0])

# Read data from data6.csv
with open('data/data6.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for linea6 in csv_reader:
        if len(linea6) > 0:
            departamento = str(linea6[0])

    def draw_year_title(c, year):

        c.setFont("Helvetica-Bold", 10)
        c.drawString(210, 820, f"{year}")
        c.setFont("Helvetica-Bold", 7)
        c.drawString(20, 800, f"SOLICITUD DE:")
        c.setFont("Helvetica-Bold", 7)
        c.drawString(15, 740, f"NOMBRE: " + nombre)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(15, 730, f"EMPRESA: " + empresa)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(15, 720, f"DEPARTAMENTO: " + departamento)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(270, 790, f"VACACIONES:")
        c.rect(380, 785, 10, 10)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(270, 780, f"FIESTAS LOCALES:")
        c.rect(380, 775, 10, 10)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(270, 770, f"OTROS PERMISOS:")
        c.rect(380, 765, 10, 10)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(220, 80, f"APROBADO POR EL RESPONSABLE:")
        c.setFont("Helvetica-Bold", 7)
        c.drawString(220, 70, f"NOMBRE Y FIRMA:")
        c.setFont("Helvetica-Bold", 7)
        c.drawString(45, 90, f"FESTIVOS")
        c.setFillColor(colors.red)
        c.rect(20 , 88 , 20, 10, fill=True, stroke=False)
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(45, 78, f"VACACIONES")
        c.setFillColor(colors.lightgreen)
        c.rect(20 , 76 , 20, 10, fill=True, stroke=False)
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(45, 66, f"FIESTAS LOCALES")
        c.setFillColor(colors.lightblue)
        c.rect(20 , 64 , 20, 10, fill=True, stroke=False)
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(45, 54, f"OTROS PERMISOS")
        c.setFillColor(colors.lightpink)
        c.rect(20 , 52, 20, 10, fill=True, stroke=False)
        c.setFillColor(colors.black)

    def draw_month(c, year, month, x_start, y_start, cell_width, cell_height):

        c.setFont("Helvetica", 8)
        cal = calendar.Calendar()
        month_days = cal.monthdayscalendar(year, month)
        # Draw the month name at the top of each month
        month_name = calendar.month_name[month]
        c.drawString(x_start + 20, y_start, f"{month_name} {year}")
        # Draw the day names
        day_names = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
        x = x_start
        y = y_start - 10
        for day in day_names:
            c.drawString(x + 2, y, day)
            x += cell_width
        # Draw the days with cells
        y -= cell_height
        for week in month_days:
            x = x_start
            for day in week:
                c.rect(x, y - cell_height, cell_width, cell_height)  # Draw cell
                if day != 0:
                    c.drawString(x + 10, y - 10, str(day))
                    fecha_str2 ="{:02d}/{:02d}/{:04d}".format(day, month, year)
                    if fecha_str2 in linea:
                        c.setFillColor(colors.lightgreen)
                        c.rect(x , y , 20, -15, fill=True, stroke=False)
                        c.setFillColor(colors.black)
                        c.line(380,785,390,795)
                        c.drawString(x + 10, y - 10, str(day))

                    if fecha_str2 in linea2:
                        c.setFillColor(colors.lightblue)
                        c.rect(x , y , 20, -15, fill=True, stroke=False)
                        c.setFillColor(colors.black)
                        c.line(380,775,390,785)
                        c.drawString(x + 10, y - 10, str(day))

                    if fecha_str2 in linea3:
                        c.setFillColor(colors.lightpink)
                        c.rect(x , y , 20, -15, fill=True, stroke=False)
                        c.setFillColor(colors.black)
                        c.line(380,765,390,775)
                        c.drawString(x + 10, y - 10, str(day))
                        
                    if fecha_str2 in festivos:
                        c.setFillColor(colors.red)
                        c.rect(x , y , 20, -15, fill=True, stroke=False)
                        c.setFillColor(colors.black)
                        c.drawString(x + 10, y - 10, str(day))
                x += cell_width
            y -= cell_height

    def create_yearly_calendar(year, filename):
        c = canvas.Canvas(filename, pagesize=A4)
        width, height = A4
        cell_width = 20
        cell_height = 15
        x_offset = 15
        y_offset = height - 170
        x_gap = 10
        y_gap = 25

        months_per_row = 3
        draw_year_title( c, year)

        for month in range(1, 13):
            row = (month - 1) // months_per_row
            col = (month - 1) % months_per_row
            x_start = x_offset + col * (cell_width * 7 + x_gap)
            y_start = y_offset - row * (cell_height * 8 + y_gap)
            draw_month(c, year, month, x_start, y_start, cell_width, cell_height)
        
        c.save()

# Especificar el año y nombre del archivo
year = NOW.year
filename = "calendario_anual.pdf"
create_yearly_calendar(year, filename)

#TERMINADO EL 25/06/2024
#DIEGO HIGUERA TRIGUERO