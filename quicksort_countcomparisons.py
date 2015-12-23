import collections
import re

total_comparisons = 0

# choode index of median element of the three
def choose_pivot(list, l, r):
    first = l
    middle = (int)(l + ((r - l - 1)/2))
    final = r - 1
    l = [(first, list[first]), (middle, list[middle]), (final, list[final])]
    l = sorted(l, key=lambda val : val[1])
    median = l[1]
    return median[0]

def partition(l, left, right):
    final_pivot_position = left + 1
    pivot_value = l[left]

    for j in range(left + 1, right): # right non-inclusive
        if l[j] <= pivot_value:
            l[j], l[final_pivot_position] = l[final_pivot_position], l[j]
            final_pivot_position += 1

    l[left], l[final_pivot_position - 1] = l[final_pivot_position - 1], l[left]
    return final_pivot_position - 1

def qs(l, left, right):
    global total_comparisons
    if right - left <= 1:
        return l

    total_comparisons += (right - left - 1)

    pivot = choose_pivot(l, left, right)
    l[left], l[pivot] = l[pivot], l[left] # left is pivot
    final_pivot_position = partition(l, left, right) # right non-inclusive
    qs(l, left, final_pivot_position) # right non-inclusive
    qs(l, final_pivot_position + 1, right) # right non-inclusive
    return l

def qs_start(l):
    return qs(l, 0, len(l)) # right non-inclusive

# checls whether array is sorted
def check_sorted(l):
    for x in range(0, len(l) - 1):
        if (l[x] > l[x + 1]):
            return False;
    return True;

with open('data/QuickSort.txt') as f:
    l = f.read().splitlines()
l = [int(i) for i in l]
qs_start(l)
print (total_comparisons)
print (check_sorted(l))