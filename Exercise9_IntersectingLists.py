# Take two lists, return intersecting elements and count.
print("\nUsing integers from input")
L1 = map(int,input('Enter numbers separated by comma for List1:').split(','))
L1 = set([int(x) for x in L1])
L2 = map(int,input('Enter numbers separated by comma for List2:').split(','))
L2 = set([int(x) for x in L2])

def intersectingElements(L1,L2):
    elem_list = list(L1&L2)
    result = {'intersecting_elements':elem_list,'count':len(elem_list)}
    return result

print(intersectingElements(L1,L2))

