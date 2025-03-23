# 3.1 Calculate seconds in an hour
seconds_in_minute = 60
minutes_in_hour = 60
seconds_in_hour = seconds_in_minute * minutes_in_hour
print(f"3.1 Seconds in an hour: {seconds_in_hour}")

# 3.2 Assign to variable seconds_per_hour
seconds_per_hour = seconds_in_hour
print(f"3.2 seconds_per_hour: {seconds_per_hour}")

# 3.3 Calculate seconds in a day using seconds_per_hour
hours_in_day = 24
seconds_in_day = hours_in_day * seconds_per_hour
print(f"3.3 Seconds in a day: {seconds_in_day}")

# 3.4 Save seconds per day in variable
seconds_per_day = seconds_in_day
print(f"3.4 seconds_per_day: {seconds_per_day}")

# 3.5 Floating-point division
float_division = seconds_per_day / seconds_per_hour
print(f"3.5 seconds_per_day / seconds_per_hour (float division): {float_division}")

# 3.6 Integer division
integer_division = seconds_per_day // seconds_per_hour
print(f"3.6 seconds_per_day // seconds_per_hour (integer division): {integer_division}")