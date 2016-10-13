melon = [2, 3, 4, 5, 6, 7, 8]
box = [1, 2, 4, 5, 3, 7, 8, 9, 10]

index1 = 0
index2 = 0
length_melon = len(melon)
length_box = len(box)
length_difference = length_box - length_melon
while index1 < length_difference:
    index2 = 0
    while index2 < length_melon:
        if box[index1+index2] > melon[index2]
