def main():
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))

    # Set up necessary constants for calculation
    BASE_RATE = 208
    MULTI = 0.7
    # Use a list to store percentages of each zone
    percentage = [0.5, 0.6, 0.7, 0.8, 0.93, 1]

    # Use equation to get max rate and rate reserve
    max_heart_rate = BASE_RATE - MULTI * age
    reserve = max_heart_rate - restHR

    print("=======================================")
    print(f"Your heart rate reserve is: {reserve} bpm\n\
Here is a breakdown of your training zones:")
    # Use for-loop to print heart rate in 5 zones
    # Round result to two decimal places
    # Guarantee the lowest value is 0.01 greater than previous highest value
    for i in range(5):
        if (i < 4):
            print(f"Zone {i+1}: \
{round(restHR + reserve * percentage[i], 2)} to \
{round(restHR + reserve * percentage[i+1] - 0.01, 2)} \
bpm")
        else:
            print(f"Zone {i+1}: \
{round(restHR + reserve * percentage[i], 2)} to \
{round(restHR + reserve * percentage[i+1], 2)} bpm")


main()
