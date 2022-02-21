from base64 import encode
import csv
from encodings import utf_8
import pandas as pd
import pdfkit


class File:

    def save_data(data):

        with open('data_riego.csv', 'a', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(data)

    def covert_file():
        
        CSV = pd.read_csv('data_riego.csv')
        CSV.to_html('data_riego.html')

        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        pdfkit.from_file('data_riego.html', 'Historial.pdf', configuration=config)

#pdfkit.from_file('data_riego.html', 'Historial.pdf', options=options)
