from utils import SCORES_FILE_NAME
import os

def init_score_from_file(score_file_path):
    score = 0
    if not os.path.isfile(score_file_path):
        score_file = open(score_file_path, "w")
        score_file.write("0")
        score_file.close()
    else:
        score_file = open(score_file_path, "r")
        score_text = score_file.read()
        score_file.close()
        if score_text.isdigit():
            score = int(score_text)
    return score

def add_score(difficulty_level):
    score_file_path = f"datafiles/{SCORES_FILE_NAME}"
    user_score = init_score_from_file(score_file_path)
    score_file = open(score_file_path, "w")
    add_to_score = difficulty_level*3 + 5
    user_score += add_to_score

    score_file.write(str(user_score))
