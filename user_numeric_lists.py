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
    future_y = round(slope * future_x + intercept)
    print(f'The Y value at the future time 15 is', {future_y})
    min1 = min(List1)
    Max1 = max(List1)
    Len1 = len(List1)
    Sum1 = sum(List1)
    set1 = set(List1)
    average1 = Sum1 / Len1
    sorted1 = sorted(List1)
    sorted11 = sorted(List1, reverse=True)

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

