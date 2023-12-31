# This program is a game of hangman

import random
word_list = ["awkward", "bagpipes", "croquet", "dwarves", "equip", "flapjack", "gossip", "hyphen", "ivory", "jumbo", "kiwifruit", "luxury", "microwave", "nightclub", "oxygen", "puppy", "quartz", "rhythm", "syndrome", "transplant", "unknown", "vodka", "wavy", "xylophone", "yummy", "zodiac"]

chosen_word = random.choice(word_list) # A random word is chosen from the word list using
chosen_word_list = list(chosen_word) # Converts the random word into a list with the letters separated
guess_gaps = ""
display_list = []
lives = 6

logo = '''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    '''
print(logo)
print("Welcome to Hangman!")

for letter in chosen_word: # YOU CAN LOOP THROUGH A WORD!! e.g you can loop through the word manicure. It doesn't just have to be a list you loop through
    guess_gaps += "_ " # For each letter in the random word, a "_" will be added to the guess_gaps variable. e.g mouse = _ _ _ _ _
    display_list += "_" # The "_" will be stored in a list. e.g cat = ["_", "_", "_"]

print(guess_gaps) # _ _ _ _ is printed out
end_of_game = False

while end_of_game == False: # Whilst the chosen word is not equal to the blanks
    guess_letter = input("Guess a letter: ").lower() # The user will continue to be asked to enter a letter until the blanks are filled out and match the chosen word
    if guess_letter in display_list:
        print(f"You have already guessed {guess_letter}, Try again.")

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess_letter: # e.g the word is mouse: if chosen_word[4], ("e"), is equal to the letter guessed "e"
            display_list[i] = guess_letter # e.g _ _ _ _ _ will become _ _ _ _ e since "e" has been guessed (FOR THE "mouse" example)

    word_combined = " ".join(display_list) # e.g This converts ["d", "o", "g"] to d o g using the " " before the .join()
    print(word_combined)

    stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

    if guess_letter not in chosen_word:
        lives = lives - 1
        print("Try again. ")

    if lives == 6:
        print(stages[6])
    elif lives == 5:
        print(stages[5])
    elif lives == 4:
        print(stages[4])
    elif lives == 3:
        print(stages[3])
    elif lives == 2:
        print(stages[2])
    elif lives == 1:
        print(stages[1])
    elif lives == 0:
        print(stages[0])

    if lives == 0:
       end_of_game = True # This ends the while loop
       print(f"YOU LOST! The word was {chosen_word}.")

    if "_" not in display_list:
        end_of_game = True # This also ends the while loop
        print(f"You guessed the word: {chosen_word}!")
