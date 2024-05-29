# I am using the book: Effective Python


# I - Use list comprehension instead of map or filter : derive a list from a sequence

import itertools
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list of squares of even numbers in a
squares = [x**2 for x in a if x % 2 == 0]
print(squares)  # [4, 16, 36, 64, 100]

# Dictionaries and sets have their own equivalents of list comprehensions
# (called dictionary comprehensions and set comprehensions,
# respectively). These make it easy to create other types of derivative
# data structures when writing algorithms

cubes_set = {x**3 for x in a}
print(cubes_set)  # {64, 1, 512, 8, 1000, 343, 216, 729, 27, 125}

odd_squares_dict = {x: x**2 for x in a if x % 2 == 1}
print(odd_squares_dict)  # {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}


""" 
Things to Remember

✦ List comprehensions are clearer than the map and filter built-in
functions because they don't require lambda expressions.
✦ List comprehensions allow you to easily skip items from the input
list, a behavior that map doesn't support without help from filter.
✦ Dictionaries and sets may also be created using comprehensions.
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

squared = [[x**2 for x in row] for row in matrix]
print(squared)  # [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

# flatten squared list of lists with itertool
print(list(itertools.chain(*squared)))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

""" 
Things to Remember
✦ Comprehensions support multiple levels of loops and multiple conditions per
loop level.
✦ Comprehensions with more than two control subexpressions are
very difficult to read and should be avoided.
"""

# Exercise

""" 
 I'm writing a program to manage
orders for a fastener company. As new orders come in from customers,
I need to be able to tell them whether I can fulfill their orders. I need
to verify that a request is sufficiently in stock and above the minimum 
threshold for shipping (in batches of 8)
"""

stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}
order = ['screws', 'wingnuts', 'clips']

# first method


def get_batches(count, size):
    return count // size


result = {}

for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches

print(result)  # {'screws': 4, 'wingnuts': 1}

# second method with dict comprehension
found = {name: get_batches(stock.get(name, 0), 8)
         for name in order
         if get_batches(stock.get(name, 0), 8)}

print(found)  # {'screws': 4, 'wingnuts': 1}

""" 
Although this code is more compact, the problem with it is that the
get_batches(stock.get(name, 0), 8) expression is repeated. This
hurts readability by adding visual noise that's technically unnecessary. 
It also increases the likelihood of introducing a bug if the two
expressions aren't kept in sync.


An easy solution to these problems is to use the walrus operator (:=),
which was introduced in Python 3.8, to form an assignment expression as 
part of the comprehension (see Item 10: “Prevent Repetition
with Assignment Expressions” for background):
"""

found = {name: batches for name in order if (
    batches := get_batches(stock.get(name, 0), 8))}
