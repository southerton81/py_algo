import sys


# Compute the number of target values t in the interval [-10000,10000] (inclusive)
# such that there are distinct numbers x,y in the input file that satisfy x+y=t
import math
class SummationsCount:
    def __init__(self):
        self.range = (-10000, 10000)
        self.foundsums = set()

    def process_sorted(self, numbers):
        max_index = len(numbers) - 1
        for n in numbers:
            min_appropriate = self.range[0] - n
            index = binary_search(numbers, min_appropriate, 0, max_index)
            max_appropriate = self.range[1] - n


            while (index <= max_index):
                value = numbers[index]
                if value <= max_appropriate and value >= min_appropriate:
                    if (n != value):
                        self.foundsums.add(n + value)
                else:
                    break;
                index = index + 1

    def get_found_sums(self):
        return self.foundsums


def binary_search(list, target_value, min_index, max_index):
    if min_index > max_index:
        return min_index

    pivot_index = int (min_index + (math.floor(max_index - min_index) / 2))

    value = list[pivot_index]
    if value == target_value:
        return pivot_index
    elif value > target_value:
        return binary_search(list, target_value, min_index, pivot_index - 1)
    elif value < target_value:
        return binary_search(list, target_value, pivot_index + 1, max_index)




#test = [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
#test.sort()

with open('Data/2sum.txt') as f:
    work = f.read().splitlines()
work = [int(i) for i in work]
work.sort()

sum_count = SummationsCount()

sum_count.process_sorted(work)
found_sums = sum_count.get_found_sums()
print(len(found_sums))

res = []
for i in found_sums:
    res.append(i)
res.sort()


'''
s = set()
for i in vals:
    s.add(i)
s2 = s.difference(found_sums)

print("====")
for t in s2:
    print(t)
'''




