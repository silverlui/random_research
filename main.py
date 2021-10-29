# Luis Cabrera

# This program is intended to calculate the mean of
# given data and its standard error. The idea is derived
# from a free fall experiment in Physics Lab.

# Sources:
# https://mathworld.wolfram.com/StandardError.html
# https://www.mathsisfun.com/data/standard-deviation-formulas.html
# https://numpy.org/devdocs/user/absolute_beginners.html
# https://people.duke.edu/~ccc14/sta-663-2016/15A_RandomNumbers.html
# https://en.m.wikipedia.org/wiki/Linear_congruential_generator
# https://apastyle.apa.org/style-grammar-guidelines/tables-figures/tables

import time
import functools
import numpy as np
from math import sqrt


# Code Structure:
# ---------------
# 1 . Data Generation
# 2 . Main Function
# 3 . Data Analysis Functions
# 4 . Data Visualization
# 5 . Misc.


# I've found memoizing to be super useful especially
# since many algo inevitablly compute same arithmetic
def memoize(func):
    '''
    Desc:
    Memoization is a optimization technique that remembers
    previous computations and calls it back when in cache instead
    of perfoming the same unnecessary computation. It is particularly
    useful for recursive functions.
    Params:
    (Any) - A function that is computationally expensive
    Returns:
    (Any) - The result of memoized function
    '''
    cache = {}  # memory

    # bug: search only allows for 1 parameter
    @functools.wraps(func)  # allows the return of function within function
    def search(items):
        if items not in cache:
            cache[items] = func(items)  # Assign new computation
        return cache[items]  # and return

    return search


# -----------------------------------------------------------
# DATA GENERATION
# -----------------------------------------------------------


# Numpy random number generator to simulate large scale data
generate = np.random.randint(10, size=100000)

x = 100000
y = 10


# I've decided to create an random function to
# demistify how random works and learn how to
# desgin an algorithm.

# @memoize # 'decorator' integrates into function
def my_random(length: int, nums_in_range: int):
    """
    Desc:
    The idea from my algo is derived from linear congruential algorithm
    and use the of time as initial value; the function is able to generates
    itself. Assuming a perfectly random coin flip has a mean of 5 over 10 attempts.
    My function seems to approach (5.5) this mean, although im unsure what
    kind of distribution the numbers should have.
    Params:
    length (int) - length of the list
    nums_in_range (int) - numbers that appear in list
    Returns:
    (list) - pseudo random list
    """
    # initialize timer
    rand = time.time()
    a = time.time() - 1
    c = time.time() - 2

    rand_list = np.arange(length)
    for i in np.nditer(rand_list):
        rand = (a * rand + c) % nums_in_range
        rand_list[i] = rand + 1

    return rand_list


# sorting data beforehand

start_time = time.time()
data = np.sort(my_random(x, y))
total_time = time.time() - start_time
# print("{} seconds".format(total_time))

length = data.size


# -----------------------------------------------------------
# MAIN FUNCTION
# -----------------------------------------------------------

def main():
    print("              Welcome to my Data Analysis Project")
    print("-" * 63)
    print(data)
    print_summary(DataItems, 50, 10)
    return print("\n[{}] seconds...".format(total_time))


# -----------------------------------------------------------
# DATA ANALYSIS FUNCTIONS
# -----------------------------------------------------------


def sample_s_deviation(a: list):
    '''
    Desc:
    Perform (dev)iance calculation for every element in list.
    Params:
    a - a list containing integers
    Returns:
    (int) - square root of new mean
    '''
    global samp_var

    # Numpy's mechanism called Broadcasting
    # allowed me to perform arithmetic to every cell
    # in array resulting in a significant performance boost
    # compared to the slow python for loop. (looping occurs in c)
    new_arr = (a - np.mean(a)) ** 2
    new_mean = np.mean(new_arr)
    samp_var = sqrt(new_mean)  # readbility
    return samp_var


def standard_error(a):
    '''
    Desc:
    Standard error formula; uses the length and samp_var global variable
    Param:
    a (int) - flawed
    '''
    return samp_var / sqrt(length)


# -----------------------------------------------------------
# DATA VISUALIZATION
# -----------------------------------------------------------


def print_summary(a: dict, left_width: int, right_width: int):
    '''
    Desc:
    Name of Table using the center method
    with arguments passed in the last two parameters.
    For loop creates the table for every item in
    the first parameter.
    Params:
    a - (dict) a dictionary containing the name and its related function
    left_width - (int) an integer that defines the spacing of function from left side
    right_width - (int) - an integer that defines the spacing of function from right side
    Returns:
    (prints) - an organized dictioary
    '''
    table_width = right_width + left_width
    print("Summary of Dataset".center(left_width + (right_width + 3), "_"))
    for i, j in a.items():
        print("|", i.ljust(left_width, " ") + str(j).rjust(right_width) + '|')
        print("|" + "-" * (table_width + 1) + "|")


# A dictionary of all of the attributes is an easy
# way of organizing and compressing the data that
# scales with the table structure.
DataItems = {
    'Data Length': format(length, '.4f'),
    'Mean': format(np.mean(tuple(data)), '.4f'),
    'Sample Standard Deviation': format(sample_s_deviation(list(data)), '.4f'),
    'Standard Error': format(standard_error(tuple(data)), '.4f'),
}

# -----------------------------------------------------------
# MISC.
# -----------------------------------------------------------

# main runs only if file is treated as a script
if __name__ == "__main__":
    main()
