sequence = [4, 3, 5, 0, 1]
swaps = 0

# Your Code Here
def bubble_sort(lst):
    index = len(lst)
    swaps = 0
    while(index != 0):
        for x in range(1, index):
            y = x - 1
            if lst[x] < lst[y]:
                swaps+=1
                tmp_num = lst[x]
                lst[x] = lst[y]
                lst[y] = tmp_num
        index-=1
    print(lst)
    print(f'swaps: {swaps}')
    return


# print(f"Final result: {result}")
# print(f"Swaps: {swaps}")
bubble_sort(sequence)