from modules.task import task, render_template, request, redirect, url_for, flash # type: ignore
from Flask_sqlalchemy import SQLAlchemy # type: ignore
app = task(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///language_learning.db'
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    progress = db.Column(db.Integer, default=0)
    achievements = db.Column(db.String(300), default="")

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(150), nullable=False)
    answer = db.Column(db.String(100), nullable=False)
    options = db.Column(db.String(300), nullable=False)

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/lessons')
def lessons():
    lessons = Lesson.query.all()
    return render_template('lessons.html', lessons=lessons)

@app.route('/lesson/<int:id>')
def lesson(id):
    lesson = Lesson.query.get_or_404(id)
    return render_template('lesson_detail.html', lesson=lesson)

@app.route('/quiz')
def quiz():
    quizzes = Quiz.query.all()
    return render_template('quiz.html', quizzes=quizzes)

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    user_answer = request.form['answer']
    correct_answer = request.form['correct_answer']
    if user_answer == correct_answer:
        flash('Correct!', 'success')
    else:
        flash('Try again!', 'danger')
    return redirect(url_for('quiz'))

@app.route('/progress')
def progress():
    user = User.query.first()  # Just for simplicity, fetch the first user
    return render_template('progress.html', user=user)

@app.route('/forum')
def forum():
    # Here you would list forum posts, but let's just show a placeholder
    return render_template('forum.html')

if __name__ == "__main__":
    app.run(debug=True)

from app import db # type: ignore

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    progress = db.Column(db.Integer, default=0)
    achievements = db.Column(db.String(300), default="")

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(150), nullable=False)
    answer = db.Column(db.String(100), nullable=False)
    options = db.Column(db.String(300), nullable=False)

class ForumPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backed=db.backer('posts', lazy=True))

