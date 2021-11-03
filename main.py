# Luis Cabrera

# This program is intended to calculate the mean of
# given data and its standard error. The idea is derived
# from a free fall experiment in Physics Lab.

# Sources:
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
from functools import wraps

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
    @wraps(func)  # allows the return of function within function
    def search(items):
        if items not in cache:
            cache[items] = func(items)  # Assign new computation
        return cache[items]  # and return
 
    return search

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
    and use the of time as intial value; the function is able to generates 
    itself. Assuming a perfectly random coin flip has a mean of 5 over 10 attempts. 
    My function seems to approach (5.5) this mean, although im unsure what
    kind of distribution the numbers should have.
    Params:
    length (int) - length of the list
    nums_in_range (int) - numbers that appear in list
    Returns:
    (list) - psuedo random list
    """
    # initialize timer
    rand = time()
    a = time()-1
    c = time()-2

    rand_list = np.arange(length)
    for i in np.nditer(rand_list):
        rand = (a * rand + c) % nums_in_range
        rand_list[i] = rand+1

    return rand_list




# sorting data beforehand 

start_time = time()
data = np.sort(my_random(1000000, 100))
total_time = time() - start_time

# Numpy random number generator to simulate large scale data
generate = np.random.randint(100, size=1000000)    


# -----------------------------------------------------------
# MAIN FUNCTION
# ----------------------------------------------------------- 

def main():
    print("\t\tWelcome to my Data Analysis Project")
    print("-" * 63)
    global data
    print_summary(DataItems, 50, 10)
    print("data", data)
    


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

    # user_choice = int(input("Numpy's Random [1]\nMy Random      [2] -->"))
    # if user_choice == 2:
    #     

    # elif user_choice == 1:
    #     data = generate
    #     print_summary(DataItems, 50, 10)
    #     print(data)

    
    return print("\n[{}] seconds...".format(total_time))
    



# -----------------------------------------------------------
# DATA ANALYSIS FUNCTIONS
# -----------------------------------------------------------


def sample_s_deviation(a : list):
    '''
    Desc:
    Perform (dev)iance calculation for every element in list.
    Params:
    a - a list containing integers
    Returns:
    (int) - square root of new mean
    '''


    # Numpy's mechanism called Broadcasting
    # allowed me to perform arithmetic to every cell
    # in array resulting in a significant performance boost
    # compared to the slow python for loop. (looping occurs in c)
    new_arr = (a - np.mean(a)) ** 2
    new_mean = np.mean(new_arr)
    samp_var = sqrt(new_mean) #readbility
    return samp_var


def standard_error(a):
    '''
    Desc:
    Standard error formula; uses the length and samp_var global variable
    Param:
    a (int) - flawed
    '''
    new_arr = (a - np.mean(a)) ** 2
    new_mean = np.mean(new_arr)
    samp_var = sqrt(new_mean)
    return samp_var / sqrt(a.size)


# occurance function

def count(a):
    count = Counter()
    for nums in a:   
        count[nums] += 1
    return dict(count)





# Create Diehard test functions
# that operate on my custom random
# number generator




# -----------------------------------------------------------
# DATA VISUALIZATION
# -----------------------------------------------------------


def print_summary(a: dict, left_width : int, right_width: int):
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
    print("Summary of Dataset".center(left_width + (right_width+3), "_"))
    for i, j in a.items():
        print("|", i.ljust(left_width, " ") + str(j).rjust(right_width) + '|')
        print("|"+ "-"*(table_width+1)+ "|")



    







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
