""""Author: Juan Luis Mendiola Gutiérrez
            Juan Pablo Ramírez Ibarra
     email: jlmg67815@gmail.com
            pablo.ram232@gmail.com """
from urllib import request

google_stocks = 'https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv'


def donwload_stock_data(url):
    reponse = request.urlopen(url)
    csv = reponse.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'forestfires.csv'
    fx = open(dest_url, "w")

    for line in lines:
        fx.write(line + "\n")

    fx.close()


donwload_stock_data(google_stocks)

