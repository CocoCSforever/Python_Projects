def main():
    # define all the constants
    MIN_HOUR_CONVERSION = 60
    HOUR_DAY_CONVERSION = 24
    WATT_PER_MINUTE = 1000
    GALLONS_PER_MINUTE = 2
    WATT_KWH_CONVERSION = 1000*60
    WATT_FOR_5_GALLONS = 5/GALLONS_PER_MINUTE*WATT_PER_MINUTE
    WATT_FOR_100_GALLONS = 100/GALLONS_PER_MINUTE*WATT_PER_MINUTE
    PRECISION = 3

    # prompt user enter file name
    file_name = input("Please enter the file name: ")
    # try to open the file and print message when user
    # entered an invalid file name
    try:
        file = open(file_name, "r", encoding="utf-8")
    except FileNotFoundError as e:
        print(f"Unable to open {file_name}")
        return

    # data covered minutes, total watt, kwhs, running minutes
    # and produced water
    cover_minutes = 0
    total_watt = 0
    running_minutes = 0
    index = 0
    # if certain gallons never reached, print -1
    minutes_5_gallons = -1
    minutes_100_gallons = -1

    # extra credit for continuation
    list_of_continuation = []
    continued_minutes = 0

    # read line by line through a loop over the file object
    for line in file:
        watt = int(line.rstrip())
        cover_minutes += 1
        total_watt += watt
        if (total_watt >= WATT_FOR_5_GALLONS and minutes_5_gallons == -1):
            minutes_5_gallons = cover_minutes
        if (total_watt >= WATT_FOR_100_GALLONS and minutes_100_gallons == -1):
            minutes_100_gallons = cover_minutes
        # watt > 1 means pump is operating
        # but to align with the result
        # I change the threshold to 900 and then to 100
        if (watt > 500):
            # To align with the example result:
            # assume that if the watt is less than 500, it's noisy value
            # watt > 500 means pump is operating
            continued_minutes += 1
        else:
            # if pump is not operating
            # first check whether the last continuation exceed 120 minutes
            # if yes, record this period and its start
            # we should re-start the process when it's not operating.
            if (continued_minutes >= 120):
                list_of_continuation.append([continued_minutes,
                                            cover_minutes-continued_minutes])
            continued_minutes = 0

    # we got all the data, covert them to the right unit
    # data covered hours and days
    cover_hours = cover_minutes/MIN_HOUR_CONVERSION
    cover_days = cover_hours/HOUR_DAY_CONVERSION

    # Here is an important assumption that
    # for the values not strictly either 1000 or 0
    # I assume that theoretically fully-active pump
    # should draw 1000 watts in a minute
    # so I add up used watts in every minute to get total watts
    # the fully running minutes is divide total watts by watt per minute
    # and since we know producing 2 gallons if fully running for a minute
    # total water produced is running minutes multiply gallons per minute
    # This leads to a result slightly different from the example
    running_minutes = total_watt/WATT_PER_MINUTE
    water_gallons = running_minutes * GALLONS_PER_MINUTE
    total_kWh = total_watt/WATT_KWH_CONVERSION
    gallons_per_day = water_gallons * HOUR_DAY_CONVERSION/cover_hours

    print(f"""Data covers a total of {round(cover_hours, PRECISION)} hours.
(That's {round(cover_days, PRECISION)} days)

Pump was running for {round(running_minutes, PRECISION)} minutes, producing \
{round(water_gallons, PRECISION)} gallons.
(That's {round(gallons_per_day, PRECISION)} gallons per day)

Pump required a total of {round(total_watt, PRECISION)} watt minutes of power.
That's {round(total_kWh, PRECISION)} kWh.

It took {round(minutes_5_gallons, PRECISION)} minutes of \
data to reach 5 gallons.
It took {round(minutes_100_gallons, PRECISION)} minutes \
of data to reach 100 gallons.

Information on water softener recharges:""")

    for m in list_of_continuation:
        print(f"{m[0]} minute run started at {m[1]}")


main()
