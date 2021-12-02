"""

--- Day 2: Dive! ---

Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

"""

# Add the input file into a list
input_file = open('input.txt', 'r')
input_list = []

for line in input_file:
    # Get rid of new line characters in the list and split
    input_list.append(line.replace('\n', '').split())

# variable declarations
horizontal_position = 0
depth = 0
aim = 0

for i in range(len(input_list)):
    if input_list[i][0] == 'forward':
        horizontal_position += int(input_list[i][1])
        depth += aim * int(input_list[i][1])
    elif input_list[i][0] == 'down':
        aim += int(input_list[i][1])
    else:
        aim -= int(input_list[i][1])

print('The product of my final horizontal position and my final depth is', horizontal_position * depth)

