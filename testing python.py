# Try adding print statements to look at the values of variables inside
# the remove function.  See if you can find out what's making it give
# silly answers such as remove('ding', 'do') -> 'dining'.

def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)
    length = len(sub)
    if(sub not in somestring):
      return somestring
    part_before = somestring[:location]
    part_after = somestring[location + length:]
    return part_before + part_after
print(remove('audacity', 'a'))
print(remove('ding', 'do'))
