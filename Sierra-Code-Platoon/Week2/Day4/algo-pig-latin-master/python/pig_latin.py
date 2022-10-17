def translate(word_or_phrase):
  
  tmp_word = word_or_phrase.lower().split()
  
  for index, word in enumerate(tmp_word):
    # check for the first letter as a vowel
    if word[0] in 'aeiou':
      tmp_word[index] = tmp_word[index] + 'ay'
    else:
      has_vowel = False
      for j, letter in enumerate(word):
        if letter in 'aeiou':
                tmp_word[index] = word[j:] + word[:j] + "ay"
                has_vowel = True
                break
      
      if(has_vowel == False):
            tmp_word[index] = tmp_word[index]+ "ay"
      
  pig_latin = ' '.join(tmp_word)
  
  # print("Pig Latin:",pig_latin)
  print(pig_latin)
  return pig_latin

# translate('apple')
  
