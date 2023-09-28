from datetime import date
from datetime import datetime

current = date.today()
time = datetime.now()

# Cosmetic changes that make the Date appear in text form instead of just numbers
DMY = current.strftime ("%d %B, %Y")
time = time.strftime ("%H:%M.%S")

print ("The Date Today is", DMY)
print ("The time right now is", time)