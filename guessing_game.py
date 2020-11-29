# Author: Ryan Rochmanofenna
# Assignment #4 - Guessing Game
# Date due: 2020-11-06
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

####### DO NOT EDIT CODE BELOW (changing MAX_MISSES is ok) ########
import random
import sys

MAX_MISSES = 5
BORDER_LENGTH = 30
SINGLE_CHAR_LENGTH = 1


def display_game_state(chars, misses):
    """
    Displays the current state of the game: the list of characters to display
    and the list of misses.
    """

    print()
    print('=' * BORDER_LENGTH)
    print()

    print("Word:\t{}\n".format(space_chars(chars)))
    print("Misses:\t{}\n".format("".join(misses)))

####### DO NOT EDIT CODE ABOVE (changing MAX_MISSES is ok) ########


def blank_chars(word):

    list_of_underscores = []

    for char in word:
        list_of_underscores.append('_')
    return list_of_underscores

def space_chars(chars):

    space = ' '
    inserted_chars = space.join(chars)
    return inserted_chars

def get_guess():

    """Returns a list of positions where guess is present in word.
    An empty list should be returned when guess is not a single
    character or when guess is not present in word.


    :param word: target word as a string
    :param guess: a single character guessed by user
    :return positions: list of integer positions
    """

    uppercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    lowercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    pick_guess = True

    while pick_guess:
        guess = input("Guess:\t")
        if guess in uppercase_letters or guess in lowercase_letters and len(guess) == 1:
            return guess.lower()
        else:
            pick_guess = True

def check_guess(word, guess):

    """Returns a list of positions where guess is present in word.
    An empty list should be returned when guess is not a single
    character or when guess is not present in word.


    :param word: target word as a string
    :param guess: a single character guessed by user
    :return positions: list of integer positions
    """

    empty_list = []

    index = 0

    for char in word:
        if char == guess:
            empty_list.append(index)
            index = index + 1
        else:
            index = index + 1

    return empty_list

def update_chars(chars, guess, positions):

    for index in positions:
        chars[index] = guess

def add_to_misses(misses, guess):

    misses.append(guess)

def update_state(chars, misses, guess, positions):

    """Updates the state of the game based on user's guess. Calls the function update_chars() when
    the positions list is not empty to reveal the indices where the character guess is present. Calls the
    function add_to_misses() when the positions list is empty to add guess to the misses list.

    :param chars: a list of characters
    :param misses: list of guesses not present in target word
    :param guess: a single character guessed by user
    :param positions: list of integer positions
    :return: None
    """

    if len(positions) == 0:
        add_to_misses(misses, guess)
    else:
        update_chars(chars, guess, positions)

def is_round_complete(chars, misses):

    if len(misses) <= MAX_MISSES and not "_" in chars:
        print("\nYOU GOT IT!")
        return True
    elif len(misses) > MAX_MISSES:
        print("\nSORRY! NO GUESSES LEFT.")
        return True
    else:
        return False

def read_words(filepath):
    """Opens a file of word located at filepath, reads the file of words line by line,
    and adds each word from the file to a list. The list is returned by the
    function

    :param filepath: path to input file of words (one per line)
    :return word_list: list of strings contained in input file
    """

    list_of_words = []

    word_file = open(filepath, 'r')

    for word in word_file:
        word = word.rstrip('\n')
        list_of_words.append(word)
    word_file.close()

    return list_of_words

def get_word(words):

    random_word = words[random.randrange(0,len(words)-1)]
    return random_word

def is_game_complete():

    """Prompts the user with "Play again (Y/N)?". The question is repeated
    until the user enters a valid response (one of Y/y/N/n). The function
    returns False if the user enters 'Y' or 'y' and returns True if the user
    enters 'N' or 'n'.

    :return response: boolean representing game completion status
    """

    play_again = True

    yes_play = 'Yy'
    no_play = 'Nn'

    while play_again:
        choice = input("Play again (Y/N)?")
        if choice in yes_play:
            return False
        elif choice in no_play:
            print("\nGoodbye.")
            return True
        else:
            play_again = True

def run_guessing_game(words_filepath):

    """Controls running The Guessing Game. This includes parsing
    the words file and executing multiple rounds of the game.

    :param words_filepath: the location of the file of words for the game
    :return: None
    """

    try:
        words_in_file = read_words(words_filepath)
        print("Welcome to The Guessing Game!")
        new_round = True
        while new_round:
            game = False
            word_from_file = get_word(words_in_file)
            correct_chars = blank_chars(word_from_file)
            missed_letters = []
            while not game:
                display_game_state(correct_chars, missed_letters)
                guess_char = get_guess()
                get_positions = check_guess(word_from_file, guess_char)
                update_state(correct_chars, missed_letters, guess_char, get_positions)
                update_chars(correct_chars, guess_char, get_positions)
                game = is_round_complete(correct_chars, missed_letters)
                if game == True:
                    display_game_state(list(word_from_file), missed_letters)
                    new_round = not is_game_complete()
    except FileNotFoundError:
        print("The provided file location is not valid. Please enter a valid path to a file.")


def main():

    ########## DO NOT EDIT ASSIGNMENT STATEMENT BELOW #########

    filepath = sys.argv[-1]

    ########## DO NOT EDIT ASSIGNMENT STATEMENT ABOVE #########

    # call run_guessing_game() with filepath as argument and remove pass below
    run_guessing_game(filepath)




if __name__ == '__main__':
    main()
