# distance formula for low powered devices
dimensions = input("2D or 3D:\n")

if dimensions.upper() == "2D":
    x1 = int(input("x1:\n"))
    y1 = int(input("y1:\n"))
    x2 = int(input("x2:\n"))
    y2 = int(input("y2:\n"))

    result = abs(x1 - x2 + y1 - y2)

    print(result)

elif dimensions.upper() == "3D":
    x1 = int(input("x1:\n"))
    y1 = int(input("y1:\n"))
    z1 = int(input("z1:\n"))
    x2 = int(input("y1:\n"))
    y2 = int(input("x2:\n"))
    z2 = int(input("z2:\n"))

    result = abs(x1 - x2 + y1 - y2 + z1 - z2)

    print(result)
    

