from flask import Flask, render_template, url_for, request,  jsonify,  redirect
import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "database.db"
)
app = Flask(__name__, static_url_path='/static')

# SQLite 데이터베이스 초기화
conn = sqlite3.connect('rps_scores.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY AUTOINCREMENT, user_score INTEGER, computer_score INTEGER);')
cursor.execute('CREATE TABLE IF NOT EXISTS results (id INTEGER PRIMARY KEY AUTOINCREMENT, user_wins INTEGER, user_loses INTEGER, user_draws INTEGER, computer_wins INTEGER, computer_loses INTEGER, computer_draws INTEGER);')
conn.commit()
conn.close()


# 점수를 데이터베이스에 추가하는 함수
def add_score(result):
    conn = sqlite3.connect('rps_scores.db')
    cursor = conn.cursor()
    if result == 'user':
        cursor.execute('UPDATE scores SET user_score = user_score + 1;')
    elif result == 'comp':
        cursor.execute('UPDATE scores SET computer_score = computer_score + 1;')
    conn.commit()
    conn.close()

# 점수를 가져오는 함수
def get_scores():
    conn = sqlite3.connect('rps_scores.db')
    cursor = conn.cursor()
    cursor.execute('SELECT user_score, computer_score FROM scores;')
    scores = cursor.fetchone()
    conn.close()
    return scores

# Flask 라우트
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/score')
def score():
    return render_template('score.html')

# JavaScript에서 호출하는 엔드포인트
@app.route('/change-score/<result>', methods=['GET'])
def change_score(result):
    add_score(result)
    return 'Score changed successfully'

# JavaScript에서 호출하는 엔드포인트
@app.route('/get-scores', methods=['GET'])
def get_scores_route():
    scores = get_scores()
    return jsonify({'user_Score': scores[0], 'computer_Score': scores[1]})

# @app.route('/test', methods=['GET'])
# def test():
#     # js -> app.py 
#     # user : paper, computer : rock, result : win
#     # save to db
#     # insert into 'tablename' values (user, computer, result)
#     scores = get_scores()
#     return jsonify({'user_Score': scores[0], 'computer_Score': scores[1]})

@app.route('/save_result', methods=['GET'])
def save_result():
    user_choice = request.args.get('user_choice')
    comp_choice = request.args.get('comp_choice')
    result = request.args.get('result')

    # 여기에서 데이터베이스에 저장하는 로직을 추가하면 됩니다.

    return "데이터가 성공적으로 저장되었습니다."

if __name__ == '__main__':
    app.run(debug=True)


