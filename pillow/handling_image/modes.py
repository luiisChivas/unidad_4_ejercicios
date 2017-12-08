""""Author: Juan Luis Mendiola Gutiérrez
            Juan Pablo Ramírez Ibarra
     email: jlmg67815@gmail.com
            pablo.ram232@gmail.com """
from PIL import Image
from PIL import ImageFilter

img = Image.open("img/charger.jpg")

"""
black_white = img.convert('L')
black_white.show()

blur = img.filter(ImageFilter.BLUR)
blur.show()

"""

edges = img.filter(ImageFilter.FIND_EDGES)
edges.show()