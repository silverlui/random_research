# Luis Cabrera

# This program is originally intended to calculate the mean of
# given data and its standard error. The idea is derived
# from a free fall experiment in Physics Lab.

# Sources:
# https://mathworld.wolfram.com/StandardError.html
# https://www.mathsisfun.com/data/standard-deviation-formulas.html
# https://numpy.org/devdocs/user/absolute_beginners.html
# https://people.duke.edu/~ccc14/sta-663-2016/15A_RandomNumbers.html
# https://en.m.wikipedia.org/wiki/Linear_congruential_generator
# https://apastyle.apa.org/style-grammar-guidelines/tables-figures/tables
# https://easy.vegas/games/craps

import matplotlib.pyplot as plt
import numpy as np
import math
from collections import Counter
from time import time

# Code Structure:
# ---------------
# 1 . Number Generation
# 2 . Main Function
# 3 . Analysis Functions
# i . Diehard Tests
# 4 . Visualization
# 5 . Misc.


# -----------------------------------------------------------
# NUMBER GENERATION
# -----------------------------------------------------------

# TOTAL
total = 10000


# I've decided to create a random function to
# demystify how random works and learn how to
# design an algorithm.

def my_random(length: int, nums_in_range: int):
    """
    Desc:
    Linear congruential algorithm
    that outputs pseudo random integers in a list format.
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


start_time = time()
data = my_random(total, 100)
total_time = time() - start_time

# Numpy random number generator to simulate large scale data
generate = np.random.randint(100, size=total)


# -----------------------------------------------------------
# MAIN FUNCTION
# -----------------------------------------------------------

def main():
    print("\t\tWelcome to my RNG Analysis Project")
    print("-" * 63)
    print("""
    This program is designed to analyze random number generators
    via Diehard Test developed by George Marsaglia. In this case 
    the generator is being tested against Craps Test.
    """)

    while True:
        try:
            user_input = int(input("Please enter number of test cases -> "))
            if user_input < 200000:
                break
            else:
                print("Value too high...")
                continue
        except ValueError:
            print("ERROR: Incorrect input")

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

    # # format data to 2d array
    # data_2 = np.reshape(data,(500, 500))
    # data_3 = np.random.random((500, 500))

    # plt.figure()

    # plt.title("My_Random Pattern Plot")
    # plt.imshow(data_2, interpolation='nearest')

    # plt.show()

    return print(craps_test(total))


# -----------------------------------------------------------
# ANALYSIS FUNCTIONS
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
    samp_var = math.sqrt(new_mean)
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
    samp_var = math.sqrt(new_mean)
    return samp_var / math.sqrt(a.size)


def count(a):
    counting = Counter()
    for nums in a:
        counting[nums] += 1
    return dict(counting)


def percent_error(exp, theo):
    """
    Param:
    exp (float) - experimental value
    theo (float) - theoretical value
    Returns:
    (string) - formatted percentage
    """
    numer = math.fabs(exp - theo)
    result = numer / math.fabs(theo)
    return "{:.2%}".format(result)


# Craps Test
# ------------
# Determines the randomness of a uniform distribution RNG.
# Craps is game that involves dice and the goal for a RNG is to
# simulate its win rate and frequency of wins.

# Goal: K=200,000 with theoretical win rate of 244/495 -> 49.4929%

def craps_test(num_of_tests):
    """
    Desc:
    Simulates Craps game by using RNG to function as dice.
    Records wins, loss and throws that determine the effective if the rng.
    This test was picked in particular as it is applicable to all kinds of generators.
    Params:
    num_of_test (int) - number of test games
    Returns:
    stats (string) - formatted attributes of test
    """

    wins = 0
    loss = 0
    throws = 0

    for games in range(num_of_tests):

        dices = np.random.randint(6, size=2) + 1
        # dices = my_random(2, 6)
        # Doesn't work because it's initialized by time.
        roll = np.sum(dices)

        if roll == 7 or roll == 11:
            # print("You Win!" , dices, roll)
            wins += 1
            throws += 1
        elif roll == 2 or roll == 3 or roll == 12:
            # print("You Lose!", dices, roll)
            loss += 1
            throws += 1
        else:
            while True:

                roll_again = np.random.randint(6, size=2) + 1
                # roll_again = my_random(2, 6)
                re_roll = np.sum(roll_again)

                if re_roll == roll:
                    # print("You Won a Re roll!", roll_again, re_roll)
                    wins += 1
                    throws += 1
                    break
                elif re_roll == 7:
                    # print("You Lost a Re roll!", roll_again, rer_oll)
                    loss += 1
                    throws += 1
                    break
                else:
                    throws += 1
                    continue

    theo = 244 / 495
    win = wins / num_of_tests
    win_rate = "{:.4%}".format(wins / num_of_tests)
    stats = f""" NUMPY'S RESULTS ->
    Wins: {wins} Losses: {loss} Throws: {throws} Games: {num_of_tests} 
    \nWIN RATE: {win_rate}
    \nPercent Error:  {percent_error(win, theo)}"""

    return stats


# -----------------------------------------------------------
# VISUALIZATION
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
    (prints) - an organized dictionary
    """
    table_width = right_width + left_width
    print("Summary of my_random".center(left_width + (right_width + 3), "_"))
    for i, j in a.items():
        print("|", i.ljust(left_width, " ") + str(j).rjust(right_width) + '|')
        print("|" + "-" * (table_width + 1) + "|")


# Some attributes of each test case are stored under
# DataItems dictionary
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
    print("\n[{}] seconds...".format(total_time))
