import os
from flask import Flask, render_template
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)

@app.route("/")
def home():
    user_score = None
    score_file_path = f"datafiles/{SCORES_FILE_NAME}"
    if os.path.isfile(score_file_path):
        score_file = open(score_file_path, "r")
        score_text = score_file.read()
        if score_text.isdigit():
            user_score = score_text
    if user_score == None:
        return render_template('error_view.html', error_code=BAD_RETURN_CODE)
    return render_template('score_view.html', user_score = user_score)
  
# in case you want the browser to popup automatically
import webbrowser
webbrowser.open_new('http://127.0.0.1:5000/')
app.run("0.0.0.0")

 