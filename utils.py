import os, time

SCORES_FILE_NAME = "score.txt"
BAD_RETURN_CODE = "506"

def get_integer_in_range_from_user(input_phrase, range_from, range_to):
    user_selection = None
    while user_selection is None:
        user_input = input(input_phrase + ": ")
        if user_input.isdigit() and range_from <= int(user_input) <= range_to:
            user_selection = int(user_input)
        else:
            print("Your selection is invalid")
    return user_selection


def exit_game(exit_phrase):
    print(exit_phrase)
    exit()

def set_new_frame_timeout(text, seconds):
    time.sleep(seconds)
    Screen_cleaner()
    print(text)

def Screen_cleaner():
    os.system('cls')
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')