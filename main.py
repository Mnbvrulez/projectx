#!/usr/bin/env python

data = [2, 1, 4, 3, -9, -10, 4, 4, 3,3, -10]

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
    frequency_map = dict()
    count = 0
    sum_data = 0
    average = 0
    min_v = None
    maxi = None

    #loop
    for x in data:
        count+=1
        sum_data += x

        #Check for minimum
        if min_v is None:
            min_v = x
        else:
            if x < min_v:
                min_v = x

        #Check for maximum        
        if maxi is None:
            maxi = x
        else:
            if x > maxi:
                maxi = x

        #count up the fequency
        if frequency_map.get(x) is None:
            frequency_map[x] = 1
        else:
            frequency_map[x] += 1
       

    
    average = sum_data/count






    print "<Results>"
    print "Count: %i" % (count)
    print "Sum: %i" % (sum_data)
    print "Minimum Value: %i" % (min_v)
    print "Maximum Value: %i" % (maxi)
    print "Average(Mean): %i" % (average)
    print "\n"
    print "Frequency"
    for key, value in frequency_map.iteritems():
        print "Number: %i Frequency: %i" % (key, value)


process_data(data)


