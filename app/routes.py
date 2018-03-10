from app import app
from app.forms import CounterForm
from flask import render_template, flash, redirect, url_for


@app.route('/')
@app.route('/index')
def index():
    match = {
        'player_1': {'name': 'Lara', 'score': 1} ,
        'player_2': {'name': 'Mariano', 'score': 1}
    }
    return render_template('index.html', title='Home', match=match)


@app.route('/update_counter', methods=['GET', 'POST'])
def update_counter():
    form = CounterForm()
    if form.validate_on_submit():
        flash('Updating {}, remember_me={}'.format(
            form.player_1.data, form.player_2.data))
        return redirect(url_for('index'))

    return render_template('update_counter.html', title='Update counter', form=form)