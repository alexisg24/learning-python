from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
from string import Template


# plantilla = """
#     <b>Bienvenido! $usuario</b>
# """

# template = Template(plantilla)
# cuerpo_html = template.substitute({"usuario": "Chanchito feliz"})
html = Path("./11-paquetes-nativos/plantilla.html").read_text("utf-8")
template = Template(html)
cuerpo_html = template.substitute(usuario="Chanchito feliz")


image_path = Path("...imagepath.png")
mime_image = MIMEImage(image_path.read_bytes())

mensaje = MIMEMultipart()
mensaje["from"] = "Hola Mundo"
mensaje["to"] = "ultimatepython@holamundo.io"
mensaje["subject"] = "Esta es una prueba"
cuerpo = MIMEText(cuerpo_html, "html")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # iniciamos
    smtp.starttls()  # codificamos la conexion

    smtp.login("correo", "passowrd")
    smtp.send_message(mensaje)
