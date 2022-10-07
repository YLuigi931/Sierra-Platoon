# Don't forget to run the tests (and create some of your own)

# Part 1
def is_character_match(string1, string2):
	# Your code here
	# if len(string1) != len(string2):
    #   return False
    result1 = {}
    result2 = {}
    lower1 = string1.lower().replace(' ', '')
    lower2 = string2.lower().replace(' ', '')
    for item in lower1:
        if item not in result1:
            result1[item] = 1
        else:
            result1[item] += 1
    for item in lower2:
        if item not in result2:
            result2[item] = 1
        else:
            result2[item] += 1
    return result1 == result2


# Part 2
def anagrams_for(word, list_of_words):
	# your code here
	results = []
	
	for item in list_of_words:
		if is_character_match(word, item):
			results.append(item)
	return results
