from stupid_lists import *

def green(string):
    return '\033[92m' + string + '\033[0m'

def red(string):
    return '\033[91m' + string + '\033[0m'

def demo(list, title):
    stupid_lists = StupidLists()
    original = str(list)
    result = str(stupid_lists.sort(list))
    separator = "  =>  "
    print "\n" + title
    print (original).ljust(30) + separator + result

def working(list, title):
    demo(list, green(title))

def still_not_working(list, title):
    demo(list, red(title))

working([1, 2, 3], 'Odd amount of elements')
working([1, 2, 3, 4], 'Even amount of elements')
working([1, 1, 1, 2, 2, 2], 'Two elements repeating')
working([1, 1, 1, 2, 2, 2, 3, 3, 3], 'Three elements repeating')
working([1, 1, 1, 1, 2, 3, 4, 5], 'Even amount of elements, 50% of which duplicates (min value)')
working([1, 2, 3, 4, 5, 5, 5, 5], 'Even amount of elements, 50% of which duplicates (max value)')
working([1, 1, 1, 1, 1, 2, 3, 4, 5], 'Odd amount of elements, 50% + 1 of which duplicates (min value)')
working([1, 2, 3, 4, 5, 5, 5, 5, 5], 'Odd amount of elements, 50% + 1 of which duplicates (max value)')

still_not_working([1,2,2,3,4], 'Even amount of unique elements but even amount of elements overall, 50% of which duplicates (lower near middle value)') #

still_not_working([1,2,3,42,2,3,4], 'Even amount of unique elements but even amount of elements overall, 50% of which duplicates (lower near middle value)')

still_not_working([1,2,3,3,3,3,4,5], 'Even amount of unique elements and even amount of elements overall, 50% of which duplicates (middle value)')

still_not_working([1,2,3,3,3,3,3,4,5], 'Odd amount of elements, 50% + 1 of which duplicates (middle value)') # 3,1,3,2,3,4,
