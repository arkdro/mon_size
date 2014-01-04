# given a diagonal and a sides ratio
# calculate sides of a monitor

import argparse
import numpy as np
from fractions import Fraction

# def diag(side, ratio):
#     return np.sqrt(side^2 + (side * ratio)^2)

def sides(diag, ratio):
    h = diag / np.sqrt(1 + np.square(ratio))
    w = h * ratio
    return (w, h)

def conv_ratio(r0):
    if isinstance(r0, str):
        if '/' in r0:
            r1 = Fraction(r0)
            ratio = float(r1.numerator) / float(r1.denominator)
        else:
            ratio = float(r0)
    else:
        ratio = float(r0)
    return ratio

def main():
    parser = argparse.ArgumentParser(description='sizes of a monitor')
    parser.add_argument('-d', '--diag', dest='diag', type=float,
                       required=True, help='diagonal')
    parser.add_argument('-r', '--ratio', dest='ratio',
                       required=True, help='ratio')
    args = parser.parse_args()
    # print(args)
    ratio = conv_ratio(args.ratio)
    (w, h) = sides(args.diag, ratio)
    print w, h

if __name__ == '__main__':
    main()
