from peewee import *


db = SqliteDatabase('challenges.db')

class Challenge(Model):
    name = CharField(max_length=100)
    language = CharField(max_length=100)

    class Meta:
        database = db
        
from models import Challenge

all_challenges = Challenge.select()

Challenge.create(language="Ruby", name="Booleans")

sorted_challenges = Challenge.select().order_by(Challenge.steps.asc())

##########

from peewee import *

db = SqliteDatabase('challenges.db')


class Challenge(Model):
    name = CharField(max_length=100)
    language = CharField(max_length=100)
    steps = IntegerField(default=1)
    
    class Meta:
      database = db
      
def initialize():
  db.connect()
  db.create_tables([Challenge], safe=True)
  
##############
## Menu Items:
# 'n', 'new challenge'
# 's', 'new step'
# 'd', 'delete a challenge'
# 'e', 'edit a challenge'

from collections import OrderedDict

menu = OrderedDict([
  ('n', 'new challenge'),
  ('s', 'new step'),
  ('d', 'delete a challenge'),
  ('e', 'edit a challenge')
  ])
  
  #########
  
#  Create a function named create_challenge() that takes name, language, and steps arguments. Steps should be optional, so give it a default value of 1. Create a Challenge from the arguments. create_challenge should not return anything.

from models import Challenge

def create_challenge(name, language, steps=1):
  Challenge.create(
    name=name,
    language=language,
    steps=steps
  )
  
#Create a function named search_challenges that takes two arguments, name and language. Return all Challenges where the name field contains name argument and the language field is equal to the language argument. Use == for equality. You don't need boolean and or binary & for this, just put both conditions in your where().

from models import Challenge


def create_challenge(name, language, steps=1):
    Challenge.create(name=name,
                     language=language,
                     steps=steps)


def search_challenges(name_query, language):
    entries = Challenge.select().where(Challenge.name.contains(name_query)).where(Challenge.language==language)
  
from models import Challenge


def create_challenge(name, language, steps=1):
    Challenge.create(name=name,
                     language=language,
                     steps=steps)


def search_challenges(name, language):
    return Challenge.select().where(
        Challenge.name.contains(name),
        Challenge.language==language
    )
    
#Create a function named delete_challenge that takes a Challenge as an argument. Delete the specified Challenge. Your function shouldn't return anything.
from models import Challenge


def create_challenge(name, language, steps=1):
    Challenge.create(name=name,
                     language=language,
                     steps=steps)


def search_challenges(name, language):
    return Challenge.select().where(
        Challenge.name.contains(name),
        Challenge.language==language
    )
  
def delete_challenge(challenge):
  challenge.delete_instance()





