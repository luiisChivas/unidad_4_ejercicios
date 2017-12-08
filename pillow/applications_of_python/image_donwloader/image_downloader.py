""""Author: Juan Luis Mendiola Gutiérrez
            Juan Pablo Ramírez Ibarra
     email: jlmg67815@gmail.com
            pablo.ram232@gmail.com """
import random
import urllib.request


def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request  .urlretrieve(url, full_name)


download_web_image("https://images8.alphacoders.com/397/thumb-1920-397110.jpg")