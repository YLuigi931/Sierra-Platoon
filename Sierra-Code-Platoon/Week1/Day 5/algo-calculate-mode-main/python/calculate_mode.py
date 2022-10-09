'''
find the most common element

'''

def calculate_mode(lst):
    tally = {}
    result = []
    for item in lst:
        if item not in tally:
            tally[item] = 1
        else:
            tally[item] += 1

    current_max = max(tally.values())
    # print(current_max)
    for num in tally:
        # print(tally.get(num))
        if tally.get(num) == current_max:
            result.append(num)

    # print(result)
    return result
    
# calculate_mode([1,2,3,3])

