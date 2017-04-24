import copy

import pyperclip as pyperclip

_author_ = "Rifatul Islam"

# Multiple assignment trick
a, b = 'Alice', 'Bob'
print(a, b)
a, b = b, a
print(a, b)

# Passing values without references
spam = ['A', 'B', 'C', 'D']
inbox = copy.copy(spam)
inbox[2] = "2"
print("Spam:", spam)
print("Inbox:", inbox)

# Dictionaries in python
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'] + myCat['color'])

for v in myCat.values():
    print(v)

for k in myCat.keys():
    print(k)

for i in myCat.items():
    print(i)

# Fantasy Game Inventory
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']


def display_inventory(inventory):
    total = 0
    for key, value in inventory.items():
        print(value, " ", key)
        total += value
    print("Initial Total: ", total)


display_inventory(stuff)


def add_to_inventory(inventory, list_of_items):
    for item in list_of_items:
        if item in inventory.keys():
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1

    print("With blessings from Dragon Total: ", sum(inventory.values()))


add_to_inventory(stuff, dragonLoot)

# String operation
comma_separated = ', '.join(['cats', 'rats', 'bats'])
print(comma_separated)

splited_string = 'My name is Simon'.split()
print(splited_string)

char_wise_spl_string = 'My name is Simon'.split('m')  # This will split the string whenever a 'm' is encountered
print(char_wise_spl_string)
'Hello'.ljust(20, '-')  # Justified String with -

spam = '    Hello World     '
print(spam.strip())
print(spam.rstrip())
print(spam.lstrip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('Spam'))

pyperclip.paste()
pyperclip.copy('This will copied to the system clipboard')

