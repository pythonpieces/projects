# strings - working with textual data

message = "pieces of py"  # this is a string stored in a variable called message

print(message)

print(len(message)) # len prints the length of our message. here the len = 12

print(message[0]) # index of our string. in this case 'p' is in our first position.

print(message[0:4]) # prints our a range. in this case 'piec' is printed.

print(message.upper())

print(message.lower())

print(message.count('p')) # count a number in our string. 'p' is in our string 2 times.

print(message.find('piece')) # what we want to find. 'piece' is at our 0 index

# formatted strings

greeting = "Hello"
name = "Jonathan"

# concatenate string. not the best method. adds a + sign.
new_message = greeting + ", " + name + " Welcome"

# using the .format method
new_message = "{}, {}. Welcome!".format(greeting, name)

# preferred new method called 'f' string in 3.6 and up.
new_message = f"{greeting}, {name}. Welcome!"
new_message = f"{greeting}, {name.upper}. Welcome!" # .upper gives uppercase and .lower gives lowercase

print(new_message)