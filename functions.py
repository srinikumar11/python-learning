def hows_the_parrot():
    print("He's pining for the fjords!")

hows_the_parrot()

def lumberjack(name):
    if(name.lower() == "srini"):
        print("{} you are a good person!!".format(name))
    else:
        print("{} will do alright".format(name))

lumberjack("Srini")
lumberjack("Rom")

def average(num1, num2):
    return (num1+num2) / 2

avg = average(2, 4)

print(avg)

  
def printer(count):
    while count:
        print("Hi")
        count -= 1

printer(10)

def product(arg1, arg2):
    return (arg1 * arg2)

retval = product(10,20)
print(retval)


# EXAMPLES
# squared(5) would return 25
# squared("2") would return 4
# squared("tim") would return "timtimtim"

def squared(arg):
    try:
        num = int(arg)
        return num * num
    except ValueError:
        return arg * len(arg)


my_list = list(range(20))
#first 4 items
print(my_list[:4])
#last 4 items
print(my_list[-4:])
#odd index items
print(my_list[1::2])


my_list_new = [1,2,'a','b','c', 'd',3,5,'f','g','h',6,7,8,'i']

#remove first 2 elements
del my_list_new[0:2]
#['a', 'b', 'c', 'd', 3, 5, 'f', 'g', 'h', 6, 7, 8, 'i'

#replace elements from index 4 - 6 
my_list_new[4:6] = ['e','f']
#['a', 'b', 'c', 'd', 'e', 'f', 'f', 'g', 'h', 6, 7, 8, 'i']

#replacing with empty list from 8 - 11
my_list_new[8:11] = []
#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


#When replacing a slice with another iterable, they must be the same size. - Not need be in the same size
# LIST[start:stop:step]

# When replacing a slice with another iterable, they must be the same size. = [::-1] will reverse the list


#Create a function named sillycase that takes a string and returns that string with the first half lowercased and the last half uppercased.

# The first half of the string, rounded with round(), should be lowercased.
# The second half should be uppercased.
# E.g. "Treehouse" should come back as "treeHOUSE"

def sillycase(arg):
  mid =int(round(len(arg)/2))
  return arg[:mid].lower()+arg[mid:].upper()