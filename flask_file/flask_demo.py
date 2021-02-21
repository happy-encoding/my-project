from flask import Flask, render_template
import sys

app = Flask(__name__)


@app.route("/")
def index():
    # 首页
    return render_template("index.html")
# @app.route("/movies/<classify>/<cla>")
# def genres():
#     # 电影列表
#     return render_template("genres.html")
