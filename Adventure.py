######################################################################################################################
# Name: 
# Date: 
# Description: See GAME INSTRUCTIONS below.
######################################################################################################################
# **functions section**

# define the game instructions.
def displayIntro():
	print "GAME INSTRUCTIONS:"
	print "You have invited Gourd to your mansion for his birthday."
	print "You have items all over the mansion that you must collect to make him a birthday cake."
	print "You MUST collect all the items and enter into the kitchen to make his cake."
	print "If you have all the items then 'You Get Cake!'."
	print "If you don't have all the items then 'No Cake For You!!' and you lose."
	print "If you accidentally go out the hidden exit then 'No Cake For You!!' and you lose."


displayIntro() # print the game instructions.

# define cake and print drawing of a cake if you enter the kitchen with all items.
def cake():
	print " " * 10 + "(" * 1 + ")" * 1
	print " " * 10 + "|" * 1 + "|" * 1
	print " " * 7 + "*" * 8
	print " " * 7 + "|" * 1 + " " * 6 + "|" * 1
	print " " * 7 + "|" * 1 + " " * 1 + "C" * 1 + "A" * 1 + "K" * 1 + "E" * 1 + " " * 1 + "|" * 1
	print " " * 7 + "|" * 1 + " " * 6 + "|" * 1
	print " " * 7 + "*" * 8


# the blueprint for a room
class Room(object):

	def __init__(self, name):
		self.name = name
		self.exits = []
		self.exitLocations = []
		self.items = []
		self.itemDescriptions = []
		self.grabbables = []

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@property
	def exits(self):
		return self._exits

	@exits.setter
	def exits(self, value):
		self._exits = value

	@property
	def exitLocations(self):
		return self._exitLocations

	@exitLocations.setter
	def exitLocations(self, value):
		self._exitLocations = value

	@property
	def items(self):
		return self._items

	@items.setter
	def items(self, value):
		self._items = value

	@property
	def itemDescriptions(self):
		return self._itemDescriptions

	@itemDescriptions.setter
	def itemDescriptions(self, value):
		self._itemDescriptions = value

	@property
	def grabbables(self):
		return self._grabbables

	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value

	# add an exit to the Room
	def addExit(self, exit, room):
		# append the exit and room to the list
		self._exits.append(exit)
		self._exitLocations.append(room)

	# add item to the Room
	def addItem(self, item, desc):
		# append the item and desc to the list
		self._items.append(item)
		self._itemDescriptions.append(desc)

	# add grabbable to the Room
	def addGrabbable(self, item):
		# append the item to list
		self._grabbables.append(item)

	# remove grabbable item from the Room
	def delGrabbable(self, item):
		# remove the item from list
		self._grabbables.remove(item)

	# returns a string desc of the Room
	def __str__(self):
		# first, the room Name
		s = "You are in {} .\n".format(self.name)

		# next, the exits from the Room
		s += "You see: "
		for item in self.items:
			s += item + " "
		s += "\n"

		# next, the exits from the Room
		s += "Exits: "
		for exit in self.exits:
			s += exit + " "

		return s


# creates the Rooms
def createRooms():
	global currentRoom

	# create the rooms and give names
	r1 = Room("Foyer")
	r2 = Room("LivingRoom")
	r3 = Room("Study")
	r4 = Room("DiningRoom")

	# add exits to Room 1
	r1.addExit("east", r2)  # to the east of room 1 is room 2
	r1.addExit("south", r3)
	# add grabbables to room 1
	r1.addGrabbable("icing")  # this is where you would add if you needed to find items to do a Cake
	# add items to room 1
	r1.addItem("bench", "It is made of oak. A can of cake ICING rests on it.")

	# add exits to room 2
	r2.addExit("west", r1)
	r2.addExit("south", r4)
	# add grabbables to room 2
	r2.addGrabbable("candle")
	r2.addGrabbable("matches")
	# add items to room 2
	r2.addItem("mantle", "Above the fireplace is a hand carved mantle. There's a CANDLE resting on it.")
	r2.addItem("fireplace", "It is full of ashes. There's a box of MATCHES sitting next to the fireplace.")

	# add exits to Study
	r3.addExit("north", r1)
	r3.addExit("east", r4)
	r3.addExit("south", True)  # You get a cake!
	# add grabbables to Study
	r3.addGrabbable("knife")
	r3.addGrabbable("plate")
	r3.addGrabbable("fork")
	# add items to Study
	r3.addItem("bookshelves", "A PLATE and FORK is on the shelves.")
	r3.addItem("desk", "The statue is resting on it. So is a KNIFE.")

	# add exits to room 4
	r4.addExit("north", r2)
	r4.addExit("west", r3)
	r4.addExit("south", None)  # No cake for you!
	# add graabbables to room 4
	r4.addGrabbable("cake-mix")
	# add items to room 4
	r4.addItem("table", "Gourd is ready to eat his cake. He has a box of CAKE-MIX sitting on the table.")
	# set room 1 as the current room at the beginning of the game
	currentRoom = r1


############################################################################################
# **main program**
# START THE GAME
inventory = []  # nothing is in the inventory yet
createRooms()  # create the rooms

# play forever
while (True):
	status = "{}\n You are carrying: {}\n".format(currentRoom, inventory)

	if (currentRoom == None):
		status = "You left Gourd through a hidden exit. No cake for you!!"
	if (currentRoom == True):
		status = "You found the kitchen. You get cake!!"
		cake() # print the cake image

	print "======================================="
	print status

	# if the player is in the room that says None, the player will not get cake
	# if the player is in the room that says True, the player gets cake
	if (currentRoom == None):
		if (currentRoom == True):
			break

	# prompt for user input
	action = raw_input("What to do? ")

	# set the user's input to lowercase ti make it easier to compare the verb and noun to known values
	action = action.lower()

	# exit the game if the player wants to leave (supports quit, exit, and bye)
	if (action == "quit" or action == "exit" or action == "bye"):
		break

	# set a default response
	response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
	# split the user input into words (words are seperated by spaces)
	words = action.split()

	# the game only understands two word inputs
	if (len(words) == 2):
		# isolate the verb and noun
		verb = words[0]
		noun = words[1]

		# the verb is: go
		if (verb == "go"):
			# set a default response
			response = "Invalid exit."

			# check for valid exits in the current room that you are in
			for i in range(len(currentRoom.exits)):
				# a valid exit is found
				if (noun == currentRoom.exits[i]):
					# change the current room to the one that is associated with the specified exit
					currentRoom = currentRoom.exitLocations[i]

					# set the response (success)
					response = "Room changed."

					# no need to check any more Exits
					break

		# the verb is: look
		elif (verb == "look"):
			# set a default response
			response = "I don't see that item."

			# check for valid items in the current room
			for i in range(len(currentRoom.items)):
				# a valid item is found
				if (noun == currentRoom.items[i]):
					# set the response to the item's Description
					response = currentRoom.itemDescriptions[i]

					# no need to check any more items
					break

		# the verb is: take
		elif (verb == "take"):
			# set a default response
			response = "I don't see that item."

			# check for a valid grabbable items in the current room
			for grabbable in currentRoom.grabbables:
				# a valid grabbable item is found
				if (noun == grabbable):
					# add the grabbable item to the player's inventory
					inventory.append(grabbable)

					# remove the grabbable item from the room
					currentRoom.delGrabbable(grabbable)

					# set the response (success)
					response = "Item grabbed."

					# no need to check any more grabbable items
					break

	# display the response
	print "\n{}".format(response)
