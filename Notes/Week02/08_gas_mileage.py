# Gas mileage program

def main():
    PRECISION = 3
    miles = float(input("Enter the number of miles:"))
    gallons = float(input("Enter the gallons of fuel used:"))

    mpg = round(miles/gallons, PRECISION)

    print("Miles per gallon:", mpg)
    print(f"Miles per gallon: {mpg}")


main()
