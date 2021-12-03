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

import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from time import time
from math import sqrt


# Code Structure:
# ---------------
# 1 . Data Generation
# 2 . Main Function
# 3 . Data Analysis Functions
# 4 . Data Visualization
# 5 . Misc.


# -----------------------------------------------------------
# DATA GENERATION
# -----------------------------------------------------------


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
    rand = time()
    m = 2 ** 31
    a = 13751
    
    rand_list = np.arange(length)
    for i in np.nditer(rand_list):
        rand = (a * rand) % m
        rand_list[i] = rand % nums_in_range + 1

    return rand_list


# sorting data beforehand

start_time = time()
data = my_random(1000000, 100)
total_time = time() - start_time

# Numpy random number generator to simulate large scale data
generate = np.random.randint(100, size=1000000)


# -----------------------------------------------------------
# MAIN FUNCTION
# -----------------------------------------------------------

def main():
    print("\t\tWelcome to my Data Analysis Project")
    print("-" * 63)
    print_summary(DataItems, 50, 10)

    # numpy_randint
    lists_1 = sorted(count(generate).items())

    x_1, y_1 = zip(*lists_1)

    # my_random
    lists_2 = sorted(count(data).items())

    x_2, y_2 = zip(*lists_2)

    plt.subplot()
    numpy_rand = plt.plot(x_1, y_1)
    plt.setp(numpy_rand, color='blue', linewidth=1)
    plt.title("Distribution Chart")
    plt.xlabel("Numbers in Range")
    plt.ylabel("Frequency")

    plt.subplot()
    my_rand = plt.plot(x_2, y_2)
    plt.setp(my_rand, color='red', linewidth=1)
    plt.show()

    print(data)
    
    # # format data to 2d array
    # data_2 = np.reshape(data,(500, 500))
    # data_3 = np.random.random((500, 500))

    # plt.figure()
   
    # plt.title("My_Random Pattern Plot")
    # plt.imshow(data_2, interpolation='nearest')

    # plt.show()

    print(data)
    return print("\n[{}] seconds...".format(total_time))


# -----------------------------------------------------------
# DATA ANALYSIS FUNCTIONS
# -----------------------------------------------------------


def sample_s_deviation(a):
    """
    Desc:
    Perform (dev)iance calculation for every element in list.
    Params:
    a - a list containing integers
    Returns:
    (int) - square root of new mean
    """
    new_arr = (a - np.mean(a)) ** 2
    new_mean = np.mean(new_arr)
    samp_var = sqrt(new_mean)
    return samp_var


def standard_error(a):
    """
    Desc:
    Standard error formula; uses the length and samp_var global variable
    Param:
    a (int) - flawed
    """
    new_arr = (a - np.mean(a)) ** 2
    new_mean = np.mean(new_arr)
    samp_var = sqrt(new_mean)
    return samp_var / sqrt(a.size)


def count(a):
    counting = Counter()
    for nums in a:
        counting[nums] += 1
    return dict(counting)


# Create Diehard test functions
# that operate on my custom random
# number generator


# -----------------------------------------------------------
# DATA VISUALIZATION
# -----------------------------------------------------------


def print_summary(a: dict, left_width: int, right_width: int):
    """
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
    """
    table_width = right_width + left_width
    print("Summary of Dataset".center(left_width + (right_width + 3), "_"))
    for i, j in a.items():
        print("|", i.ljust(left_width, " ") + str(j).rjust(right_width) + '|')
        print("|" + "-" * (table_width + 1) + "|")


# A dictionary of all of the attributes is an easy
# way of organizing and compressing the data that
# scales with the table structure.
DataItems = {
    'Data Length': format(data.size, '.4f'),
    'Mean': format(np.mean(data), '.4f'),
    'Sample Standard Deviation': format(sample_s_deviation(data), '.4f'),
    'Standard Error': format(standard_error(data), '.4f'),
}

# -----------------------------------------------------------
# MISC.
# -----------------------------------------------------------

# Driver Code
if __name__ == "__main__":
    main()
