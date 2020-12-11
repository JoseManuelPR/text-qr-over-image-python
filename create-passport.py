from PIL import Image, ImageFont, ImageDraw 
import qrcode
import random
import numpy as np
import pyshorteners as ps

#Enlace para QR de Pasaporte AGROS
origin_url = "https://pasaporte.agros.tech/identidad/bd04227a-89f3-4aae-b1b9-dc712deadc4f"
#link_decode = ps.Shortener().tinyurl.short(origin_url)

#Creando la instancia del QR
qr = qrcode.QRCode(
        version=1,
        box_size=8,
        border=0)
qr.add_data(origin_url)
qr.make(fit=True)
qr_passport_code = qr.make_image(fill='black', back_color='white').convert("RGBA")

front_passport_image = Image.open("template/front-credential.png")
back_passport_image = Image.open("template/back-credential.png")

#Nombres
name_text = "Segundo Santos"
name_size = len(name_text)
if name_size <= 25 : 
    name_font = ImageFont.truetype('font/Montserrat-Bold.ttf', 45)
else :
    name_font = ImageFont.truetype('font/Montserrat-Bold.ttf', 35)

#Apellidos
surname_text = "Valladolid Garavito"
surname_size = len(surname_text)
if surname_size <= 25 : 
    surname_font = ImageFont.truetype('font/Montserrat-Bold.ttf', 45)
else :
    surname_font = ImageFont.truetype('font/Montserrat-Bold.ttf', 35)

#DNI
dni_text = "03377706"
dni_font = ImageFont.truetype('font/Montserrat-Regular.ttf', 30)

#Ciudad
city_text = "Chulucanas"
city_font = ImageFont.truetype('font/Montserrat-Regular.ttf', 30)

front_passport_image_editable = ImageDraw.Draw(front_passport_image)
front_passport_image_editable.text((390,252), name_text, (74, 86, 37), font=name_font)
front_passport_image_editable.text((390,312), surname_text, (74, 86, 37), font=surname_font)
front_passport_image_editable.text((463,432), dni_text, (0, 0, 0), font=dni_font)
front_passport_image_editable.text((514,520), city_text, (0, 0, 0), font=city_font)
front_passport_image.paste(qr_passport_code, (55,258), qr_passport_code)

#Codigo
code_font = ImageFont.truetype('font/Montserrat-Bold.ttf', 40)
code_text = str(random.randint(1111,9999))

back_passport_image_editable = ImageDraw.Draw(back_passport_image)
back_passport_image_editable.text((500,325), code_text, (0, 0, 0), font=code_font)

front_passport_image.save("credentials/pasaporte-agros-front.png")
back_passport_image.save("credentials/pasaporte-agros-back.png")