""""Author: Juan Luis Mendiola Gutiérrez
            Juan Pablo Ramírez Ibarra
     email: jlmg67815@gmail.com
            pablo.ram232@gmail.com """
from PIL import Image

img = Image.open("img/charger2.jpg")

r,g,b = img.split()

r.show()
g.show()
b.show()