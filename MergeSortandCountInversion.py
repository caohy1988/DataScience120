from dipy.utils.six.moves import xrange
def partition(array):
    size = len(array)
    half_size = int(size/2)
    x1 = []
    x2 = []
    for index in xrange(0, half_size):
        x1.append(array[index])
    for index in xrange(half_size, size):
        x2.append(array[index])
    return [x1, x2]

def merge(x1, x2):
    x = []
    x1_index = 0
    x2_index = 0
    inv_count = 0
    size_1 = len(x1)
    size_2 = len(x2)
    while (x1_index < size_1 and x2_index < size_2):
        if x1[x1_index] <= x2[x2_index]:
            x.append(x1[x1_index])
            x1_index += 1
        else:
            x.append(x2[x2_index])
            x2_index += 1
            inv_count += (size_1 - x1_index)

    for i in range(x1_index, size_1):
        x.append(x1[i])
    for i in range(x2_index, size_2):
        x.append(x2[i])

    return x, inv_count


def merge_sort(array):
    if len(array) > 1:
        [x1, x2] = partition(array)
        x1, left_inv = merge_sort(x1)
        x2, right_inv = merge_sort(x2)
        merged, split_inv = merge(x1, x2)
        return merged, (left_inv + right_inv + split_inv)
    else:
        return array, 0
array = [11,12,10,1,3,2,5,4,7,6,9,8]
sort_list, num = merge_sort(array)
print (sort_list, num)
