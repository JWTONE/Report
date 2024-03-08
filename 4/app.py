from flask import Flask, render_template, url_for, request,  jsonify,  redirect
import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite를 사용하는 예시
db = SQLAlchemy(app)

class Score(db.Model):
    __table_name__ = 'score'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    profile_image = db.Column(db.String(100), default='default.png')

    def __repr__(self):
        return f"<User('{self.id}', '{self.username}', '{self.email}')>"


@app.route('/play_game', methods=['POST'])
def play_game():
    user_choice = request.form.get('user_choice')
    comp_choice = get_computer_choice()

    result = determine_winner(user_choice, comp_choice)

    update_score(result)

    return jsonify({'result': result, 'comp_choice': comp_choice})

def get_computer_choice():
    # 여기에 컴퓨터가 무작위로 가위, 바위, 보 중 하나를 선택하는 코드 추가
    pass

def determine_winner(user_choice, comp_choice):
    # 여기에 가위바위보 승패를 판단하는 코드 추가
    # 결과에 따라 'user', 'comp', 'draw' 등을 반환
    pass

def update_score(result):
    score_entry = Score.query.first()
    if score_entry is None:
        score_entry = Score()

    if result == 'user':
        score_entry.user_score += 1
    elif result == 'comp':
        score_entry.computer_score += 1

    db.session.add(score_entry)
    db.session.commit()

@app.route('/update_score_data', methods=['POST'])
def update_score_data():
    data = request.json
    user_score = data.get('userScore')
    computer_score = data.get('computerScore')

    # 디버깅 코드 추가
    print(f"Received data: userScore={user_score}, computerScore={computer_score}")

    # 데이터베이스 업데이트
    score_entry = Score.query.first()
    if score_entry is None:
        score_entry = Score()
    score_entry.user_score = user_score
    score_entry.computer_score = computer_score

    # 디버깅 코드 추가
    print(f"Before commit: user_score={score_entry.user_score}, computer_score={score_entry.computer_score}")

    db.session.add(score_entry)
    db.session.commit()

    # 디버깅 코드 추가
    print(f"After commit: user_score={score_entry.user_score}, computer_score={score_entry.computer_score}")

    return jsonify({'success': True})


# Flask 라우트
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/score')
def score():
    return render_template('score.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


