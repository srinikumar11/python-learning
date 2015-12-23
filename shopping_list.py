# Make a list to hold on Items
shopping_list = []
# Print out instreuction
print("What shoud we pick up from store? ")
print("Enter 'DONE' to stop adding items.")

while True:
    # ask for new item
    new_item = input("> ")
    # be able to quit the app
    if(new_item.upper() == "DONE"):
        break
        
    # add new item to our list
    shopping_list.append(new_item)

# print out the list
print("here is your list:")
for item in shopping_list:
    print(item)
    
