""" 
organizational tool for programmers

1 - Never Unpack More Than Three Variables When Functions Return Multiple Values
"""

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
minimum, maximum = get_stats(lengths) # Two return values
print(f'Min: {minimum}, Max: {maximum}')