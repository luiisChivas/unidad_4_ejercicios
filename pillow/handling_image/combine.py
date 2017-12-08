""""Author: Juan Luis Mendiola Gutiérrez
            Juan Pablo Ramírez Ibarra
     email: jlmg67815@gmail.com
            pablo.ram232@gmail.com """
from PIL import Image

img = Image.open("img/charger.jpg")
img2 = Image.open("img/charger2.jpg")

area = (100, 100, 400, 300)
region = img.crop(area)
img2.paste(region, area)
img2.show()