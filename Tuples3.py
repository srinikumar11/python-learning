#Tuple has a fixed type of memory. will be used while programming with memory management

# Tuples
my_tuples = (1,2,3)
#(1, 2, 3)

my_tuples_new = 4, 5, 6
#(4, 5, 6)

my_third_tuple = tuple([6,7,8])
#(6, 7, 8)

my_third_tupe[2]
#8

>>> my_third_tupe[2] = 2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

#Tuple Packing And Unpacking
#Combining values, making multiple variables, and having smarter return values from functions. One of the most common design patterns in Python.
# This is called symultaneous assignmet

a,b = 1,2
# >>> a
# 1
# >>> b
# 2
# >>> a+b
# 3
# >>>
c = 2, 3 # packing `c` with 2,3
#>>> c
#(2, 3)
d,e = c # unpacking `c` and assigning it d & e respectivly
#>>> d
#2
#>>> e
#3
#>>> 
f = d,e # packing d & e to f
# >>> f
# (2, 3)
f == c
# True
# >>>
###### Swaping variable values
# >>> del a
# >>> del b
a, b = 1,2
# >>> a
# 1
# >>> b
# 2
# >>> a,b
# (1, 2)
a,b = b,a
# >>> a,b
# (2, 1)
# >>>

def myfunc():
    return 1,2,3

myfunc()
#(1, 2, 3)
tup = myfunc()
#>>> tup
#(1, 2, 3)
x,y,z = myfunc()
#>>> x
#1
#>>> y
#2
#>>> z
#3
#>>> 

#Create a function named stringcases that takes a string and returns a tuple of four versions of the string: uppercased, lowercased, titlecased (where every word's first letter is capitalized), and a reversed version of the string.

# Handy functions:
# .upper() - uppercases a string
# .lower() - lowercases a string
# .title() - titlecases a string
# There is no function to reverse a string.
# Maybe you can do it with a slice?

def stringcases(string):
    return string.upper(), string.lower(), string.title(), string[::-1]

stringcases('srini')
#('SRINI', 'srini', 'Srini', 'inirs')

my_alphabet = list('abcdefghijklmnopqrstuvwxyz')
count = 0
for letter in my_alphabet:
    print("{}: {}".format(count, letter))
    count += 1
# 0: a
# 1: b
# 2: c
# 3: d
# 4: e
# 5: f
# 6: g
# 7: h
# 8: i
# 9: j
# 10: k
# 11: l
# 12: m
# 13: n
# 14: o
# 15: p
# 16: q
# 17: r
# 18: s
# 19: t
# 20: u
# 21: v
# 22: w
# 23: x
# 24: y
# 25: z

# enumerate will return index, loop item
for index, letter in enumerate(my_alphabet):
    print("{}: {}".format(index, letter))
# 0: a
# 1: b
# 2: c
# 3: d
# 4: e
# 5: f
# 6: g
# 7: h
# 8: i
# 9: j
# 10: k
# 11: l
# 12: m
# 13: n
# 14: o
# 15: p
# 16: q
# 17: r
# 18: s
# 19: t
# 20: u
# 21: v
# 22: w
# 23: x
# 24: y
# 25: z

for step in enumerate(my_alphabet):
    print("{}: {}".format(step[0], step[1]))
    
# 0: a
# 1: b
# 2: c
# 3: d
# 4: e
# 5: f
# 6: g
# 7: h
# 8: i
# 9: j
# 10: k
# 11: l
# 12: m
# 13: n
# 14: o
# 15: p
# 16: q
# 17: r
# 18: s
# 19: t
# 20: u
# 21: v
# 22: w
# 23: x
# 24: y
# 25: z

for step in enumerate(my_alphabet):
    print("{}: {}".format(*step))
# 0: a
# 1: b
# 2: c
# 3: d
# 4: e
# 5: f
# 6: g
# 7: h
# 8: i
# 9: j
# 10: k
# 11: l
# 12: m
# 13: n
# 14: o
# 15: p
# 16: q
# 17: r
# 18: s
# 19: t
# 20: u
# 21: v
# 22: w
# 23: x
# 24: y
# 25: z

# Create a function named combo() that takes two iterables and returns a list of tuples. Each tuple should hold the first item in each list, then the second set, then the third, and so on. Assume the iterables will be the same length.

# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]
# If you use .append(), you'll want to pass it a tuple of new values.

def combo(a, b):
    tuple_list = []
    a = list(a)
    b = list(b)
    count = 0
    for item in a:
        tuple_list.append((item, b[count]))
        count +=1
    return tuple_list
# Run
combo([1, 2, 3], 'abc')    
# [(1, 'a'), (2, 'b'), (3, 'c')]
        
    



# Create a function named nchoices() that takes an iterable and an integer. The function should return a list of n random items from the iterable where n is the integer. Duplicates are allowed.

import random
def nchoices(arg_list, arg_int):
    new_list = []
    arg_list = list(arg_list)
    while True:
        choice = random.choice(arg_list)
        new_list.append(choice)        
        if(len(new_list) == arg_int):
            break
    return new_list
            
nchoices(arg_list, 4)

##### Example tuple not to be used
from game import Game
class GameScore(Game):
  def __str__(self):
    return "Player 1: {}; Player 2: {}".format(*self.score)
    
