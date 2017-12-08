""""Author: Juan Luis Mendiola Gutiérrez
            Juan Pablo Ramírez Ibarra
     email: jlmg67815@gmail.com
            pablo.ram232@gmail.com """
from PIL import Image

img = Image.open("img/a.jpg")

"""square = img.resize((250,250))
square.show()
flip = img.transpose(Image.FLIP_LEFT_RIGHT)
flip = img.transpose(Image.FLIP_TOP_BOTTOM)
flip.show()

spin = img.transpose(Image.ROTATE_90)"""

spin = img.transpose(Image.ROTATE_270)

spin.show()