#!/usr/bin/env python3

import operator
import readline
from termcolor import colored
import sys

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '>': operator.gt,
    '<': operator.lt,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(token)
            stack.append(result)
        
        print '[',

        #Get rid of space after using ','
        sys.stdout.softspace=0
        
        for i in stack[:-1]:
            if(i == '+'):
                print colored(str(i), 'green') + ',',
            elif(i == '-'):
                print colored(str(i), 'red') + ',',
            elif(i == '*'):
                print colored(str(i), 'yellow') + ',',
            elif(i == '/'):
                print colored(str(i), 'magenta') + ',',
            elif(i == '^'):
                print colored(str(i), 'grey') + ',',
            else:
                print str(i) + ',',

        print str(stack[len(stack) - 1]) + ']'

    if len(stack) != 2:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> ")) 
        
        if(result < 0):
            print("Result:"),
            print colored(result, 'red', attrs=['bold', 'blink'])
        elif (result == 0):
            print("Result:"),
            print colored(result, 'yellow', attrs=['bold', 'blink'])
        else:
            print("Result:"),
            print colored(result, 'green', attrs=['bold', 'blink'])


if __name__ == '__main__':
    main()
