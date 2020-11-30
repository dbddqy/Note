#!/usr/bin/env python3.5

# f_1 (2) = 2
# f_1 (3) = 2
# f_2 (2) = 1
# f_2 (3) = 3

# if n % 2 == 1: f_1 (n) = f_2 ((n-1)/2) * 2
#              : f_2 (n) = f_1 ((n+1)/2) * 2 - 1
# if n % 2 == 0: f_1 (n) = f_1 (n/2) * 2
#              : f_2 (n) = f_2 (n/2) * 2 - 1

# T = O(log N)

# import sys
#
# n = eval(sys.argv[1])
# b = eval(sys.argv[2])

n = 2


def f_1(n):
    if n == 2 or n == 3:
        return 2
    elif n % 2 == 1:
        return f_2((n-1)/2) * 2
    else:
        return f_1(n/2) * 2


def f_2(n):
    if n == 2:
        return 1
    elif n == 3:
        return 3
    elif n % 2 == 1:
        return f_1((n+1)/2) * 2 - 1
    else:
        return f_2(n/2) * 2 - 1


print(f_1(20))
