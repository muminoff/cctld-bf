#!/usr/bin/env python

import itertools
import string
import random

# vowels = ['e', 'u', 'i', 'o', 'a', 'ye', 'yu', 'yi', 'yo', 'ya']
vowels = 'euioa'
# consonants = [x for x in string.lowercase if x not in vowels]
consonants = [''.join(x) for x in string.lowercase if x not in vowels]
consonants.remove('c')
consonants += ['sh', 'ch']

blocks = (1, 2, 3)

def block_v_1():
    return [''.join(block) for block in itertools.product(vowels)]

def block_v_2():
    return [''.join(block) for block in itertools.product(vowels, consonants)]

def block_c_2():
    return [''.join(block) for block in itertools.product(consonants, vowels)]

def block_c_3():
    return [''.join(block) for block in itertools.product(consonants, vowels, consonants)]

# def main():
    # print block_v_1()
    # print block_v_2()
    # print block_c_2()
    # print block_c_3()
    # suzlar = itertools.product(block_v_1, block_c_2)
    # for s in suzlar:
    #     print s
#     for a in itertools.product(block_c_3(), block_c_3(), block_c_3()):
#         print ''.join(a)


# if __name__ == '__main__':
#     main()
