inv_count = 0
# Inversions count, how far (or close) the array is from being sorted.
# If array is already sorted then inversion count is 0. If array is sorted
# in reverse order that inversion count is the maximum.
def mergeSort(alist):
    global inv_count

    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        len_left = len(lefthalf)
        while i < len_left and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                inv_count = inv_count + 1
                inv_count = inv_count + (len_left - i - 1)
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)

with open('Data/Merge.txt') as f:
    alist = f.read().splitlines()
alist = [int(i) for i in alist]
mergeSort(alist)
print(inv_count)
print(alist)
