class GuessingGame():
        def __init__(self, number):
              self.number = number 
              self.user_guessed = False


        def guess(self, user_guess):
             if user_guess < self.number:
                  return 'low'
             if user_guess > self.number:
                 return 'high'
             elif user_guess == self.number:
                  self.user_guessed = True
                  return 'correct'
        
        def solved(self):
             return self.user_guessed
                        
             
 


def test_guess_high():
    game = GuessingGame(10)
    result = game.guess(15)
    assert result == 'high'
test_guess_high()

def test_guess_low():
    game = GuessingGame(10)
    result = game.guess(5)
    assert result == 'low'
test_guess_low()

def test_guess_correct():
    game = GuessingGame(10)
    result = game.guess(10)
    assert result == 'correct'
test_guess_correct()

def test_solved_false():
    game = GuessingGame(10)
    assert game.solved() == False
test_solved_false()
    
def test_solved_true():
    game = GuessingGame(10)
    game.guess(10)
    assert game.solved() == True
test_solved_true()