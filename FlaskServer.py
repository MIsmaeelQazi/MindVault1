from flask import Flask, send_from_directory
import os

Diary = Flask(__name__)

@Diary.route("/")
def home():
    return send_from_directory(os.getcwd(), "index.html")

if __name__ == "__main__":
    Diary.run(host="0.0.0.0", port=5000)