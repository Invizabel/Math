# calculates force of gravity on an object! :)
grams = float(input("mass (grams):\n"))
meters = float(input("diameter (meters):\n"))
result = 0.266955e-12 * (grams / meters ** 2)
print(str(result) + " meters per second squared")
