import math

# calculates force of gravity on an object! :)
grams = float(input("mass (grams):\n"))
area = float(input("surface area (meters):\n"))
meters = 2 * math.sqrt(area / (4 * math.pi))
result = 0.266955e-12 * (grams / meters ** 2)
print(str(result) + " meters per second squared")
