time_sec = int(input("Enter number of seconds > "))
time_min = time_sec//60
time_secost = time_sec%60
time_hour = time_min/60
time_hour = float('{:.1f}'.format(time_hour))

print(f"{time_hour}:{time_min}:{time_secost}")
