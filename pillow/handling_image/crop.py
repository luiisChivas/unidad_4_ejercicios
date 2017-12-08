""""Author: Juan Luis Mendiola Gutiérrez
            Juan Pablo Ramírez Ibarra
     email: jlmg67815@gmail.com
            pablo.ram232@gmail.com """
from PIL import Image

img = Image.open("img/charger.jpg")

area = (100, 100, 200, 200)

cropped_img = img.crop(area)

cropped_img.show()