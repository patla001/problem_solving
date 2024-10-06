#!/bin/python


def reverse(string):
    i = 0
    n = len(string) - 1
    tmp = []
    while(n > 0 ):
        
        tmp.append(string[n])
        n = n - 1

    return ''.join(tmp)

if '__main__' == __name__:
    string = 'hello'
    print(f'Input: {string}')
    print(f'Output: {reverse(string)}')