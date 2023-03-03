import os

os.system("clear")

grams = float(input("mass (grams):\n"))
meters = float(input("diameter (meters):\n"))

print(str(0.266955e-12 * (grams / meters ** 2)) + " meters per second squared")