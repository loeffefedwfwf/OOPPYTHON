from counter import Counter
#iter1 = iter([1,2,3,4,5,6,7,8,9,10])
'''
for i in iter1:
    print(i)
'''
'''
try:
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
except StopIteration:
    pass
'''
iter0 = Counter(15, 21)
'''
for _ in iter0:
    print(iter0.__str__())
'''
while(True):
    try:
        print(iter0.__str__())
        iter0.__next__()
    except StopIteration:
        break