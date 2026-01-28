#Create a dictionary of items and quantities. Update the quantity when an item is sold.
def sell_item(items, item_name, quantity_sold):
    if item_name in items:
        items[item_name] -= quantity_sold

        if items[item_name] < 0:
            items[item_name] = 0

        else:
            print(" sorry item not found")

store = {
    "pen": 20,
    "book":199,
    "pencil": 15
    
}

sell_item(store, "book",3)
print(store)

#Given a dictionary of names and ages, print only those who are eligible to vote.
def eligible_voters(people):
    for name, age in people.items():
        if age >= 18:
            print(name)
ages = {
    "Reva": 20,
    "mike": 16,
    "finn": 22,
    "wolfhard": 17
}

eligible_voters(ages)
