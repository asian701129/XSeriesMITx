from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    currentBestScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    currentBestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if (isValidWord(word, hand, wordList)):
            # Find out how much making that word is worth
            thisWordScore = getWordScore(word, len(word))
            # If the score for that word is higher than your best score
            if (thisWordScore > currentBestScore):
                # Update your best score, and best word accordingly
                currentBestScore = thisWordScore
                currentBestWord = word

    # return the best word you found.
    return currentBestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    
    # Keep track of the total score
    handScore = 0
    # As long as there are still letters left in the hand:
    while (True):
        # Display the hand
        print ("Current Hand: "),
        displayHand(hand),
        # Ask the computer to chose a word
        wordCompChose = compChooseWord(hand, wordList, n)
        # If no more words can be made, we're done
        if (wordCompChose == None):
            break                  
        
        # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
        wordScore = getWordScore(wordCompChose, n)
        handScore = handScore + wordScore
        print( '"' + str(wordCompChose) + '" earned ' + str(wordScore) + " points. Total: " + str(handScore) + " points")
        # Update the hand
        hand = updateHand(hand, wordCompChose)


        print
        lettersUsedUp = 0
        for counter in hand.itervalues():
            if counter == 0: #this value is empty
                lettersUsedUp = lettersUsedUp + 1
            else: #this value is not used up
                continue
        if lettersUsedUp == len(hand): #if all the letters are used up
            break
    print('Total score: ' + str(handScore) + 'points.')




#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    hand = {}
    while (True):
        print
        
        # Prompt the user for the hand to use
        mode = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        
        # If not valid get a new input
        if not(mode == 'n' or mode == 'r' or mode == 'e'):
            print("Invalid command.")
            continue
        # If e was chosen then exit
        if mode == 'e': # do we exit?
            return
        # If r was chosen, verify there was a prior hand
        if mode == 'r':
            if hand == {}:
                print ("You have not played a hand yet. Please play a new hand first!")
                continue
        # if n was chose, make the new hand
        if mode == 'n':
            hand = dealHand(HAND_SIZE)

        mode2 = ''
        # Now prompt the user to determine who plays
        while not(mode2 == 'c' or mode2 == 'u'):
            mode2 = raw_input('Enter u to have yourself play, c to have the computer play: ')
            # you play
            if (mode2 == 'u'):
                if (mode == 'n'):
                    playHand(hand,wordList,HAND_SIZE)
                elif mode == 'r':
                    playHand(hand,wordList,HAND_SIZE)
            # computer plays
            elif (mode2 == 'c'):
                if (mode == 'n'):
                    compPlayHand(hand,wordList,HAND_SIZE)
                elif mode == 'r':
                    compPlayHand(hand,wordList,HAND_SIZE)
            # nobody plays ask again
            else:
                print("Invalid command.")


        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


