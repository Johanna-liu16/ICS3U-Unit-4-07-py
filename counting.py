#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Oct 2022
# This program adds two numbers

import random


def main():

    # process
    value = input("Press Enter to print all the numbers between 1000-2000.")
    for num in range(1000, 2001):
        if num % 5 == 0 and num != 1000:
            print("\n{0} ".format(num), end="")
        else:
            print("{0} ".format(num), end="")
    print("")
    print("\nDone.")


if __name__ == "__main__":
    main()
