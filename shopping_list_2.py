# have a help command
# have a show command

# Make a list to hold on Items
shopping_list = []
def show_help():
    # Print out instreuction
    print("What shoud we pick up from store? ")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'SHOW' to see your list
    """)
  
show_help()

#print out the list
def show_list():
    print("here is your list:")
    for item in shopping_list:
        print(item)
    
def add_to_list(item):
      # add new item to our list
    shopping_list.append(item)
    print("Addded {}. List now has {} items".format(item, len(shopping_list)))
    
    
while True:
    # ask for new item
    new_item = input("> ")
    # be able to quit the app
    if(new_item.upper() == "DONE"):
        break
    elif new_item.lower() == "help":
        show_help()
        continue
    elif new_item.lower() == "show":
        show_list()
        continue
    add_to_list(new_item)
        
show_list()
