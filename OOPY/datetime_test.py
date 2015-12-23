import datetime


def minutes(time1, time2):
  diff = time2 - time1
  return round(diff.seconds/60)
  
  
now = datetime.datetime.now()
date = now - datetime.timedelta(minutes=-2)
now1 = datetime.datetime.now()

diff = now1 - now
diff.seconds/60

# >>> now
# datetime.datetime(2015, 12, 22, 16, 45, 34, 402595)
now.strftime("%B")
# 'December'
now.strftime("%m/%d/%Y")
#'12/22/2015'
strDatetime = now.strftime("%m/%d/%Y")
datetime.datetime.strptime(strDatetime,'%m/%d/%Y')
#datetime.datetime(2015, 12, 22, 0, 0)

date1 = datetime.datetime(2015, 12, 22)
time1 = datetime.time( 10, 35, 45)
datetime.datetime.combine(date1, time1)

import datetime


def time_tang(date, time):
    return datetime.datetime.combine(date, time)


## Examples
# to_string(datetime_object) => "24 September 2012"
# from_string("09/24/12 18:30", "%m/%d/%y %H:%M") => datetime

import datetime


def to_string(datetime_obj):
  return datetime_obj.strftime('%d %B %Y')


def from_string(date_str, format_str):
  datetime_obj = datetime.datetime.strptime(date_str, format_str)
  return datetime_obj.strftime(format_str)
  
def from_string(date_str, format_str):
  return datetime.datetime.strptime(date_str, format_str)
  
import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def delorean(integer):
  return starter + datetime.timedelta(hours = integer)
  
  
import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)


#Write a function named time_machine that takes an integer and a string of "minutes", "hours", "days", or "years". This describes a timedelta. Return a datetime that is the timedelta's duration from the starter datetime.
# Remember, you can't set "years" on a timedelta!
# Consider a year to be 365 days.

## Example
# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)

def time_machine(integer, string):
  if string == 'years' or string == 'days':
    integer = 365 * integer
    delta = datetime.timedelta(days = integer)
  elif string == 'minutes':
    delta = datetime.timedelta(minutes = integer)
  elif string == 'hours':
    delta = datetime.timedelta(hours = integer)
  else:
    print("invalid")
  return starter + delta
  