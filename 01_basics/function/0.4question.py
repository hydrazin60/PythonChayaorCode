r = int(input("Enter a Radius of circle: "))

def calculation(r):
    pi = 3.14  # Approximate value of pi
    area = pi * r * r  # Calculate the area of the circle
    circumference = 2 * pi * r  # Calculate the circumference of the circle
    pi = 3.14
    area  =pi *r*r
    circumference = 2*pi*r
    return area, circumference
 
area, circumference  = calculation(r)
print("Area of circle is: ",  area)
