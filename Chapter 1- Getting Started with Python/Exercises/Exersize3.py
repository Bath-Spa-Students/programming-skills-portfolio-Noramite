from datetime import date

current = date.today()

# Cosmetic changes that make the Date appear in text form instead of just numbers
DMY = current.strftime ("%d %B, %Y")

print ("The Date Today is", DMY)