import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def sendmail(file):

    contenido ='''
    Saludos,

    Este es un correo por parte del sistema de riego automatico Green Drops.

    Adjunto se encuentra el Historial de Riego.





    Atentamente
    Green Drops - Sistema de Riego automatico'''

    # The mail addresses and password
    sender_address = 'rafael.fzurita@gmail.com'
    sender_pass = 'armando2001'
    receiver_address = 'armando.zuritaa@gmail.com'

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Historial de Riego'

    # The body and the attachments for the mail
    message.attach(MIMEText(contenido, 'plain'))

    # PDF
    pdfname = file

    # Open the file as binary mode
    bynary_pdf = open('Historial.pdf', 'rb')
    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    payload.set_payload((bynary_pdf).read())

    # encode the attachment
    encoders.encode_base64(payload)

    # add payload header with filename
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    message.attach(payload)

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    print('Correo Enviado')

def run():

    file = 'Historial.pdf'
    sendmail(file)

if __name__ == '__main__':
    run()