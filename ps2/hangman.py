# Hangman 

import random 
import string 

wordlist_filename = "words.txt"
with open(wordlist_filename,"r") as f:
    f_content = f.read()
    wordlist = f_content.split()
    print(len(wordlist), "words loaded\n")
    
def choose_random_word(wordlist):
    secret_word = random.choice(wordlist)
    return secret_word

def is_word_guessed(secret_word,letters_guessed):
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True
       
def get_guessed_word(secret_word,letters_guessed):
    guessed_word = ""
    for char in secret_word:
        if char in letters_guessed:
            guessed_word += char
        else:
            guessed_word += "_ "
    return guessed_word 
    
def get_available_letters(letters_guessed):
    available_letters = ""
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            available_letters += char
    return available_letters

def before_each_guess(remaining_warning,remaining_guess,available_letters):
    print(
"""--------------------------
You have {} warnings left.
You have {} guesses left.
Available letters: {}""".format(remaining_warning,remaining_guess,available_letters))

def without_space(string):
    new_string = ""
    for char in string:
        if char != " ":
            new_string += char
    return new_string
    
def is_input_valid(guess,letters_guessed):
    if len(guess) == 1 and guess in string.ascii_lowercase and guess not in letters_guessed:
       return True
    else:
       return False
   
def number_of_unique_letters(string):
    unique_letters = ""
    for char in string:
        if char not in unique_letters:
            unique_letters += char
    return len(unique_letters)
   

def match_with_gaps(secret_word, word_from_list, letters_guessed):
    if get_guessed_word(secret_word, letters_guessed) == get_guessed_word(word_from_list, letters_guessed):
        return True 
    return False
        

def show_possible_matches(secret_word,letters_guessed):
    possible_matches = ""
    for word in wordlist:
        if match_with_gaps(secret_word, word,letters_guessed) == True:
            possible_matches += word + " "
    if possible_matches == "":
        print("No matches found")
    else:
        print(possible_matches)
    

def hangman(secret_word):
    remaining_guess = 6
    remaining_warning = 3
    letters_guessed = []
    print(
"""Welcome to the game Hangman! 
I am thinking of a word that is {} letters long.""".format(len(secret_word)))
    while remaining_guess > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        before_each_guess(remaining_warning,remaining_guess,get_available_letters(letters_guessed))
        guess = without_space(str.lower(input("Please guess a letter: ")))
        if is_input_valid(guess,letters_guessed) == True:
            letters_guessed.append(guess)
            if guess in secret_word:
                print("Good guess: {}".format(get_guessed_word(secret_word, letters_guessed)))
            else:
                if guess in "aeiou":
                    remaining_guess -= 2
                else:
                    remaining_guess -= 1
                print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters_guessed)))
        else:
            if remaining_warning > 0:
                remaining_warning -= 1
            else:
                remaining_guess -= 1
                
            if guess in letters_guessed:
                print("Oops! You have already guessed that letter: {}".format(get_guessed_word(secret_word, letters_guessed)))
            else:
                print("Oops! That input is not a valid letter: {}".format(get_guessed_word(secret_word, letters_guessed)))
    if remaining_guess <= 0 and is_word_guessed(secret_word, letters_guessed) == False:
        print("Sorry, you ran out of guesses. The word was {}".format(secret_word))
    if remaining_guess > 0 and is_word_guessed(secret_word, letters_guessed) == True:
        total_score = remaining_guess*number_of_unique_letters(secret_word)
        print("Congratulations, you won! Your total score is: {}".format(str(total_score)))

        
def hangman_with_hints(secret_word):
    remaining_guess = 6
    remaining_warning = 3
    hint = 1
    letters_guessed = []
    print(
"""Welcome to the game Hangman! 
I am thinking of a word that is {} letters long.""".format(len(secret_word)))
    while remaining_guess > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        before_each_guess(remaining_warning,remaining_guess,get_available_letters(letters_guessed))
        guess = without_space(str.lower(input("Please guess a letter: ")))
        if is_input_valid(guess,letters_guessed) == True:
            letters_guessed.append(guess)
            if guess in secret_word:
                print("Good guess: {}".format(get_guessed_word(secret_word, letters_guessed)))
            else:
                if guess in "aeiou":
                    remaining_guess -= 2
                else:
                    remaining_guess -= 1
                print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters_guessed)))
        elif guess == "*":
            if hint > 0:
                print("Possible word matches are:")
                show_possible_matches(secret_word,letters_guessed)
                hint -= 1
            else:
                print("You have already used your hint.")
        else:
            if remaining_warning > 0:
                remaining_warning -= 1
            else:
                remaining_guess -= 1
                
            if guess in letters_guessed:
                print("Oops! You have already guessed that letter: {}".format(get_guessed_word(secret_word, letters_guessed)))
            else:
                print("Oops! That input is not a valid letter: {}".format(get_guessed_word(secret_word, letters_guessed)))
    if remaining_guess <= 0 and is_word_guessed(secret_word, letters_guessed) == False:
        print("Sorry, you ran out of guesses. The word was {}".format(secret_word))
    if remaining_guess > 0 and is_word_guessed(secret_word, letters_guessed) == True:
        total_score = remaining_guess*number_of_unique_letters(secret_word)
        print("Congratulations, you won! Your total score is: {}".format(str(total_score)))
    
        

        
        
if __name__ == "__main__":
    secret_word = choose_random_word(wordlist)
    # hangman(secret_word)
    hangman_with_hints(secret_word)
            
        


       