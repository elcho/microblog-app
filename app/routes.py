from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Lakewood!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Pesach is almost here!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/wisdom')
def second_page():
    user = {'username': 'Elchonon'}
    messages = [
        {
            'message': 'A drop of honey catches more flies than a gallon of gall.'
        },
        {
            'message': 'A calm and honest life brings more happiness than the pursuit of success and restlessness.'
        }
    ]
    return render_template('wisdom.html', title='Home', user=user, messages=messages)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
