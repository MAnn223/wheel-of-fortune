VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'
import random
 
class WOFPlayer():
    prizeMoney = 0
    prizes = []
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    def addMoney(self, amt):
        self.prizeMoney += amt
    def goBankrupt(self):
        self.prizeMoney = 0
    def addPrize(self, prize):
        self.prizes.append(prize)
    def __str__(self):
        return('{} (${})').format(self.name, self.prizeMoney)

class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):
        print("this function is being used")
        userInput = input('''{} has ${}
 
                 Category: {}
                 Phrase:  {}
                 Guessed: {}
 
                 Guess a letter, phrase, or type 'exit' or 'pass':'''.format(self.name, self.prizeMoney, self.category, self.obscuredPhrase, self.guessed))
        return userInput

class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
    def smartCoinFlip(self):
        #print('Entered')
        randNum = random.randint(1, 10)
        #print(randNum)
        if randNum > self.difficulty:
            return True
        else:
            return False
    def getPossibleLetters(self, guessed):
        #print('Starting method getPossibleLetters')
        possibleLetters = []
        for letter in LETTERS:
            if letter not in guessed:
                possibleLetters.append(letter)
        #print(possibleLetters)
        if WOFPlayer.prizeMoney < VOWEL_COST:
            for vowel in VOWELS:
                if vowel in possibleLetters:
                    possibleLetters.remove(vowel)
        #print(possibleLetters)
        return possibleLetters
    def getMove(self, category, obscuredPhrase, guessed):
        movePosLetters = self.getPossibleLetters(guessed)
        #print(movePosLetters)
      
        if self.getPossibleLetters(guessed) == []:
            print('Should return pass')
            return 'pass'
        moveCoinFlip = self.smartCoinFlip()
        #print(moveCoinFlip)
        freqList = list(self.SORTED_FREQUENCIES)
        r = []
        for letter in freqList:
            r.append(freqList[-1])
            freqList.pop()
          
        if moveCoinFlip is True:
            for letter in r:
                if letter in movePosLetters:
                    return letter
        else:
             return random.choice(movePosLetters)

 
class WOFPlayer():
    prizeMoney = 0
    prizes = []
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    def addMoney(self, amt):
        self.prizeMoney += amt
    def goBankrupt(self):
        self.prizeMoney = 0
    def addPrize(self, prize):
        self.prizes.append(prize)
    def __str__(self):
        return('{} (${})').format(self.name, self.prizeMoney)
            
 
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):

        userInput = input('''{} has ${}
 
                 Category: {}
                 Phrase:  {}
                 Guessed: {}
 
                 Guess a letter, phrase, or type 'exit' or 'pass':'''.format(self.name, self.prizeMoney, category, obscuredPhrase, guessed))
        return userInput
 
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
    def smartCoinFlip(self):
        #print('Entered')
        randNum = random.randint(1, 10)
        #print(randNum)
        if randNum > self.difficulty:
            return True
        else:
            return False
    def getPossibleLetters(self, guessed):
        #print('Starting method getPossibleLetters')
        possibleLetters = []
        for letter in LETTERS:
            if letter not in guessed:
                possibleLetters.append(letter)
        #print(possibleLetters)
        if WOFPlayer.prizeMoney < VOWEL_COST:
            for vowel in VOWELS:
                if vowel in possibleLetters:
                    possibleLetters.remove(vowel)
        #print(possibleLetters)
        return possibleLetters


#code below is given by the course except for wheel and phrases 
import json
import random
import time
 
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS  = 'AEIOU'
VOWEL_COST  = 250
 

def getNumberBetween(prompt, min, max):
    userinp = input(prompt) 
 
    while True:
        try:
            n = int(userinp) 
            if n < min:
                errmessage = 'Must be at least {}'.format(min)
            elif n > max:
                errmessage = 'Must be at most {}'.format(max)
            else:
                return n
        except ValueError: 
            errmessage = '{} is not a number.'.format(userinp)
 
        
        userinp = input('{}\n{}'.format(errmessage, prompt))
 

def spinWheel():
  wheel = { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to the beach!"}, { "type": "bankrupt", "text": "Bankrupt", "prize": "false" }, { "type": "loseturn", "text": "Lose a turn", "prize": "false" }, {"type": "cash", "text": "$550", "value": 550, "prize": "false"}, {"type": "cash", "text": "$150", "value": 150, "prize": "false"}, {"type": "cash", "text": "$350", "value": 350, "prize": "A free car "}, {"type": "cash", "text": "$450", "value": 450, "prize": "false"}
  return random.choice(wheel)

def getRandomCategoryAndPhrase():
  phrases = {"Celebrity": ["Selena Gomez", "Tom Cruise", "Jennifer Lopez"] , "Place":["Beach", "Park", "Pool"]}
  category = random.choice(list(phrases.keys()))
  phrase   = random.choice(phrases[category])
  return (category, phrase.upper())
 

def obscurePhrase(phrase, guessed):
    rv = ''
    for s in phrase:
        if (s in LETTERS) and (s not in guessed):
            rv = rv+'_'
        else:
            rv = rv+s
    return rv
 

def showBoard(category, obscuredPhrase, guessed):
    return """
Category: {}
Phrase:   {}
Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))
 

print('='*15)
print('WHEEL OF PYTHON')
print('='*15)
print('')
 
num_human = getNumberBetween('How many human players?', 0, 10)
 

human_players = [WOFHumanPlayer(input('Enter the name for human player #{}'.format(i+1)), 5) for i in range(num_human)]
 
num_computer = getNumberBetween('How many computer players?', 0, 10)
 

if num_computer >= 1:
    difficulty = getNumberBetween('What difficulty for the computers? (1-10)', 1, 10)
 

computer_players = [WOFComputerPlayer('Computer {}'.format(i+1), difficulty) for i in range(num_computer)]
 
players = human_players + computer_players
for i in players:
  print(i)
 

if len(players) == 0:
    print('We need players to play!')
    raise Exception('Not enough players')
 

category, phrase = getRandomCategoryAndPhrase()

guessed = []
 

playerIndex = 0
 
winner = False
 
def requestPlayerMove(player, category, guessed):
    while True: 
        time.sleep(0.5) 
        move = player.getMove(category, obscurePhrase(phrase, guessed), guessed)
        move = move.upper() 
        if move == 'EXIT' or move == 'PASS':
            return move
        elif len(move) == 1: 
            if move not in LETTERS: 
                print('Guesses should be letters. Try again.')
                continue
            elif move in guessed: 
                print('{} has already been guessed. Try again.'.format(move))
                continue
            elif move in VOWELS and player.prizeMoney < VOWEL_COST:
                    print('Need ${} to guess a vowel. Try again.'.format(VOWEL_COST))
                    continue
            else:
                return move
        else: 
            return move
 
 
while True:
    player = players[playerIndex]
    wheelPrize = spinWheel()
 
    print('')
    print('-'*15)
    print(showBoard(category, obscurePhrase(phrase, guessed), guessed))
    print('')
    print('{} spins...'.format(player.name))
    time.sleep(2)
    print('{}!'.format(wheelPrize['text']))
    time.sleep(1) 
    if wheelPrize['type'] == 'bankrupt':
        player.goBankrupt()
    elif wheelPrize['type'] == 'loseturn':
        pass 
    elif wheelPrize['type'] == 'cash':
        move = requestPlayerMove(player, category, guessed)
        if move == 'EXIT': 
            print('Until next time!')
            break
        elif move == 'PASS': 
            print('{} passes'.format(player.name))
        elif len(move) == 1:
            guessed.append(move)
 
            print('{} guesses "{}"'.format(player.name, move))
 
            if move in VOWELS:
                player.prizeMoney -= VOWEL_COST
            count = phrase.count(move) 
            if count > 0:
                if count == 1:
                    print("There is one {}".format(move))
                else:
                    print("There are {} {}'s".format(count, move))
 
                
                player.addMoney(count * wheelPrize['value'])
                if wheelPrize['prize']:
                    player.addPrize(wheelPrize['prize'])
 
               
                if obscurePhrase(phrase, guessed) == phrase:
                    winner = player
                    break
 
                continue 
 
            elif count == 0:
                print("There is no {}".format(move))
        else: 
            if move == phrase: 
                winner = player

                player.addMoney(wheelPrize['value'])
                if wheelPrize['prize']:
                    player.addPrize(wheelPrize['prize'])
 
                break
            else:
                print('{} was not the phrase'.format(move))
 
    playerIndex = (playerIndex + 1) % len(players)
 
if winner:
    print('{} wins! The phrase was {}'.format(winner.name, phrase))
    print('{} won ${}'.format(winner.name, winner.prizeMoney))
    if len(winner.prizes) > 0:
        print('{} also won:'.format(winner.name))
        for prize in winner.prizes:
            print('    - {}'.format(prize))
else:
    print('Nobody won. The phrase was {}'.format(phrase))
