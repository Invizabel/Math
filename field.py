# measures the electro-magnetic field or gravitational field of a sphere, not sure which one! :)
mass = float(input("mass (in grams):\n"))
diameter = float(input("diameter (in meters)\n"))
result = 4 / 3 * 3.1415 * ((0.133302e-12 * ((mass / diameter) / (0.266955e-12 * (mass / diameter ** 2)))) / 2) ** 3
print(str(result) + " cubic meters")
