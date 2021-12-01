"""

--- Day 1: Sonar Sweep ---

As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor.
On a small screen, the sonar sweep report (your puzzle input) appears:
each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with
- you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement.
(There is no measurement before the first measurement.)

"""

# Add the input file into a list
input_file = open('input.txt', 'r')
input_list = []
count = 0

for line in input_file:
    # Get rid of new line characters in the list and cast to int
    input_list.append(int(line.replace('\n', '')))

# Python way of working with indexes
for index, val in enumerate(input_list):
    if index == 0:
        print(val, ' (N/A - no previous measurement)')
    elif input_list[index] < input_list[index - 1]:
        print(val, ' (decreased)')
    else:
        print(val, ' (increased)')
        count += 1

print("The total of measurements larger than the previous measurement is ", count)




