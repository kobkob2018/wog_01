import requests, json, random
from wog_helper import exit_game

def get_guess_from_user():
    user_guess = None
    while user_guess is None:
        user_input = input("Please guess the amount in USD: ")
        if user_input.isdigit():
            user_guess = int(user_input)
        else:
            print("Your guess is invalid")
    return user_guess


def get_USD_to_ILS_rates():
    url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_QvGMxyvOdOceqDlKNRRYKGcndwEro2RPmgbExvnS"
    resp = requests.get(url)
    if resp.status_code != 200:
        # print("OOPS! We are having issues connecting the currencies API. Please try again later.")
        exit_game("OOPS! We are having issues connecting the currencies API. Please try again later.")
        return None
    cur_list = json.loads(resp.text)
    return cur_list['data']['ILS']

    
def get_money_interval(difficulty_level):
    print("The computer choose a random USD amount between 0 to 100")
    USD_amount = random.randint(0, 100)
    ILS_rate = get_USD_to_ILS_rates()
    # print("rates are")
    # print(ILS_rate)
    ILS_amount = USD_amount * ILS_rate
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


