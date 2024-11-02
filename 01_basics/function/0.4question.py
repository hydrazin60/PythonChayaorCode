r = int(input("Enter a Radius of circle: "))
def calculation(r):
    area = 3.14 * r * r
    circumference = 2 * 3.14 * r
    return area, circumference

area, circumference = calculation(r)

print("Area of circle is: ", area)
print("Circumference of circle is: ", circumference)
