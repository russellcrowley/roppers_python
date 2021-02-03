#!/usr/bin/env python3
"""
The following program is meant to be a simple coin toss guessing game. 
The player gets two guesses (it’s an easy game). However, the program 
has several bugs in it. Run through the program a few times to find the 
bugs that keep the program from working correctly.
"""
import random, logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
def coin_toss():
    logging.debug("Start of program")
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    """ SOLUTION
    if guess == 'heads':
        guess = 1
    else:
        guess = 0
    """
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    # ISSUE 1 - the coin value is an int, but the guess is a string
    logging.debug("toss value is {}, guess is {}".format(toss, guess))
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input() # SOLUTION 'guesss' is misspelled
        # Poss other issue - input is a string, not int
        """ SOLUTION
                if guess == 'heads':
            guess = 1
        else:
            guess = 0
        """
        logging.debug("DEBUG: toss value is {}, guess is {}".format(toss, guess))
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')
    logging.debug("End of program")    

coin_toss()


"""
-Not really sure how to go about this one one
-Thought about starting with some unit tests and assertions
-Settled on the logging module

Ideas for future:
    -Chanage the function to actuall run the game
    -More interactive debugging account
"""