import random
from hangman_art import stages
print(r'''
 __
|  |
|  |___     ___ __ __  ___     ___ __ __  ___  ____     ___ __ __ ___        
|  |__  \ /  __'  |  | __   \ / __|  |  | __  ' __  \ /  __'  |  |__  \
|  |  |  |  |__|  |  |   |  |  |__|  |  |   |  |  |  |  |__|  |  |  |  |
|__|  |__|\ ___/__|__|   |__|\____/  |__|   |__|  |__| \___/__|__|  |__|
                               __/   |
                               |____/
''')

import nltk
from nltk.corpus import words

nltk.download('words')
word_list= words.words()


chose_word = random.choice(word_list)
lives = 6

place_holder = ""
word_length = len(chose_word)

for i in range(word_length):
    place_holder += "_"
print("word to guess:" + place_holder)

game_over = False
correct_letters = []
while not game_over :
    print(f"*********************** {lives}/6 LIVES LEFT *********************************")
    user_letter = input("guess the letter: ").lower()
    if user_letter  in correct_letters:
        print(f"you already guessed {user_letter}")

    display = ""
# to print ----- with letter it prints one time
# so to continue game we have to use while at starting
    for letter in chose_word:
        if letter == user_letter:
            # we display to store and print
            display += user_letter
            correct_letters.append(user_letter)

        elif letter in correct_letters:
            display += letter

        else :
            display += "_"
    print("Word to guess :",display)



    if  user_letter not in chose_word :
        lives -= 1
        print(f"you guess {user_letter} not in the word")

        if lives == 0:
            game_over = True
            print("************************* YOU LOSE *****************************")
            print(f"THE CORRECT WORD IS : '{chose_word}' ")
    if "_" not in display:
        game_over = True
        print("You Guessed the Correct Word!!")
        print("************************** YOU WIN ******************************")

    print(stages[lives])
