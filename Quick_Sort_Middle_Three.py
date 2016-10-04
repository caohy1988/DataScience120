firstcomparison = 0
lastcomparison = 0
mediancomparison = 0

#A method for partition around the first element of the array
def partition_first(array, leftend, rightend):
    pivot = array[leftend]
    i = leftend + 1
    for j in range(leftend + 1, rightend):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    leftendval = array[leftend]
    array[leftend] = array[i-1]
    array[i-1] = leftendval
    return i - 1

#A method for partitioning around the last element of the array
def partition_last(array, leftend, rightend):

    pivot = array[rightend-1]

    array[rightend-1] = array[leftend]
    array[leftend] = pivot

    i = leftend + 1
    for j in range(leftend + 1, rightend):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    leftendval = array[leftend]
    array[leftend] = array[i-1]
    array[i-1] = leftendval
    return i - 1

#A method to calculate the median of three numbers using two comparisons
def median(array, a, b, c):
    if ( array[a] - array[b]) * (array[c] - array[a]) >= 0:
        return array[a], a

    elif (array[b] - array[a]) * (array[c] - array[b]) >= 0:
        return array[b], b

    else:
        return array[c], c

#A method to partition around the median
def partition_median(array, leftend, rightend):
    left = leftend
    right = rightend-1
    length = rightend - leftend
    if length % 2 == 0:
        middle = leftend + int(length/2) - 1
    else:
        middle = leftend + int(length/2)



    pivot, pivotindex = median(array, left, right, middle)

    #only works if all values in array unique

    array[pivotindex] = array[leftend]
    array[leftend] = pivot

    i = leftend + 1
    for j in range(leftend + 1, rightend):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    leftendval = array[leftend]
    array[leftend] = array[i-1]
    array[i-1] = leftendval
    return i - 1


#Implement quicksort while partitioning around the first index
def quick_sort1(array, leftindex, rightindex):
    global firstcomparison
    if leftindex < rightindex:

        newpivotindex = partition_first(array, leftindex, rightindex)

        firstcomparison += (rightindex - leftindex - 1)

        quick_sort1(array, leftindex, newpivotindex)

        quick_sort1(array, newpivotindex + 1, rightindex)

def quicksort_last(array, leftindex, rightindex):
    global lastcomparison
    if leftindex < rightindex:

        newpivotindex = partition_last(array, leftindex, rightindex)

        lastcomparison += (rightindex - leftindex - 1)

        quicksort_last(array, leftindex, newpivotindex)
        quicksort_last(array, newpivotindex + 1, rightindex)


def quicksort_median(array, leftindex, rightindex):
    global mediancomparison
    if leftindex < rightindex:

        newpivotindex = partition_median(array, leftindex, rightindex)

        mediancomparison += (rightindex - leftindex - 1)
        quicksort_median(array, leftindex, newpivotindex)


        quicksort_median(array, newpivotindex + 1, rightindex)



test3 = [1, 11, 5, 15, 2, 12, 9, 99, 77, 0]
test4 = []
for i in range(1, 101):
    test4.append(i)

quicksort_median(test3, 0, len(test3)-1)
print (mediancomparison)
