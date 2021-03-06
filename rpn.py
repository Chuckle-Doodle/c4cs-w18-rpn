#!/usr/bin/env python3

import operator
import colored
from colored import stylize

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}


def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        for s in stack:
            if int(s) == 0:
                print("ZERO HERE!!!")
            if int(s) < 0:
                print(stylize(s, colored.fg("red")), end='')
                print(" ", end='')
            if int(s) > 10:
                print(stylize(s, colored.fg("blue")), end='')
                print(" ", end='')
            else:
                print(s, end='')
                print(" ", end='')
        print('')
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()


def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", end='')
        print(stylize(result, colored.fg("green")))


if __name__ == '__main__':
    main()
