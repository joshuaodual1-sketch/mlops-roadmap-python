cal = input("Expression:" ).strip()
x, y, z = cal.split()
x1 = float(x)
z1 = float(z)


if y == "+":
    result = x1 + z1
elif y == "-":
    result = x1 - z1
elif y == "*":
    result = x1 * z1
elif y == "/":
    result = x1 / z1


print(f"{result:.1f}")