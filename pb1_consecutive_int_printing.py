#Problem

# The included code stub will read an integer, , from STDIN.
#
# Without using any string methods, try to print the following:
#
#
# Note that "" represents the consecutive values in between.
#
# Example
#
# Print the string .
#
# Input Format
#
# The first line contains an integer .
#
# Constraints
#  1 <= n <= 150
#
# Output Format
#
# Print the list of integers from  through  as a string, without spaces.
#
# Sample Input 0
#
# 3
# Sample Output 0
#
# 123


#Solution

def cons_print(n) :
    i = 1
    a = 0
    while i <= n :
        if i <= 9 :
            a = ((a * 10) + i)
            i = i + 1
        elif 10 <= i <= 99 :
            a = ((a * 100) + i)
            i = i + 1
        elif 100 <= i <= 150 :
            a = ((a * 1000) + i)
            i = i + 1
        else :
            Print('out of Constraints')
    return print(a)

cons_print(int(input( )))
