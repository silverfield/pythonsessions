__author__ = 'ferrard'

for i in range(6):
    print("fdsfds")

print(i)
exit()

from datetime import datetime
import time

print("Current time: " + str(datetime.now()))
print("Current hour: " + str(datetime.now()))
print("Current minute: " + str(datetime.now().minute))
print("Current second: " + str(datetime.now().second))

while datetime.now().second != 59:
    print("Current second: " + str(datetime.now().second))
    time.sleep(0.5)
print("New minute is coming!")