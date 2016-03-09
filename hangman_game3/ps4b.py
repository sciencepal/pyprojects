from ps4a import *
import time



def compIsValidWord(word, hand, wordList):
    k=0
    for j in hand.keys():
        for i in word:
            if hand.get(i,0)!=0 and i==j:
                k+=1
            elif hand.get(i,0)==0:
                return False
        if k>hand[j]:
            return False
        k=0
    return True

    

#
#
# Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    word=None
    max=0
    for i in wordList:
        if compIsValidWord(i, hand, wordList)==True:
            s=getWordScore(i, n)
            if (s>max):
                word=i
                max=s
    return word

#
# Computer plays a hand
#


def compPlayHand(hand, wordList, n):
    score=0
    s=0
    while calculateHandlen(hand)>0:
        print ('Current Hand: '),
        displayHand(hand)
        word=compChooseWord(hand, wordList, n)
        if word==None:
            break
        else:
            s=getWordScore(word, n)
            score+=s
            hand=updateHand(hand, word)
            print ('\"'+word+'\"'+' earned '+(str)(s)+' points. Total: '+str(score)+' points')
            print ()
            if calculateHandlen(hand)==0:
                break
    if word==None and score!=0:
        print ('Total score: '+str(score)+' points.')
    else:
        print ('Goodbye! Total score: '+str(score)+' points.')




#
# Playing a game
#
#
def playGame(wordList):
    trial=0
    k='n'
    while k!='e':
        uc=None
        print ('**********************************************************************************')
        print ()
        k=input('Enter n to deal a new hand, r to replay the last hand, l for rules, or e to end game: ')
        print ()
        if k=='r' and trial==0:
            print ('You have not played a hand yet. Please play a new hand first!')
        elif k=='e':
            print ('Created by sciencepal')
            #sleep(1)
            print ('Thanks for playing ... More games coming soon...')
            break
        elif k=='n':
            while uc!='u' and uc!='c':
                uc=input('Enter u to have yourself play, c to have the computer play: ')
                if uc=='u':
                    trial+=1
                    hand=dealHand(HAND_SIZE)
                    h=hand.copy()
                    playHand(hand, wordList, HAND_SIZE)
                elif uc=='c':
                    trial+=1
                    hand=dealHand(HAND_SIZE)
                    h=hand.copy()
                    compPlayHand(hand, wordList, HAND_SIZE)
                else:
                    print ('Invalid command.')
        elif k=='r':
            while uc!='u' and uc!='c':
                print ()
                uc=input('Enter u to have yourself play, c to have the computer play: ')
                if uc=='u':
                    trial+=1
                    hand=h.copy()
                    playHand(hand, wordList, HAND_SIZE)
                elif uc=='c':
                    trial+=1
                    hand=h.copy()
                    compPlayHand(hand, wordList, HAND_SIZE)
                else:
                    print ('Invalid command.')
        elif k=='l':
        	print ()
        	print ("*********************Rules************************")
        	print ()
        	print ('1. You are given a list of letters initially called a starting hand')
        	print ()
        	print ('2. You can form multiple words from the hand but each letter can be used only once')
        	print ()
        	print ('3. After every word framed, the hand gets reduced')
        	print ()
        	print ('4. Form a new word from the reduced hand')
        	print ()
        	print ('5. Score for a hand = sum of values of each character in your word x length of word')
        	print ()
        	print ('5. Your score = sum of scores for each word till you play a new starting hand or replay the starting hand')
        	print ()
        	print ('6. Your score is reset once you play a new starting hand (press n for a new starting hand in main menu)')
        	print ()
        	print ('7. After playing a round, you can replay that starting hand yourself or make the computer play')
        	print ()
        	print ('8. Each letter has its own value as under : ')
        	print ()
        	print ("Letter\t  |\tValue")
        	print ()
        	for i in range(26):
        		print ('   '+chr(97+i)+'      |      '+str(SCRABBLE_LETTER_VALUES[chr(97+i)]))
        	print ()
        	print ("**************************************************")
        else:
            print ('Invalid command.')
        print ()




        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


