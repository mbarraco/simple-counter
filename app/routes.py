from app.forms import CounterForm, LoginForm
from flask import (render_template,
    flash,
    redirect,
    url_for,
    request
)
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app, db
from app.models import User
from app.forms import RegistrationForm


@app.route('/')
@app.route('/index')
@login_required
def index():
    match = {
        'player_1': {'name': 'Lara', 'score': 1} ,
        'player_2': {'name': 'Mariano', 'score': 1}
    }
    return render_template('index.html', title='Home', match=match)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        #  Handle 'next' query string arg.
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/update_counter', methods=['GET', 'POST'])
@login_required
def update_counter():
    form = CounterForm()
    if form.validate_on_submit():
        flash('Updating {}, remember_me={}'.format(
            form.player_1.data, form.player_2.data))
        return redirect(url_for('index'))

    return render_template('update_counter.html', title='Update counter', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/counter')
def counter():
    return render_template('counter.html')
