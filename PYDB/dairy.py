#!/usr/bin/env python3

from collections import OrderedDict
import datetime
import sys
import os

from peewee import *

db = MySQLDatabase('python_db',host="localhost", port=3306, user='root')


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default = datetime.datetime.now)
    
    class Meta:
        database = db
        
def initialise():
    db.connect()
    db.create_tables([Entry], safe=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_loop():
    """show the menu"""
    choice = None
    
    while choice != 'q':
        clear()
        print('Entry "q" to quit')
        for key, value in menu.items():
            print('{}) {}'.format(key,value.__doc__))
        choice = input('Action: ').lower().strip()
        
        if choice in menu:
            clear()
            menu[choice]()
    
def add_entry():
    """add an entry"""
    print('enter your entry, press ctrl+ when finished')
    data = sys.stdin.read().strip()
    
    if data:
        if input('Save entry? (Y/n) ').lower() != 'n':
            Entry.create(content=data)
            print('Entry saved')
    
def view_entries(search_query=None):
    """show entry list """
    entries = Entry.select().order_by(Entry.timestamp.desc())
    
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))
    
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d %Y %H:%M%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('n) next entry')
        print('d) delete entry')
        print('q) rerurn to main menu')
        next_action = input('Action: [Ndq] ').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)
    
def search_entries():
    """Search entries for a string."""
    view_entries(input('Search query: '))

def delete_entry(entry):
    """delete an entry"""
    if input('Are you sure? (y/n)').lower() == 'y':
        entry.delete_instance()
        print('Entry deleted')

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries)
])

if __name__ == '__main__':
    initialise()
    menu_loop()