from utils import get_integer_in_range_from_user
import random


def generate_number(difficulty_level):
    return random.randint(0, difficulty_level)


def get_guess_from_user(difficulty_level):
    return get_integer_in_range_from_user("Please guess the number", 0, difficulty_level)
    

def compare_results(user_guess, generated_number):
    print(f'''The computer generated: {generated_number}
You chose: {user_guess}''')
    return user_guess == generated_number



def play(difficulty_level):
    generated_number = generate_number(difficulty_level)
    print("The computer has generated a number between 0 and " + str(difficulty_level))
    user_guess = get_guess_from_user(difficulty_level)
    return compare_results(user_guess,generated_number)
