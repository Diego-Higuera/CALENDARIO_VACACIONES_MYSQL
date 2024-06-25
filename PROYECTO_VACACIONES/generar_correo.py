import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, recipient_email, subject, body, pdf_path):
    # Crear un objeto MIMEMultipart
    msg = MIMEMultipart()

    # Configurar los parámetros básicos del correo
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Adjuntar el cuerpo del correo
    msg.attach(MIMEText(body, 'plain'))

    # Leer el archivo PDF y adjuntarlo
    filename = 'calendario_anual.pdf'  # Nombre del archivo PDF adjunto
    with open(pdf_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {filename}")
        msg.attach(part)

    # Conectar al servidor SMTP y enviar el correo
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        print('Correo enviado exitosamente')
    except Exception as e:
        print(f'Error al enviar el correo: {e}')
    finally:
        server.quit()
        

# Configuración del correo
sender_email = 'tu_correo@gmail.com'
sender_password = 'tu_contrasena'
recipient_email = 'correo_destinatario@gmail.com'
subject = 'Asunto del correo'
body = 'Cuerpo del correo'
pdf_path = 'calendario_anual.pdf'

# Enviar el correo
send_email(sender_email, sender_password, recipient_email, subject, body, pdf_path)

#TERMINADO EL 25/06/2024
#DIEGO HIGUERA TRIGUERO