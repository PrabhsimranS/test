#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      715907
#
# Created:     29/05/2020
# Copyright:   (c) 715907 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
#added comment
def test():
    """this is test function code
    this is second line """
    print ("u r in test function")
def main():
    a = "i am not doing it , i dnt feel like i can"
    b=a.replace('i','you')
    #print (b)
###### reverse list
    a2=[1,2,3,4,5]
    a2.reverse()
    print(a2)
###### docstring usage with fucntion test
    help(test)
    print(test.__doc__)
if __name__ == '__main__':
    main()
