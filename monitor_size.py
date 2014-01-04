# given a diagonal and a sides ratio
# calculate sides of a monitor
# and points per inch

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

def calc_ppi(w, h, points_w, points_h):
    if points_w and points_h:
        ppi_w = int(points_w / w)
        ppi_h = int(points_h / h)
        return ppi_w, ppi_h

def main():
    parser = argparse.ArgumentParser(description='sizes of a monitor')
    parser.add_argument('-d', '--diag', dest='diag', type=float,
                       required=True, help='diagonal')
    parser.add_argument('-r', '--ratio', dest='ratio',
                       required=True, help='ratio')
    parser.add_argument('-pw', '--points-width', dest='width', type=int,
                       help='width in points')
    parser.add_argument('-ph', '--points-height', dest='height', type=int,
                       help='height in points')
    args = parser.parse_args()
    # print(args)
    ratio = conv_ratio(args.ratio)
    (w, h) = sides(args.diag, ratio)
    ppi = calc_ppi(w, h, args.width, args.height)
    if ppi:
        (ppi_w, ppi_h) = ppi
        print w, h, ppi_w, ppi_h
    else:
        print w, h

if __name__ == '__main__':
    main()
