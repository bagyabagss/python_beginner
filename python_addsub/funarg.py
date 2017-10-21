#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      16ece004
#
# Created:     21/10/2017
# Copyright:   (c) 16ece004 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
list = ['GUVI', 'learning', 'is', 'awesome', 'always']
def foo(x):
     print x * 3


def my_map_simple(fun, list):
     for item in list:
         fun(item)


my_map_simple(foo, list)

