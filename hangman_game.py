import random

MAX_TRIES = 5

WORDS = [
    "apple", "banana", "orange", "grape", "melon",
    "water", "house", "table", "chair", "window",
    "school", "teacher", "student", "pencil", "paper",
    "computer", "keyboard", "mouse", "screen", "phone",
    "music", "guitar", "piano", "drum", "song",
    "river", "ocean", "beach", "mountain", "forest",
    "animal", "tiger", "lion", "zebra", "monkey",
    "rabbit", "horse", "sheep", "goat", "camel",
    "bird", "eagle", "snake", "fish", "shark",
    "pizza", "bread", "cheese", "salad", "soup",
    "coffee", "sugar", "honey", "butter", "cookie",
    "happy", "angry", "funny", "quiet", "brave",
    "smart", "strong", "clean", "dirty", "small",
    "large", "short"]

def choose_random_word():
    return random.choice(WORDS)
    
def make_hidden_word_list(word_len):
    hidden_word_list = []
    for char in range(word_len):
        hidden_word_list.append('_')
    return hidden_word_list

def print_opening_screen():
    print ('''   WELCOME TO THE HANGMAN GAME   
in this game You need to reveal word 
by guessing it one letter at a time
           good luck!\n''')


def print_corrent_situation(tries_counter, hidden_word_list):
    print(f'you heve {MAX_TRIES - tries_counter} gueses left')
    print(f'corrent state of word: {' '.join(hidden_word_list)}')
    
def get_valid_input():
    is_input_valid = False
    while not is_input_valid:
        guess = input('enter your guess\n')
        if guess.isalpha() and  len(guess) == 1:
            is_input_valid = True
        else:
            print('illegal input, input must be one letter!')
    return guess

def check_if_guess_already_made(guess, previous_guesses):
    if guess in previous_guesses:
        print('guess made already')
        return True
    return False

def get_user_guess(previous_guesses):
    is_guess_made_before = True
    while is_guess_made_before:
        guess = get_valid_input()
        is_guess_made_before = check_if_guess_already_made(guess, previous_guesses)
    return guess

def update_hidden_word_list(guess, the_wining_word, hidden_word_list):
    for index, letter in enumerate(the_wining_word):
        if letter == guess:
            hidden_word_list[index] = guess
    return hidden_word_list


def end_game_message(tries_counter, the_wining_word, hidden_word_list):
    print_corrent_situation(tries_counter, hidden_word_list)
    is_won = tries_counter < MAX_TRIES
    if is_won:
        print('Congratulations you won')
    else:
        print(f'unfortunately you lost\nthe word was {the_wining_word}')

def start_game(the_wining_word, hidden_word_list, is_word_reveald, tries_counter, previous_guesses):
    while tries_counter < MAX_TRIES and not is_word_reveald:
        print_corrent_situation(tries_counter, hidden_word_list)
        guess = get_user_guess(previous_guesses)
        previous_guesses.add(guess)
        is_guess_correct = guess in the_wining_word
        if is_guess_correct:
            print ('correct guess')
            hidden_word_list = update_hidden_word_list(guess, the_wining_word, hidden_word_list)
            is_word_reveald = the_wining_word == ''.join(hidden_word_list)
        else:
            print('wrong guess')
            tries_counter += 1
    end_game_message(tries_counter, the_wining_word, hidden_word_list)
    


def initial_game():
    the_wining_word = choose_random_word()
    hidden_word_list = make_hidden_word_list(len(the_wining_word))
    is_word_reveald = False
    tries_counter = 0
    previous_guesses = set()
    print_opening_screen()
    start_game(the_wining_word, hidden_word_list, is_word_reveald, tries_counter, previous_guesses)

initial_game()

    
    