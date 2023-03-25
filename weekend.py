# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
  return day.lower() == 'saturday' or day.lower() == 'sunday'

print(weekend("monday"))
print(weekend("June"))
print(weekend("SUNDAY"))
print(weekend("SaTURdaY"))
print(weekend("november"))
