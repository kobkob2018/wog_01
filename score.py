from utils import SCORES_FILE_NAME
import os

def add_score(difficulty_level):
    score_file_path = f"datafiles/{SCORES_FILE_NAME}"
    if os.path.isfile(score_file_path):
        score_file = open(score_file_path, "w")
        print("yeees")
    else:
        score_file = open(score_file_path, "w")
        print("no file")
        score_file.write("bla")


add_score(7)