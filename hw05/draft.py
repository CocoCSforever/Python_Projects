def main():
    MIN_HOUR_CONVERSION = 60
    HOUR_DAY_CONVERSION = 24
    WATT_PER_MINUTE = 1000
    GALLONS_PER_MINUTE = 2
    WATT_KWH_CONVERSION = 1000*60
    WATT_FOR_5GALLONS = 5/GALLONS_PER_MINUTE*WATT_PER_MINUTE
    WATT_FOR_100GALLONS = 100/GALLONS_PER_MINUTE*WATT_PER_MINUTE
    PRECISION = 3

    file_name = input("Please enter the file name: ")
    # try to open the file and print message when user
    # entered an invalid file name
    try:
        file = open(file_name, "r", encoding="utf-8")
    except FileNotFoundError as e:
        print(f"Unable to open {file_name}")
        return

    lines_list = [int(i) for i in file.read().split()]

    # data covered hours and days
    cover_hours = len(lines_list)/MIN_HOUR_CONVERSION
    cover_days = cover_hours/HOUR_DAY_CONVERSION

    # total watt, kwhs, running minutes and produced water
    total_watt = 0
    running_minutes = 0
    index = 0
    minute_5_gallons = -1
    minute_10_gallons = -1

    # extra credit for continuation
    list_of_continuation = []
    continued_minutes = 0
    for i in lines_list:
        total_watt += i
        if (i > 1):
            continued_minutes += 1
        else:
            if (continued_minutes >= 120):
                list_of_continuation.append([continued_minutes, index-continued_minutes])
            continued_minutes = 0
        # lines_list[index] = total_watt
        if (total_watt >= WATT_FOR_5GALLONS and minute_5_gallons == -1):
            minute_5_gallons = index + 1
        if (total_watt >= WATT_FOR_5GALLONS and minute_5_gallons == -1):
            minute_5_gallons = index + 1
        index += 1
    running_minutes = total_watt/WATT_PER_MINUTE
    producing_gallons = running_minutes * GALLONS_PER_MINUTE
    total_kWh = total_watt/WATT_KWH_CONVERSION

    # need to round to 3 decimal places
    print(f"""Data covers a total of {cover_hours} hours
(That's {cover_days} days)

Pump was running for {running_minutes} minutes, producing \
{producing_gallons} gallons
(That's 336.0 gallons per day)

Pump required a total of {total_watt} watt minutes of power
That's {total_kWh} kWh

It took {minute_5_gallons} minutes of data to reach 5 gallons.
It took {minute_10_gallons} minutes of data to reach 100 gallons.
""")


main()
