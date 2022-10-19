def binary_search(value , lst):
    '''
    return the index of the value within the lst if not return -1
    '''
    
    lst.sort()
    
    low = 0
    high = len(lst)-1
    mid = 0
    
    while(low <= high):
        
        mid = (high + low) // 2
        
        if lst[mid] < value:
            low = mid + 1
            
        elif lst[mid] > value:
            high = mid - 1
        
        else:
            return mid
    
    return -1

# test1_lst = [ 2, 3, 4, 10, 40 ]
# val = 10
# print(binary_search(val, test1_lst))