"""
Modify this docstring.

"""

# import some modules first - how many can you make use of?

import math
import statistics

# define some functions


def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something
    # could go wrong
    try:
        area = 0  # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("your code here")

    List1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    listx = [1,2,3,4,5,6,7,8,9,10]
    listy = [2,4,6,10,12,14,16,18,20,22]
    mean1 = statistics.mean(List1)
    meanx = statistics.mean(listx)
    meany = statistics.mean(listy)
    print(f'The mean for list 1 is', {mean1} , ' \n The mean for list x is ', {meanx}, ' \n The mean for list y ', {meany})
    mode1 = statistics.mode(List1)
    modex = statistics.mode(listx)
    modey = statistics.mode(listy)
    print(f'The mode for list 1 is', {mode1} , ' \n The mode for list x is ', {modex}, ' \n The mode for list y ', {modey})
    median1 = statistics.median(List1)
    medianx = statistics.median(listx)
    mediany = statistics.median(listy)
    print(f'The median for list 1 is', {median1} , ' \n The median for list x is ', {medianx}, ' \n The median for list y ', {mediany})
    Stand1 = statistics.stdev(List1)
    standx = statistics.stdev(listx)
    standy = statistics.stdev(listy)
    print(f'The Standard deviation for list 1 is', {Stand1} , ' \n The Standard Deviation for list x is ', {standx}, ' \n The Standard Deviation for list y ', {standy})
    Var1 = statistics.variance(List1)
    Varx = statistics.variance(listx)
    Vary = statistics.variance(listy)
    print(f'The Variance for list 1 is', {Var1} , ' \n The Variance for list x is ', {Varx}, ' \n The Variance for list y ', {Vary})
    xy_corr = statistics.correlation(listx, listy)
    print(f'The correlation between list X and list Y is ', {xy_corr})
    slope, intercept = statistics.linear_regression(listx, listy)
    future_x = 15
    future_y = slope * future_x + intercept
    print(f'The future y value at x = 15 is ', {future_y})
    min1 = int(min(List1))
    Max1 = int(max(List1))
    Len1 = int(len(List1))
    Sum1 = int(sum(List1))
    average1 = int(Sum1 / Len1)
    sorted1 = tuple(sorted(List1))
    sorted11 = tuple(sorted(List1, reverse=True))
    print(f'The min, max, Len, Sum, Set, average, sorted and reverse sorted for list 1 is \n', {min1}, {Max1}, {Len1}, {Sum1}, {average1})
    print(f'The sorted list 1 is ', {sorted1})
    print(f'The reverse sorted list 1 is ', {sorted11})
    first = [1,2,3]
    group = [1,2,3,4,5]
    app = first.append(4)
    print(f'This is the list appending', first.append(2))
    ex = first.extend([4,5,6])
    print(f'This is the list ending')
    i = 0
    newvalue = 42
    first.insert(i,newvalue)
    item_to_remove = 5 
    cool = first.remove(item_to_remove)
    print(f'This is removing an item', {cool})
    ace = acendingsort = first.sort()
    print(f'This is acending sort', {ace})
    ct_of_2 = first.count(2)
    print(f"This is counting 2", {ct_of_2})
    Decendingsort = first.sort(reverse=True)
    print('This is Decending Sort', {Decendingsort})
    second = first.copy()
    print(f'This is using .copy', )
    first = second.pop(0)
    print(f'This is using .pop(0)', {first})
    last = second.pop(-1)
    print(f'This is using .pop(-1)', {last})
    scores_less_than_4 = [x for x in group if x < 4]
    print(f'This is only using x < 4')
    cubed_root = map(lambda x: math.pow(x), group)
    print('This is using cubed root', {cubed_root})
    volume_list = [map(lambda x: x * x * x, group)]
    print(f'This is using volume')
    listfiltered = [filter(lambda x: x < 4, group)]
    print(f'This is the list filtered', (listfiltered))
    tripled_scores = [map(lambda x: x * 3, group)]
    print(f'This is the list trippled', [tripled_scores])
    quad_scores = [map(lambda x: x * 4, group)]
    print(f'This is the list quadrupled', quad_scores)

# Why? Why only print if this the module called?
# Because when you write good functions, you may want to
# import this module into another script - just like you did
# math or statistics.
# Build a library of resuable functions to support your domain.

# For example, if your domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a list of your favorite artists.


# When you write reusable functions for your domain, you can
# import the module with your utility functions into other modules
# and use them there.  This is a very common practice.
# Anything you write can be imported into later projects.

