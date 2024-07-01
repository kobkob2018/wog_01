from wog_helper import get_integer_in_range_from_user, clear_frame, set_new_frame_timeout
from games.geuss_game import play as play_guess_game        
from games.currency_game import play as play_currency_game
from games.memory_game import play as play_memory_game

def welcome():
    clear_frame()
    user_name = input("please enter username: ")
    print(f"Hi {user_name} and welcome to the World of Games: The Epic Journey")


available_games = [
    {'name': "Memory Game",
     'description': "a sequence of numbers will appear for 1 second and you have to guess it back."},
    {'name': "Guess Game",
     'description': "guess a number and see if you chose like the computer."},
    {'name': "Currency Roulette",
     'description': "try and guess the value of a random amount of USD in ILS"},
]


def start_play():

    for game_index, game in enumerate(available_games):
        print(f"{game_index + 1}. {game['name']} - {game['description']}")

    user_game_id = get_integer_in_range_from_user("Please select a game from the list", 1, 3) - 1
    print("your game is " + available_games[user_game_id]['name'])

    user_difficulty_selection = get_integer_in_range_from_user("Please select difficulty level from 1 to 5", 1, 5)
    print("difficulty leve: " + str(user_difficulty_selection))
    set_new_frame_timeout("Welcome to " + available_games[user_game_id]['name'], 2)
    play_again = 'y'
    while(play_again == 'y'):
        init_selected_game(user_game_id, user_difficulty_selection)
        play_again = input("Play again? (type 'y' for yes, any key for no): ")

def init_selected_game(user_game_id, user_difficulty_selection):
    if(user_game_id == 0):
        user_win = play_memory_game(user_difficulty_selection)
    elif(user_game_id == 1):
        user_win = play_guess_game(user_difficulty_selection)
    elif(user_game_id == 2):
        user_win = play_currency_game(user_difficulty_selection)
    print("user_win? "+str(user_win))