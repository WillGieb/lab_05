#Programmers: Brett Bonner, Will Gieb

# Course: CS151, Mehri

# Date: 10/20

# Lab Number: 5

# Program Inputs: Length, Width, floor_option

# Program Outputs: total_cost

# **Intro Comments**


# determines if the input is valid for floor option and returns true if valid
def valid_floor_option(floor_option):
    if floor_option == "hardwood" or floor_option == "carpet" or floor_option == "tile":
        return True
    else:
        return False


# returns the rate of the different floor options
def get_cost_per_sqft(floor_option):
    if floor_option == "hardwood":
        return 1.39
    elif floor_option == "carpet":
        return 3.99
    elif floor_option == "tile":
        return 4.99


# gets the cost for one room
def get_cost_per_room(length, width, floor_option):
    return length * width * get_cost_per_sqft(floor_option)


# menu for the user to see the different floor options
def menu():
    print("Floor Options \n\t\tHardwood \n\t\tCarpet \n\t\tTile")


# askes the user for the length, width, and floor option. returns the cost of the one room if the length and width
# are greater then 0 and if valid_floor_option is true. Else the function returns -1
def process_room():
    length = float(input("Please enter the length of the room: "))
    width = float(input("Please enter the width of the room: "))
    menu()
    floor_option = input("Please enter the floor type you would like: ")
    floor_option = floor_option.lower().strip()
    if length > 0 and width > 0:
        if valid_floor_option(floor_option):
            return get_cost_per_room(length, width, floor_option)
        else:
            return -1
    else:
        return -1


# while the count is less then 5, process_room() function is called to calculate the cost for a room, and adds one to
# the room count, if room_cost = -1 it tells the user there is an invalid input and the program breaks
def main():
    room_count = 0
    total_cost = 0
    invalid = True
    while room_count < 5:
        room_cost = process_room()
        if room_cost != -1:
            total_cost = room_cost + total_cost
            room_count += 1
        elif invalid:
            print("Invalid input, run program again!")
            break
            # allows the user to see the total price after each rooms price is calculated
        print("The total cost is: $ ", round(total_cost, 2))


main()

