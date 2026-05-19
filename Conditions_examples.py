from datetime import datetime

print("Current time: ", datetime.now().strftime("%H:%M:%S"))

now= datetime.now()
hour = now.hour

print("Hour now is: ", hour)
print(f"the hour now is {hour} o'clock")

if hour < 16:
    print("Good day")
elif hour < 20:
    print("Good evening")
else:
    print("Good night")

    if hour != 19:
        print("It's not noon")
    else:        print("It's noon")