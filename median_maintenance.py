# maintains median for incoming numbers without sorting but by using two heaps
from functools import reduce
from heapq import heappop, heappush
import math
import sys

# default Python heap is minheap, this class turns it into maxheap using negation of values
class Heap:
    def __init__(self, max_heap):
        self.pq = []
        self.max_heap = max_heap

    def push(self, value):
         if self.max_heap == True:
            value = -value
         heappush(self.pq, value)

    def pop(self):
        value = heappop(self.pq)
        if self.max_heap == True:
            value = -value
        return value

    def lookup(self):
        value = self.pq[0]
        if self.max_heap == True:
            value = -value
        return value

    def len(self):
        return len(self.pq)

# keeps track of the median in the growing unsorted list,
# returns current median
class MedianMainteiner:
    def __init__(self):
        self.loheap = Heap(True)
        self.hiheap = Heap(False)
        self.curr_median = sys.maxsize

    # feed in the unsorted numbers one by one
    def push(self, value):

        # push the number to low heap if it is smaller than median
        if value < self.curr_median:
            self.loheap.push(value)
        else:
            self.hiheap.push(value)

        # hiheap and lowheap shouldn't differ in size by more than 1,
        # if one heap is larger than the other take one item from it
        # and push it to the heap that is smaller
        if (self.loheap.len() - self.hiheap.len() > 1):
            transfer_value = self.loheap.pop()
            self.hiheap.push(transfer_value)
        elif (self.hiheap.len() - self.loheap.len() > 1):
            transfer_value = self.hiheap.pop()
            self.loheap.push(transfer_value)

        # our median is either at the top of loheap or hiheap
        k = self.hiheap.len() + self.loheap.len() # total items count
        k = math.ceil(k / 2) # index of median
        if k > self.loheap.len():
            self.curr_median = self.hiheap.lookup()
        else:
            self.curr_median = self.loheap.lookup()
        return self.curr_median

def main():
    test1 = [11, 3, 6, 9, 2, 8, 4, 10, 1, 12, 7, 5]
    test2 = [1,2,3,4,5,6,7,8,9]

    with open('Data/Median.txt') as f:
        work = f.read().splitlines()
    work = [int(i) for i in work]

    results = []
    m = MedianMainteiner()
    for i in work:
        results.append(m.push(i))

    print("Medians sum mod 10000 = ", reduce(lambda x,y: x+y, results) % 10000)


main()
