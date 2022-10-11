class GuessingGame():
    
    def __init__(self, number):
        self.number = number
        self.ans = False
        
    def guess(self, num):
        
        if int(num) > int(self.number):
            return 'High'
        elif(int(num) < int(self.number)):
            return 'Low'
        else:
            self.ans = True
            return 'correct'
    
    def solved(self):
        return self.ans
    
    
    def __str__(self):
        pass
    
    
# game = GuessingGame(10)
# print(game.guess(5))
# print(game.guess(7))
# print(game.guess(20))
# print(game.solved())
# print(game.guess(10))
# print(game.solved())

    
