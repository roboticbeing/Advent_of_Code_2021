"""

--- Day 3: Binary Diagnostic ---

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate
and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all
numbers in the diagnostic report.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each
position is used.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them
together. What is the power consumption of the submarine?

"""

# Add the input file into a list
input_file = open('input.txt', 'r')
input_list = []

for line in input_file:
    # Get rid of new line characters in the list
    input_list.append(line.replace('\n', ''))

# variable declarations
position = 0
gamma_rate = ''
epsilon_rate = ''

# Loop through every character in the binary number
while position < len(input_list[0]):
    zero_count = 0
    one_count = 0
    # this is to avoid the TypeError: list indices must be integers or slices, not str
    for i in range(len(input_list)):
        # the second square brackets refers to the character (because it's a string), that's so cool! i love python
        if input_list[i][position] == '1':
            one_count += 1
        else:
            zero_count += 1
    if one_count > zero_count:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'
    position += 1

# converts from binary to decimal
print('The power consumption of the submarine is', int(gamma_rate, 2) * int(epsilon_rate, 2))

