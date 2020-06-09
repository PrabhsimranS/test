#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      715907
#
# Created:     03/06/2020
# Copyright:   (c) 715907 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re
def main():
    # find occurance of charater in string
    s = "there to check count of character"
    l = re.findall(r't',s)
    print(len(l))

    # get all the 0 values at the end of the list
    y = [1,0,4,0,0,2,3]
    y.sort(reverse=True)
    print (y)
if __name__ == '__main__':
    main()
