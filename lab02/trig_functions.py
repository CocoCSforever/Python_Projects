import math

def main():
    angle=float(input("Enter an angle:"))
    degree_in_radians=math.radians(angle)
    cos_d=math.cos(degree_in_radians)
    sin_d=math.sin(degree_in_radians)
    print(f"The cosine of {angle} is {cos_d}\nThe sine of {angle} is {sin_d}")

main()