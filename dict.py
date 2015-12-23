#Introduction To Dictionaries

# You can check for dictionary membership using the
# "key in dict" syntax from lists.

### Example
# my_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
# my_list = ['apples', 'coconuts', 'grapes', 'strawberries']
# members(my_dict, my_list) => 2

my_dict = {'name':"Srinivasan", 'last':"kumar"}
my_dict['name']
my_dict['age'] #will throw KeyError - when we access a key that does not exist
my_dict['age'] = 34
#{'age': 34, 'last': 'kumar', 'name': 'Srinivasan'}
my_dict['names']={'first_name':'Srinivasan', }
my_dict['names']['last_name']='Kumar'
#{'age': 34, 'last': 'kumar', 'name': 'Srinivasan', 'names': {'first_name': 'Srinivasan', 'last_name': 'Kumar'}}

my_dict.update({'name': 'Srini', 'age': 33, 'job': 'learner'})
# my_dict = {'name':"Srinivasan", 'last':"kumar"}
# my_dict.update({'name': 'Srini', 'age': 33, 'job': 'learner'})
# {'age': 33, 'job': 'learner', 'last': 'kumar', 'name': 'Srini'}


def members(my_dict, my_list):
    count = 0
    for item in my_list:
      try:
        val = my_dict[item]
        count +=1
      except KeyError:
        continue
    return count
    
# E.g. word_count("I am that I am") gets back a dictionary like:
# {'i': 2, 'am': 2, 'that': 1}
# Lowercase the string to make it easier.
# Using .split() on the sentence will give you a list of words.
# In a for loop of that list, you'll have a word that you can
# check for inclusion in the dict (with "if word in dict"-style syntax).
# Or add it to the dict with something like word_dict[word] = 1.

def word_count(arg):
  input_string = arg.lower()
  word_list = input_string.split(" ")
  my_dict = {};
  for word in word_list:
    try:
      word_exisit = my_dict[word]
      my_dict[word] = int(my_dict[word]) + 1
    except KeyError:
      my_dict[word] = 1
  return my_dict
  
#################
my_string = "Hi! my name is {name}, I live in {place}"
my_string.format({'name': 'Srinivasan', 'place': 'Ambattur'})
  # Traceback (most recent call last):
  #   File "<stdin>", line 1, in <module>
  # KeyError: 'name'
  # >>>
my_string.format(name='Srinivasan', place='Ambattur')
#'Hi! my name is Srinivasan, I live in Ambattur'

my_string.format(place='Ambattur',name='Srinivasan')
#'Hi! my name is Srinivasan, I live in Ambattur'

my_dict = {'name': 'Srinivasan', 'place': 'Ambattur'}
my_string.format(**my_dict)
'Hi! my name is Srinivasan, I live in Ambattur'

my_string.format(**{'name': 'Srinivasan', 'place': 'Ambattur'})
'Hi! my name is Srinivasan, I live in Ambattur'

  
  

#Create a function named string_factory that accepts a list of dictionaries and a string. Return a new list build by using .format() on the string, filled in by each of the dictionaries in the list.

dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(dicts, string):
    new_list = []
    for item in dicts:
      new_string = string.format(**item)
      new_list.append(new_string)
    return new_list
    
string_factory(dicts, string)
#["Hi, I'm Michelangelo and I love to eat PIZZA!", "Hi, I'm Garfield and I love to eat lasanga!", "Hi, I'm Walter and I love to eat pancakes!", "Hi, I'm Galactus and I love to eat worlds!"]


# Looping dictionaries
my_dict = {'age': 33, 'job': 'learner', 'last': 'kumar', 'name': 'Srini'}

# Looping using keys
for thing in my_dict:
    # thing -> key in a dict
    print(my_dict[thing]) 
    
# looping over values
for value in my_dict.values():
    print(value)
    
    
#Challenge Task 1 of 4

# Create a function named most_classes that takes a dictionary of teachers. Each key is a teacher's name and their value is a list of classes they've taught. most_classes should return the teacher with the most classes.
# The dictionary will be something like:
teacher_dict = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'], 'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.

def most_classes(dicts):
    teacher = {}
    max_count = 0
    for key in dicts:
        if max_count < len(dicts[key]):
            teacher = key
            max_count = len(dicts[key])
    return teacher

most_classes(teacher_dict)
    
#Next, create a function named num_teachers that takes the same dictionary of teachers and classes. Return the total number of teachers.

def num_teachers(dicts):
  total_num = 0
  for key in dicts:
    total_num += 1
  return total_num
    
#Now, create a function named stats that takes the teacher dictionary. Return a list of lists in the format [<teacher name>, <number of classes>]. For example, one item in the list would be ['Dave McFarland', 1].

def stats(dicts):
    stats = []
    for key in dicts:
        stats.append([key, len(dicts[key])])
    return stats

#Great work! Finally, write a function named courses that takes the teachers dictionary. It should return a single list of all of the courses offered by all of the teachers.

def courses(dicts):
    courses_list = []
    for key in dicts:
        courses_list = courses_list+dicts[key]
    return courses_list
    
my_dict = {'age': 33, 'last': 'kumar', 'job': 'learner', 'name': 'Srini'}
for key, value in my_dict.items():
    print("{}: {}".format(key, value))

# age: 33
# last: kumar
# job: learner
# name: Srini