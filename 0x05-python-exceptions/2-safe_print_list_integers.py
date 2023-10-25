#!/usr/bin/python3

"""
Write a function that prints the first x elements of a list and only integers.
"""


def safe_print_list_integers(my_list=[], x=0):
    en = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            en += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (en)
