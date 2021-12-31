# ❄️ Day 1 Reflection ❄️

## Part 1
I love the simplicity of Python but it is so hard to wrap my head around the Python way of doing things.

Indexing for example! You have to use a specific function for that: ```enumerate()```

```python
for index, val in enumerate(input_list):
    if index == 0:
        print(val, ' (N/A - no previous measurement)')
    elif input_list[index] < input_list[index - 1]:
        print(val, ' (decreased)')
    else:
        print(val, ' (increased)')
```

In this function, I'm comparing two indexes in the list to determine which of their values is larger/smaller. 

## Part 2
I also learned how to restart to the beginning of a list if the end was reached with this nifty little modulo math trick.
```python
alphabet_list[index % len(alphabet_list)]
```

## Optimised Solution
It's so crazy that this can be solved in one line of code. The sum function can be used to return a count based on an expression; in this case, everytime the next number is larger than the previous number in the list. Fascinating. 🙂
### Part 1
```python
sum(x < y for x, y in zip(nums, nums[1:]))
```

### Part 2
```python
sum(x < y for x, y in zip(nums, nums[3:]))
```

These use ```Generator Expressions```: frequently used with ```sum()```, ```min()```, and ```max()``` functions to reduce an iterable input to a single value.

Generator expressions are similar to list comprehensions except they don't return a list & don't store it in memory.
The difference is that list comprehension uses square brackets and generator expressions use parentheses.

The zip function returns pairs based on the iterators it's given
```(176, 184), (184, 188), (188, 142), (142, 151)```

it's good for creating dictionaries
```python
>>> fields = ["id", "name", "location"]
>>> values = ["13", "bill", "redmond"]
>>> dict(zip(fields, values))
{'location': 'redmond', 'id': '13', 'name': 'bill'}
```
### Source
```Chitinid``` on Reddit:
https://www.reddit.com/r/adventofcode/comments/r66vow/2021_day_1_solutions/hmrggq3/
