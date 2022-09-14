items = ["Roger", "Shally", 1, True, "Syd"]
print("Roger" in items)
#A list can also be defined as empty:
#items = []
#items[0] = "Roger"
#Get the number of items contained in a list
len(items)
print("{}".format(len(items)))
#You can add items to the list by using a list append()
items.append("Test")
#or the extend() method
items.extend(["Test"])
#You can also use the += operator
items += ["Test"]
#Remove an item using the remove() method:
items.remove("Test")
#You can add multiple elements using
items += ["Test1", "Test2"]
#or
items.extend(["Test1", "Test2"])
#To add an item in the middle of a list, at a specific
#index, use the insert() method
items.insert(2, "Draft")
