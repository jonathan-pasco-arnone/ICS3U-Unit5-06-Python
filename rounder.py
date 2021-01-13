#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: January 2021
# This program removes a specified amount of decimals form a specified number

def changer(number, round_off_amount):
    # This function removes a specified amount of
    # decimals form a specified number

    number[0] = ((int(number[0] * pow(10, round_off_amount) + 0.5))
                 / pow(10, round_off_amount))


def main():
    # This function gathers inputs and places them into the
    # designated functions

    number_list = []

    try:
        print("")
        number_input = float(input("Enter a number with decimals: "))
        print("")
        round_off_amount_input = int(input("Number of to round off to: "))
        print("")
    except Exception:
        print("Please enter valid integers")
    else:
        if round_off_amount_input > 0:
            number_list.append(number_input)
            changer(number_list, round_off_amount_input)
            print("The number is {}".format(number_list[0]))
        else:
            print("Please input a positive round off amount")


if __name__ == "__main__":
    main()
