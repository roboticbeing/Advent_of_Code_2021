"""

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the
previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough
measurements left to create a new three-measurement sum.

"""

# Add the input file into a list
input_file = open('input.txt', 'r')
input_list = []
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']

for line in input_file:
    # Get rid of new line characters in the list and cast to int
    input_list.append(int(line.replace('\n', '')))

# variable declarations
count = 0
start = 0
end = 3
prev_sum = 0

# while not at the end of list
while end != len(input_list) + 1:
    sum = 0
    # Create subsets of three
    for i in range(start, end):
        sum += input_list[i]
    if start == 0:
        # Start at the beginning of the list if the end is reached
        print(alphabet_list[start % len(alphabet_list)] + ':', sum, '(N/A - no previous sum)')
    elif sum > prev_sum:
        print(alphabet_list[start % len(alphabet_list)] + ':', sum, '(increased)')
        count += 1
    elif sum < prev_sum:
        print(alphabet_list[start % len(alphabet_list)] + ':', sum, '(decreased)')
    else:
        print(alphabet_list[start % len(alphabet_list)] + ':', sum, '(no change)')
    start += 1
    end += 1
    prev_sum = sum

print('There are', count, 'sums larger than the previous sum.')