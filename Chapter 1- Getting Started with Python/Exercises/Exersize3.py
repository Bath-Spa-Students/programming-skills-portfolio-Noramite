from datetime import datetime

current = datetime.today()
time = datetime.now()

# Cosmetic changes that make the Date appear in text form instead of just numbers
DMY = current.strftime ("%d %B, %Y")
time = time.strftime ("%I:%M %p")

print ("The Date Today is", DMY)
print ("The time right now is", time)