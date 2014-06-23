#!/usr/bin/env python

data = [2, 1, 4, 3]

"""
my_values.sort(cmp=my_function)
print sum(sorted(my_values))
print min(my_values)
print max(my_values)
print my_values

def fun_average(x):
    average1 = sum(x)
    average2 = len(x)
    print(average1/average2)

fun_average(my_values)
"""

def process_data(data):
    
    count = 0
    num = 0
    mi = 0
    y = 0
    this_doesnt_do_anything = 0

    #loop
    for x in data:
        count+=1
        num = x + num
        if y == 0:
            y = x
        else:
            if x < y:
                y = x




    print "<Results>"
    print "Count: %i" % (count)
    print "Sum: %i" % (num)
    print "Minimum Value: %i" % (y)

process_data(data)


