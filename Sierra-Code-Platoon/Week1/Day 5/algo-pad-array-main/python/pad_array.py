#REMEMBER TO PSEUDOCODE
''' 
part 1:
check wether the length of the current array is longer
than the min_size if not return the original list

part 2:
if the value == None and the min_size is longer than the list.
the list will append 'None' base on the length of the min_size

part 3:
If the min_size is over the list size and there is a 3rd value.
instead of appending 'None', append what that value

'''

def pad(array, min_size, value = None):
    lst_size = len(array)
    arr_copy = array
    if(min_size < lst_size):
        return array
    else:
        for item in range(lst_size-1,min_size-1):
            arr_copy.append(value)
        return arr_copy
    
# print(pad([1,2,3], 5, 'apple'))
# print(pad([1,2,3], 5))