def tr_area(h, b1, b2):
    return (b1 + b2) * h / 2
h, b1, b2 = int(input("Height: ")), int(input("Base, first value: ")), int(input("Base, second value: "))
area = tr_area(h, b1, b2)
print("Expected output:", area)

