from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

plantilla = Path("modulos-nativos/plantilla.html").read_text("utf-8")
template = Template(plantilla)
# cuerpo = template.substitute({"usuario": "user02456654"})
cuerpo = template.substitute(usuario="user02456654")

path = Path("ruta de la imagen")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Brian"
mensaje["to"] = "brianbentancourt9@gmail.com"
mensaje["subject"] = "Esta es una prueba"

cuerpo = MIMEText("Cuerpo del mensaje", "html")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("gmail user", "gmail password")
    smtp.send_message(mensaje)
    print("Mensaje enviado")
