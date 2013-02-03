Python Lists Reference

Lists, lists, lists! Here's a big post all about lists in Python.

### Basic stuff

Declare a list:

```python
example_list = []```

Put stuff in the list:

```python
example_list = [1, 2, 3, 4, 5]```

Get items from the list:

```python
example_list[0] # 1
example_list[1] # 2
example_list[2] # 3```

Find the number of items in the list:

```python
len(example_list) # 5```

Find the max and minimum items in the list. This follows the ASCII sort order.

```python
min(example_list) # 1
max(example_list) # 5```

### Sorting lists

Sorting time! Let's say you have a nested list (lists with more lists inside):

```python
some_list = [[0,2,.93],[5,3,.53],[6,7,.12],[12,4,.68]]```

And you want to sort the lists inside 'some_list' by the third value in the 
lists (the decimal numbers .93, .53, etc). You would do something like:

```python
sorted_list = sorted(some_list, key=lambda weight: weight[2], reverse=True)

>>> some_list = [[0,2,.93],[5,3,.53],[6,7,.12],[12,4,.68]]
>>> sorted_list = sorted(some_list, key=lambda weight: weight[2], reverse=True)
>>> sorted_list
[[0, 2, 0.93], [12, 4, 0.68], [5, 3, 0.53], [6, 7, 0.12]]```

### Shuffling lists

```python
import random # we will need the random module
example_list = [1, 2, 3, 4, 5]
random.shuffle(example_list)
>>> example_list
[4, 1, 2, 3, 5]```

### Useful functions

Determine if variable x is in a list:

```python
def is_in_list(x, list):
    if x in list:
        return True
    else:
        return False```

Return a list as all integers:

```python
def list_to_int(list):
        new_list = []
        for string in list:
                new_list.append(int(str))
        return new_list```
