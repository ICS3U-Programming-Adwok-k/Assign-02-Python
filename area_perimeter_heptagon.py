#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: Mar 7th 28th, 2025
# This program calculates the area and the
# perimeter of a heptagon.
import math


def main():
    # The initial greeting
    print("Hello & Welcome to Adwok's Heptagon formula !")
    # input
    # Side length of the Heptagon
    a = int(input("Enter the side length of the heptagon: "))
    # Process
    # The area of the heptagon
    area = (7 / 4) * (a**2) * (1 / math.tan(math.radians(180 / 7)))
    # The perimeter of the heptagon
    perimeter = 7 * a
    # Output
    # The area of the heptagon
    print("The Area of the heptagon is:{:,.2f}cm^2".format(area))
    # The perimeter of the heptagon
    print("The perimeter of the heptagon is:{}cm".format(perimeter))


if __name__ == "__main__":
    main()
