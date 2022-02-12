import random
import string

WORDLIST_FILENAME = "words.txt"

inFile = open(WORDLIST_FILENAME, 'r')
line = inFile.readline()
wordlist = line.split()
print("  ", len(wordlist), "words loaded.")

secret_word = str(random.choice(wordlist))
print(secret_word)
letters_guessed = ""
a = list(secret_word)
x = list(letters_guessed)
common_list = []
noncommon_list = []
alphabets = "abcdefghijklmnopqrstuvwxyz"
alphabets_list = list(alphabets)
word = "_" * int(len(secret_word))
convert = list(word)

print("""Welcome to the game Hangman!
I am thinking of a word that is """ +str(int(len(secret_word))) + """ letters long
You have 6 guesses left.
You have 3 warnings left.
Available letters: abcdefghijklmnopqrstuvwxyz""")


for no_of_guesses in range(1, 7):
    guess = input("Please guess a letter:")
    if guess in x:
       print("Oops! You've already guessed that letter. You have 2 warning left.")

    elif guess not in alphabets_list:
       print("Oops! That is not a valid letter. You have 2 warnings left")

    else:
        x.append(guess)                            #adding letter in letter guessed list

    if guess in a:
        common_list.append(guess)
    else:
        noncommon_list.append(guess)

    if len(common_list) != 0:

        for i in range(0, len(secret_word)):
            if secret_word[i] == guess:
                del convert[i]
                convert.insert(i, guess)
        print("Good guess: "+ ''.join(convert))
        if ''.join(convert) == str(secret_word):
            print("""Congratulations! You have guessed the word.
        You won!""")
            break
        print("You have " + str(6-int(no_of_guesses)) + " guesses remaining.")
        alphabets_list.remove(guess)
        y = ''.join(alphabets_list)
        print("Available letters: " + y)

    else:
        word = "_" * int(len(secret_word))
        print("Oops! That letter is not in my word: " + str(word))
        print("You have " + str(6-int(no_of_guesses)) + " guesses remaining.")
        if no_of_guesses == 6:
            print("Sorry, you ran out of guesses. The word was: " + secret_word)
            break
        alphabets_list.remove(guess)
        y = ''.join(alphabets_list)
        print("Available letters: " + y)
