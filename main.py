import pandas
import numpy as np

excel_file = "mjerenja.xlsx"
sheet = pandas.read_excel(excel_file)

idealni_pomak = 25.0
print(f"Idealni pomak: {idealni_pomak} mikrometara")

print()

pomaci = sheet.iloc[:, 1].to_list()

prosjecni_pomak = round(sum(pomaci) / len(pomaci), 5)
print(f"Prosječni pomak: {prosjecni_pomak} mikrometara")

tocnost_pomaka = round(abs(prosjecni_pomak - idealni_pomak), 5)
print(f"Točnost pomaka: {tocnost_pomaka} mikrometara")

print()

devijacija = np.std(pomaci)
print(f"Devijacija pomaka: {devijacija} mikrometara")