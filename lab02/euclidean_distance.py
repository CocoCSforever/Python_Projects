import math

def main():
    a=float(input("Enter x1 for the first point:"))
    b=float(input("Enter y1 for the first point:"))
    c=float(input("Enter x2 for the Second point:"))
    d=float(input("Enter y2 for the Second point:"))

    distance_x_square=(a-c)**2
    distance_y_square=(b-d)**2
    res=math.sqrt(distance_x_square+distance_y_square)
    print(f"The euclidean distance between ({a},{b}) and ({c},{d}) is {res}")
main()



