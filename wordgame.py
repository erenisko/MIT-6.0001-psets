# Problem Set 3 
import random
import math

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

WORDLIST_FILENAME = "/Users/erenonaran/Downloads/PS3/words.txt"
with open(WORDLIST_FILENAME,"r") as f:
    wordlist = []
    for line in f:
        wordlist.append(line.strip().lower())
    print("{} words loaded.\n".format(len(wordlist)))
        
def get_word_score(word,n):
    points_for_letters = 0
    word = word.lower()
    for char in word:
        points_for_letters += SCRABBLE_LETTER_VALUES.get(char,0)
    reward_coefficient = max(1, 7*len(word)-3*(n-len(word)))
    score = points_for_letters*reward_coefficient
    return score
    
def get_frequency_dict(word):
    word = word.lower()
    frequency_dict = {}
    for char in word:
       frequency_dict[char] = frequency_dict.get(char,0) + 1
    return frequency_dict

def display_hand(hand):
    print("Current hand:",end=" ")
    for char in hand:
        for x in range(hand[char]):
            print(char, end=" ")
    print()
            
def deal_hand(n):
    hand = {"*":1}
    num_vowels = math.ceil(n/3)
    for i in range(1,num_vowels):
        char = random.choice(VOWELS)
        hand[char] = hand.get(char,0) + 1
    for i in range(num_vowels,n):
        char = random.choice(CONSONANTS)
        hand[char] = hand.get(char,0) + 1
    return hand

def update_hand(hand, word):
    word = word.lower()
    new_hand = hand.copy()
    for char in word:
        if char in new_hand:
            new_hand[char] -= 1
            if new_hand[char] == 0:
                new_hand.pop(char)
    return new_hand

def is_valid_word(word, hand, wordlist):
    word = word.lower()
    word_dict = get_frequency_dict(word)
    for char in word_dict:
        if word_dict[char] > hand.get(char,0):
            return False
    for possible_words in [word.replace("*",vowel) for vowel in VOWELS]:
        if possible_words in wordlist:
            return True
    return False


def play_hand(hand,wordlist):
    total_score = 0
    while len(hand.keys()) > 0:
        display_hand(hand)
        word = input("Enter word, or \"!!\" to indicate that you are finished: ")
        if word == "!!":
            break 
        if is_valid_word(word,hand,wordlist) == True:
            total_score += get_word_score(word, len(hand.keys()))
            print("{} earned {} points. Total: {} points\n".format(word, get_word_score(word, len(hand.keys())),total_score))
        else:
            print("That is not a valid word. Please choose another word.\n")
        hand = update_hand(hand, word)    
    if len(hand.keys()) == 0:
        print("Ran out of letters. Total score for this hand:",total_score)
    else:
        print("Total score for this hand:",total_score)
    return total_score


def substitute_hand(hand, letter):
    new_hand = hand.copy()
    if letter in hand:
        possible_letters = [letter for letter in SCRABBLE_LETTER_VALUES if letter not in new_hand]
        new_letter = random.choice(possible_letters)
        new_hand[new_letter] = new_hand[letter]
        del new_hand[letter]
    return new_hand
  
def play_game(wordlist):
    total_score_for_game = 0
    is_sub_possible = True
    is_replay_possible = True
    num_hands = int(input("Enter total number of hands: "))
    for num in range(num_hands):
        hand = deal_hand(HAND_SIZE)
        if is_sub_possible == True:
            display_hand(hand)
        if is_sub_possible == True and input("Would you like to substitute a letter? ").lower() == "yes":
            letter_to_change = input("Which letter would you like to replace: ").lower()
            hand = substitute_hand(hand, letter_to_change)
            is_sub_possible = False
        total_score_for_hand = play_hand(hand, wordlist)
        if is_replay_possible == True and input("Would you like to replay the hand? ").lower() == "yes":
            total_score_for_hand2 = play_hand(hand, wordlist)
            is_replay_possible == False
            total_score_for_game += max(total_score_for_hand,total_score_for_hand2)
        else:
            total_score_for_game += total_score_for_hand
    print("Total score over all hands:",total_score_for_game)
    return total_score_for_game









if __name__ == "__main__":
    play_game(wordlist)



