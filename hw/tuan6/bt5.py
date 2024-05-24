from datetime import datetime


curr = datetime.now()
print(curr)

print(curr.strftime('Today is %d/%m/%y'))
print(curr.strftime('Time right now: %H:%M:%S'))
