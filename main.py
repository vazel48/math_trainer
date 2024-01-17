from flask import Flask, render_template, request, redirect, url_for, session
import random
import time
from addition import generate_addition_question
from subtraction import generate_subtraction_question
from multiplication import generate_multiplication_question
from serverless_wsgi import handle_request
from werkzeug.wrappers import Request, Response

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        session['operation'] = request.form['operation']
        session['level'] = request.form['level']
        session['score'] = 0
        session['question_number'] = 0
        session['questions'] = []
        session['user_answers'] = []
        session['correct_answers'] = []
        session['start_time'] = time.time()  # Start the timer
        return redirect(url_for('quiz'))
    return render_template('index.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'operation' not in session or 'level' not in session:
        return redirect(url_for('home'))

    if session['question_number'] >= 15:
        session['end_time'] = time.time()  # End the timer
        return redirect(url_for('results'))

    if request.method == 'POST':
        user_answer = request.form.get('answer')
        correct_answer = session.get('answer')
        session['questions'].append(session['question'])
        session['user_answers'].append(user_answer if user_answer and user_answer.isdigit() else "No answer")
        session['correct_answers'].append(correct_answer)
        if user_answer and user_answer.isdigit() and int(user_answer) == correct_answer:
            session['score'] += 1
        session['question_number'] += 1
        return redirect(url_for('quiz'))
    else:
        operation = session['operation']
        if operation == 'random':
            operation = random.choice(['addition', 'subtraction', 'multiplication'])
        question_func = {
            'addition': generate_addition_question,
            'subtraction': generate_subtraction_question,
            'multiplication': generate_multiplication_question
        }[operation]
        question, answer = question_func(session['level'])
        session['question'] = question
        session['answer'] = answer
        return render_template('question.html', question=question, question_number=session['question_number'] + 1)


@app.route('/results')
def results():
    questions = session.get('questions', [])
    user_answers = [str(answer) if answer is not None else 'No answer' for answer in session.get('user_answers', [])]
    correct_answers = session.get('correct_answers', [])
    score = session.get('score', 0)
    elapsed_time = int(session.get('end_time', 0) - session.get('start_time', 0))
    session.clear()
    return render_template('results.html', score=score, questions=questions, user_answers=user_answers, correct_answers=correct_answers, elapsed_time=elapsed_time, zip=zip)


# Create handler for AWS Lambda
def lambda_handler(event, context):
    return handle_request(app, event, context)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
