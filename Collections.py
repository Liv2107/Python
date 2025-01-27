# Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter as counter

a = "aaaaabbbbbbcccddeee"
counter_one = counter(a)
print(counter_one)
print(counter_one.values())
print(counter_one.most_common())
print(list(counter_one.elements()))

from collections import namedtuple as nt

point = nt("point", "x,y")
pt = point(1,-4)
print(pt)

from collections import OrderedDict as OD

ordered_dict = OD()
ordered_dict['a'] = 1
ordered_dict['b'] = 4
ordered_dict['c'] = 2
ordered_dict['d'] = 3

print(ordered_dict)

from collections import defaultdict as dd

d = dd(int)
d['a'] = 1
d['b'] = 4
d['c'] = 2
d['d'] = 3

print(d["a"])
print(d["r"]) # will return the default int value : 0.


from collections import deque
# used to add and remove elements.

deq = deque()

deq.append(1)
deq.append(2)

deq.appendleft(2)
deq.pop() # removes the last element

print(deq)

deq.clear()
deq.extend([4,5,6]) # or deq.extendleft(...).

print(deq)

deq.rotate(1)

print(deq)

from collections import ChainMap 
   
   
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

c = ChainMap(d1, d2, d3) 
   
print(c) # ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}) stores multiple maps.

print(c['a'])
print(c.values())
print(c.keys())

d4 = {'g': 3, 'h': 7}
c2 = c.new_child(d4) # adding to a chain map.

print(c2)