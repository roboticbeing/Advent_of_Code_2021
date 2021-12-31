"""

--- Day 3: Binary Diagnostic ---

"""


def find_rating(rating):
    # Add the input file into a list
    input_file = open('input.txt', 'r')
    input_list = []

    for line in input_file:
        # Get rid of new line characters in the list
        input_list.append(line.replace('\n', ''))

    # variable declarations
    position = 0
    least_common_bit = ''
    most_common_bit = ''

    # Loop through every character in the binary number
    while position <= len(input_list[0]):
        zero_count = 0
        one_count = 0

        if len(input_list) == 1:
            return input_list[0]

        # Loop through all the numbers to find the most common bit
        for i in range(len(input_list)):
            if input_list[i][position] == '1':
                one_count += 1
            elif input_list[i][position] == '0':
                zero_count += 1

        if zero_count > one_count:
            least_common_bit = '1'
            most_common_bit = '0'
        else:
            least_common_bit = '0'
            most_common_bit = '1'

        # Loop through all the numbers again to remove the least/most common bit from the list
        # iterate over the list in reverse order to avoid index out of range issues when deleting items
        for i in range(len(input_list) - 1, -1, -1):
            if rating == 'oxygen':
                if input_list[i][position] == most_common_bit:
                    del input_list[i]
            elif rating == 'co2':
                if input_list[i][position] == least_common_bit:
                    del input_list[i]

        position += 1


print("The life support rating of the submarine is", int(find_rating('oxygen'), 2) * int(find_rating('co2'), 2))
