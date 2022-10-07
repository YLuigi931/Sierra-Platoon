def sum_pairs(lst , number):
    
    result = []
    
    for n in lst:
        for num in lst:
            # if n != num:
            if n + num == number and [num , n] not in result:
                    result.append([n , num])
        
    if len(result) == 0:
        return "unable to find pairs"
    print(result)    
    return result
    
