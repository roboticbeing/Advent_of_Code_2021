"""


--- Part Two ---

In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0.
The commands also mean something entirely different than you first thought:

down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
- It increases your horizontal position by X units.
- It increases your depth by your aim multiplied by X.

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

