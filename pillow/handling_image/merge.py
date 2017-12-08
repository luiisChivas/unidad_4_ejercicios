""""Author: Juan Luis Mendiola Gutiérrez
            Juan Pablo Ramírez Ibarra
     email: jlmg67815@gmail.com
            pablo.ram232@gmail.com """
from PIL import Image

img = Image.open("img/a.jpg")
r, g, b = img.split()
print(img.size)

""" new_img = Image.merge("RGB", (r,g,b)) """
"""new_img = Image.merge("RGB", (b,g,r))
new_img.show()"""

img1 = Image.open("img/b.jpg")
r1, g1, b1 = img1.split()
new_img = Image.merge("RGB", (b1, g, r1))
new_img.show()