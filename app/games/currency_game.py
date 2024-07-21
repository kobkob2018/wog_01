from currency_converter import CurrencyConverter
from utils import exit_game
import random

def get_guess_from_user():
    user_guess = None
    while user_guess is None:
        user_input = input("Please guess the amount in USD: ")
        if user_input.isdigit():
            user_guess = int(user_input)
        else:
            print("Your guess is invalid")
    return user_guess
    
def get_money_interval(difficulty_level):

    print("The computer choose a random USD amount between 0 to 100")
    converter = CurrencyConverter()

    USD_amount = random.randint(0, 100)
    ILS_amount = converter.convert(USD_amount, 'USD', 'ILS')

    difficulty_offset = 6 - difficulty_level
    money_interval_arr = {"ILS_amount":ILS_amount, "USD_amount":USD_amount, "from":USD_amount - difficulty_offset, "to":USD_amount + difficulty_offset, "difficulty_level": difficulty_level, "difficulty_offset": difficulty_offset}
    return money_interval_arr



def compare_results(user_guess, money_interval_arr):
    print("THE TRUE AMOUNT IN USD IS: " + str(money_interval_arr["USD_amount"]))
    return user_guess >= money_interval_arr['from'] and user_guess <= money_interval_arr['to']



def play(difficulty_level):
    money_interval_arr = get_money_interval(difficulty_level)
    # print(money_interval_arr)
    print(f'''THE AMOUNT IN ILS IS: {money_interval_arr["ILS_amount"]} 
You need to guess the amount IN USD with offset less then  {money_interval_arr['difficulty_offset']}''')    
    user_guess = get_guess_from_user()
    # print("THE TRUE AMOUNT IN USD IS: " + str(money_interval_arr["USD_amount"]))
    user_win = compare_results(user_guess, money_interval_arr)
    if(user_win):
        print("Very good :)")
    else: 
        print(":(")
    return user_win


