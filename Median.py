# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

def median(a, b, c):
  return sorted((a, b, c))[1]

print(median(10,4,6))
