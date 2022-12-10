class Room:
    # def __init__(self, roomName, north, east, south, west, locked, item):
    #     self.roomName = roomName
    #     self.north = north
    #     self.east = east
    #     self.west = west
    #     self.south = south
    #     self.locked = locked
    #     self.item = item

    def __init__(self, roomName, locked, item):
        self.roomName = roomName
        self.locked = locked
        self.item = item
        self.availableDirections = []

# Create a list of room objects for game map
def createRooms():
    # rooms.append(Room('Surveillance Center', '', 'Bunk Room', '', '', False, 'Blueprints'))
    # rooms.append(Room('Bunk Room', '', 'Torture Chamber', 'Dining Room', 'Surveillance Center', False, 'Cellphone'))
    # rooms.append(Room('Torture Chamber', '', '', '', 'Bunk Room', False, 'Cleaver'))
    # rooms.append(Room('Kitchen', '', 'Dining Room', '', '', False, ''))
    # rooms.append(Room('Dining Room', 'Bunk Room', 'Bathroom', 'Master Bedroom', 'Kitchen', False, 'Coins'))
    # rooms.append(Room('Bathroom', '', '', '', 'Dining Room', False, 'Key'))
    # rooms.append(Room('Master Bedroom', 'Dining Room', 'Weapon Room', '', '', True, 'Nuclear Device'))
    # rooms.append(Room('Weapon Room', '', '', '', 'Master Bedroom', True, ''))

    # TODO should rooms directions point to other room objects like below instead
    surveillanceCenter = Room('Surveillance Center', False, 'Blueprints')
    bunkRoom = Room('Bunk Room', False, 'Cellphone')
    tortureChamber = Room('Torture Chamber', False, 'Cleaver')
    kitchen = Room('Kitchen', False, '')
    diningRoom = Room('Dining Room', False, 'Bag of Coins')
    bathroom = Room('Bathroom', False, 'Key')
    masterBedroom = Room('Master Bedroom', True, 'Nuclear Device')
    weaponRoom = Room('Weapon Room', True, '')

    # Add possible paths for each room and update list of rooms
    surveillanceCenter.east = bunkRoom
    rooms.append(surveillanceCenter)

    bunkRoom.west = surveillanceCenter
    bunkRoom.east = tortureChamber
    bunkRoom.south = diningRoom
    rooms.append(bunkRoom)

    tortureChamber.west = bunkRoom
    rooms.append(tortureChamber)

    kitchen.east = diningRoom
    rooms.append(kitchen)

    diningRoom.north = bunkRoom
    diningRoom.east = bathroom
    diningRoom.south = masterBedroom
    diningRoom.west = kitchen
    rooms.append(diningRoom)

    bathroom.west = diningRoom
    rooms.append(bathroom)

    masterBedroom.north = diningRoom
    masterBedroom.east = weaponRoom
    rooms.append(masterBedroom)

    weaponRoom.west = masterBedroom
    rooms.append(weaponRoom)
# Function to print intro
def printIntro():
    print('Dragon Text Adventure Game\n')
    print('Collect 6 items to win the game, or be eaten by the dragon.')
    print('Move commands: go South, go North, go East, go West')
    print('Add to Inventory: get \'item name\' ')

possibleDirectionChoices = ('go North', 'go East', 'go South', 'go West')
possibleItemChoices = []
gameItems = ('Key', 'Nuclear Device', 'Cellphone', 'Blueprints', 'Bag of Coins', 'Cleaver')
rooms = []

isOn = True
playerInventory = []

# Set up *************************************************

# printIntro()
createRooms()

# Create list of possible item choices
for item in gameItems:
    possibleItemChoices.append('get ' + item)

# Set player location to the starting point / the kitchen
for room in rooms:
    if room.roomName == 'Kitchen':
        playerLocation = room

# Main game loop *****************************************
while (isOn):
    # Print player location
    print(f'\nYou are in the {playerLocation.roomName}')

    # Print player inventory
    print('Inventory : ', end='')
    print(playerInventory)

    # Print any items in room
    if (playerLocation.item != ''):
        print(f'You see a {playerLocation.item}')

    # Print organizational lines
    print('---------------------------')

    playerChoice = input('Enter your move:\n')

    # If player chooses to move a valid direction, move player
    if playerChoice in possibleDirectionChoices:
        # Are unlock requirements met TODO
        # Master Bedroom and Weapon room have unlock requirements
        # TODO add better comments to explain here

        # Move player
        match playerChoice:
            case 'go North':
                try:
                    playerLocation = playerLocation.north
                except AttributeError:
                    print('There is no room to the North')
            case 'go East':
                try:
                    if playerLocation.east.roomName == 'Weapon Room':
                        if 'Coins' in playerInventory:
                            playerLocation = playerLocation.east
                            #TODO add endgame stuff here
                        else:
                            print('You need to obtain coins to distract the guard.')

                    playerLocation = playerLocation.east
                except AttributeError:
                    print('There is no room to the East')
            case 'go South':
                # Is the south available and are unlock requirements met
                try:
                    # Master Bedroom is only accessible from Dining Room's South
                    if (playerLocation.south.roomName == 'Master Bedroom'):
                        # The player can only enter this room once they obtain the key
                        if ('Key' in playerInventory):
                            playerLocation = playerLocation.south
                        else:
                            print('You need to obtain a key in order to access this room.')
                    else:
                        playerLocation = playerLocation.south
                except AttributeError:
                    print('There is no room to the south')
                    pass

                # only masterbedroom and weapon room have reqs

            case 'go West':
                try:
                    playerLocation = playerLocation.west
                except AttributeError:
                    print('There is no room to the West')
    # TODO remove unlocked variable from room class and objects
    # Else if player chooses to retrieve an item, acquire the item
    elif playerChoice in possibleItemChoices:
        # Update player's inventory and remove item from room
        chosenItem = playerChoice[4:]
        if playerLocation.item == chosenItem:
            playerInventory.append(chosenItem)
            print(f'{chosenItem} retrieved!')
        else:
            print(f'Can\'t get {chosenItem}!')
        playerLocation.item = ''

    else:
        print('Invalid Input!')



#test but dont on



