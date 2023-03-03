import os

os.system("clear")

mass = float(input("mass (in grams):\n"))
diameter = float(input("diameter (in meters)\n"))

print(str(4 / 3 * 3.1415 * ((0.133302e-12 * ((mass / diameter) / (0.266955e-12 * (mass / diameter ** 2)))) / 2) ** 3) + " cubic meters")