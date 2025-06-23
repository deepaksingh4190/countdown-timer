import time

my_time = int(input("Enter the time in seconds: "))
# iterating loop for reverse countdown
for x in range(my_time,0,-1):
# taking seconds by modulus having 60 seconds
    seconds = x % 60
# taking minutes having 60 seconds
    minutes = int(x / 60) % 60
# taking hours having 3600 seconds
    hours = int(x / 3600)
# printing the countdown 
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
# taking the setup of timer
    time.sleep(3)
# output result
print("Good Morning!")