import random
import string

# ================== dice.py ========================

class Dice:
  
    def __init__(self):
        self.value = ''.join(random.choices(string.ascii_uppercase, k=1))
        # print(self.value)

    def get_value(self):
        return self.value
    
'''
We currently implement our board without modeling dice. 
We should do that next to make our board come closer to 
modeling a real Boggle board. Instead of choosing 16 
random letters from the entire alphabet, we should choose 
a random letter from any of the six letters on the die, 
for each of the 16 dice that boggle uses. We also need to 
choose a random order for the dice themselves. 
'''
# =====================buggle_board.py============
class Buggle_board:
    '''
    row is the length of the lines
    col represent how many rows
    '''
    def __init__(self, row , col):
        self.board = self.assemble(row, col)
    
    def shake(self):
        pass
    
    def assemble(self, row, col):
        # makes [[dice,dice],[dice,dice],[...]...]
        arrays = []
        word_bank = 0
        
        while(word_bank != col):
            word = 0
            lst = []
            while(word != row):
                die = Dice()
                lst.append(die)
                # print(die.get_value())
                word+=1
                
            arrays.append(lst)
            word_bank+=1
             
        # print(arrays)
        return arrays
        
    def __str__(self):
        result = '```python\n'
        
        for dice_bag in self.board:
            tmp_word = ''
            for die in dice_bag:
                if die.get_value() == 'Q':
                    tmp_word += 'Qu'
                    tmp_word += ' '
                else:
                    tmp_word += die.get_value()
                    tmp_word += '  '
                
            tmp_word += '\n'
            result += tmp_word
        result += '```'
        return result
        
# =========== main.py ==============

board1 = Buggle_board(3,5)
print(board1)

board2 = Buggle_board(8,7)
print(board2)

