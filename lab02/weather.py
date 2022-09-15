highest_temp=75
lowest_temp=50
diff_hi_to_lo=highest_temp-lowest_temp
average_temp=(61+59+60+63+65+66+67+64+65+69)/10
conver_fahr_to_celsius=round((75-32)*5/9,2)
print("The difference between the highest and the lowest temperature values predicted for the 10 day forecast is", diff_hi_to_lo, "Fahrenheit.")
print(f"The average temperature at noon predicted for the 10 day forecast is {average_temp} Fahrenheit.")
print(f"the highest temperature predicted for the 10 day forecast is {conver_fahr_to_celsius} Celsius.")