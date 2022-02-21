import csv
from riego_noPi_V3 import Riego as riego

def save_in_file():
    
    with open('data_riego.csv', 'a', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(header)
        writer.writerow(data)
        writer.writerow(data)


header = ['Dia', 'Hora', 'Tierra', 'Agua', 'Estación', 'Estado']
data = []


tierra, agua, estacion = riego.lectura_sensor()
hora_actual_formato, dia_actual_formato, estado = riego.control_riego(tierra, dias, agua, estacion)

data.append(dia_actual_formato)
data.append(hora_actual_formato)
data.append(tierra)
data.append(agua)
data.append(estacion)
data.append(estado)


CSV = pd.read_csv('data_riego.csv')
CSV.to_html('data_riego.html')

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
pdfkit.from_file('data_riego.html', 'Historial.pdf', configuration=config)