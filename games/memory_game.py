from wog_helper import get_integer_in_range_from_user, set_new_frame_timeout
import random


def generate_sequence(difficulty_level):
    set_new_frame_timeout("The computer will now show you a sequence of " + str(difficulty_level) + " numbers between 0 and 10 ", 2)
    set_new_frame_timeout("Ready???", 3)
    game_sequence = []

    for i in range(difficulty_level):
        next_number = random.randint(0, 10)
        game_sequence.append(next_number)
        set_new_frame_timeout(next_number, 1)
    set_new_frame_timeout(":-|", 1)
    return game_sequence


def get_list_from_user(difficulty_level):
    set_new_frame_timeout("Let's see if you remember the values in the sequence", 0.5)
    user_list = []
    for i in range(difficulty_level):
        user_list.append(get_integer_in_range_from_user("VALUE No. " + str(i + 1), 0, 100))
    return user_list
    

def compare_results(generated_sequence, user_list):
    print("AND Now!... ")
    print("LET'S SEE IF YOU GOT IT RIGHT: ")
    user_win = True
    for i in range(len(generated_sequence)):
        print("VALUE No. " + str(i) + " WAS: " + str(generated_sequence[i]) + " AND YOU GUESSED: " + str(user_list[i])) 
        if user_list[i] != generated_sequence[i]:
            user_win = False
    return user_win

def play(difficulty_level):
    generated_sequence = generate_sequence(difficulty_level)
    user_list = get_list_from_user(difficulty_level)
    user_win = compare_results(generated_sequence, user_list)
    return user_win
