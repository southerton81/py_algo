import collections
import re

total_comparisons = 0

# choode index of median element of the three
def choose_pivot(list, l, r):
    first = l
    middle = l + ((r - l - 1)/2)
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
        if (x > l[x + 1]):
            return False;
    return True;

with open('QuickSort.txt') as f:
    l = f.read().splitlines()
l = [int(i) for i in l]
qs_start(l)
print total_comparisons
print check_sorted(l)



#print choose_pivot(rl, 0, len(rl))
## print check_sorted(l)

#print(check_sorted(l))
#print(qs_start(alist))

#word = "something"
#splits = [(word[:i], word[i:]) for i in range(len(word)+1)]
#print(splits)
#for index, value in splits:
#        print index, value

#def partition(l, left, right, pivot):
#    final_pivot_position = left
#    pivot_value = l[pivot]
#    l[pivot], l[right] = l[right], l[pivot]
#    for i in range(left, right):
#        if l[i] < pivot_value:
#            if (i != final_pivot_position):
#                l[i], l[final_pivot_position] = l[final_pivot_position], l[i]
#            final_pivot_position += 1
#    l[final_pivot_position], l[right] = l[right], l[final_pivot_position]
#    return final_pivot_position

#alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
#def words(text): return re.findall('[a-z]+', text.lower())
#
#def train(features):
#    models = collections.defaultdict(lambda: 1)
#    for f in features:
#        models[f] += 1
#    return models
#
#NWORDS = train(words(file('big.txt').read()))
#
#def edits1(word):
#    splits = [(word[:i], word[i:]) for i in range(len(word)+1)]
#    deletes = [a + b[1:] for a, b in splits if b]
#    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
#    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
#    inserts = [a + c + b for a, b in splits for c in alphabet]
#    return set(deletes + transposes + replaces + inserts)
#
#def edits2(word):
#    return set(e2 for e1 in edits1(word) for e2 in edits1(e1))
#
#def known(words): return set(w for w in words if w in NWORDS)
#
#def correct(word):
#    candidates = known([word]) or known(edits2(word)) or [word]
#    return sorted(candidates, key=NWORDS.get)
#
#print known(edits2("smething"))
#print correct("smething")

