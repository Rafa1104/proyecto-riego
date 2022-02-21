#import RPi.GPIO as GPIO
from email import header
import time
import csv
from datetime import  datetime, timedelta
#import os

import pandas as pd
import pdfkit
from fpdf import FPDF


class Riego:
    def lectura_sensor(self):

        tierra = 1    # Sensor de Tierra: Tierra seca 1 - Tierra humeda = 0
        estacion = 1  # Estacion de año: verano = 1, invierno = 0
        agua = 0      # Sensor de la Reserva: Reserva llena 0 - Reserva vacia = 1

        return(tierra, agua, estacion)

    def control_riego(self, tierra, dias, agua, estacion):

        # s = tierra
        # r = estacion
        # d = dia noche
        # v = agua

        dia_actual = datetime.today()
        dia_actual_formato = datetime.strftime(dia_actual, '%d-%m-%Y')

        hora_actual = datetime.now()
        hora_actual_formato = datetime.strftime(hora_actual, '%I:%M:%S %p')


        estado = ""
        tierra_Status = ""
        agua_Status = ""


        if tierra == 1:  # seca
            tierra_Status = "Seca"
            if estacion == 1:  # Verano
                if agua == 0:  # lleno
                    agua_Status = "Con Agua"
                    #GPIO.output(32, GPIO.HIGH)
                    estado = "BOMBA ACTIVADA"
                else:
                    agua_Status = "Sin Agua"

                    #GPIO.output(32, GPIO.LOW)
                    print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")

            else:

                if agua == 1:  # Reserva vacia
                    agua_Status = "Sin Agua"
                    print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")
                    estado = "BOMBA DESACTIVADA"
                    #GPIO.output(32, GPIO.LOW)

                else:

                    if agua == 0:  # lleno
                        agua_Status = "Con Agua"
                        #GPIO.output(32, GPIO.HIGH)
                        estado = "BOMBA ACTIVADA"

                    else:
                        agua_Status = "Sin Agua"
                        print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")
                        estado = "BOMBA DESACTIVADA"
                        #GPIO.output(32, GPIO.LOW)

        else:
            tierra_Status = "Humeda"

            print("-NO NECESITA RIEGO-")
            if estacion == 1:  # Verano
                if agua == 1:  # Reserva vacia
                    agua_Status = "Sin Agua"
                    print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")

            else:

                if agua == 1:  # Reserva vacia
                    agua_Status = "Sin Agua"
                    print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")
            estado = "BOMBA DESACTIVADA"
            #GPIO.output(32, GPIO.LOW)

        if dias == 3:
            #GPIO.output(32, GPIO.HIGH)
            print("-Dia 3, la bomba siempre se activa")
            #GPIO.output(32, GPIO.HIGH)
            estado = "BOMBA ACTIVADA"
            if agua == 1:  # Reserva vacia
                agua_Status = "Sin Agua"
                print("-LA BOMBA NO PUEDE TRABAJAR SI EL DEPOSITO ESTA VACIO-")
                #GPIO.output(32, GPIO.LOW)
                estado = "BOMBA DESACTIVADA"

        return(dia_actual, dia_actual_formato, hora_actual_formato, tierra_Status, agua_Status, estado)


riego = Riego()
tierra, agua, estacion = riego.lectura_sensor()
# --------------------------------------------------------
dias = 0
header = ['Dia', 'Hora', 'Tierra', 'Agua', 'Estación', 'Estado']
data = []

for i in range(3):
    dias +=1

    print("Dia: ", dias)
    print("***************************************")
    dia_actual, dia_actual_formato, hora_actual_formato, tierra_Status, agua_Status, estado = riego.control_riego(tierra, dias, agua, estacion)

    dia_actual = datetime.timedelta(days=1)
    print("\nFecha: ", dia_actual_formato, " - Hora: ", hora_actual_formato, "\nEstado :", estado , "\n")
    print("***************************************\n")
    if dias == 3:
        dias = 0




data.append(dia_actual_formato)
data.append(hora_actual_formato)
data.append(tierra_Status)
data.append(agua_Status)
data.append(estacion)
data.append(estado)

# --------------------------------------------------------

with open('data_riego.csv', 'a', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(header)
    writer.writerow(data)
    writer.writerow(data)



# pdf = FPDF()

# pdf.add_page()
# page_width = pdf.w - 2 * pdf.l_margin

# pdf.set_font('Times', 'B', 14.0)
# pdf.cell(page_width, 0.0, 'Historial de Riego', align='C')
# pdf.ln(10)

# pdf.set_font('Courier', '', 12)

# col_width = page_width/4

# pdf.ln(1)

# th = pdf.font_size

# for row in reader:
#     # print(row)
#     pdf.cell(col_width, th, str(row[0]), border=1)
#     pdf.cell(col_width, th, str(row[1]), border=1)
#     pdf.cell(col_width, th, str(row[2]), border=1)
#     pdf.cell(col_width, th, str(row[3]), border=1)
#     pdf.cell(col_width, th, str(row[4]), border=1)
#     pdf.cell(col_width, th, str(row[5]), border=1)
#     pdf.ln(th)

# pdf.ln(10)

# pdf.set_font('Times', '', 10.0)
# pdf.cell(page_width, 0.0, '- Fin fe Historial -', align='C')

# pdf.output('Historial de Riego.pdf', 'F')