from flask import Flask
from flask import render_template
import templates

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/welcome/<string:student_name>/')
def welcome(student_name):
    return render_template("welcome.html", student_name=student_name)


@app.route('/roster/<int:roster_view>/')
def roster(roster_view):
    c = [
        {
            'name': "s1",
            'grade': 100,
            'stand': "sophomore"
        },
        {
            'name': "s2",
            'grade': 90,
            'stand': "freshman"
        },
        {
            'name': "s3",
            'grade': 50,
            'stand': "Senior"
        },
        {
            'name': "s1",
            'grade': 100,
            'stand': "sophomore"
        },
        {
            'name': "s2",
            'grade': 90,
            'stand': "freshman"
        },
        {
            'name': "s3",
            'grade': 50,
            'stand': "Senior"
        },
        {
            'name': "s3",
            'grade': 50,
            'stand': "Senior"
        }

    ]

    return render_template("roster.html", view=roster_view, roster1=c)


if __name__ == '__main__':
    app.run()
