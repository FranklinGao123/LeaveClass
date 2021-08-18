import pyautogui, datetime, time

print("Move your mouse to your desired location in 5 second")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
x, y = pyautogui.position()

year = int(input("What is today's year:"))
month = int(input("What is today's month:"))
day = int(input("What is today's day (number):"))
hour = int(input("What hour do you want to leave (24h):"))
minute = int(input("What minute do you want to leave (24h):"))
print("Please put the right window infront")
print("Waiting for Time...")

#Year, Month, Day, Hour, Min
while True:
	if datetime.datetime.today() >= datetime.datetime(year, month, day, hour, minute):
		break
pyautogui.click(x,y)
print("Left Meeting at "+str(hour)+":"+str(minute)+" on "+str(month)+"/"+str(day)+"/"+str(year))