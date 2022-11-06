from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required, login_user, logout_user
from app.forms import LoginForm, RegisterForm
from app.models import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        return redirect(url_for('profile'))
    return render_template(
        'login.html',
        title='Login',
        form=form
        )


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template(
        'register.html',
        title='Register',
        form=form
        )


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
@app.route('/profile')
@login_required
def profile():
    return render_template(
        'profile.html',
        title='Profile'
        )


@app.route('/publishing')
@login_required
def publishing():
    return render_template(
        'publishing.html',
        title='Publishing'
        )


@app.route('/moderation')
@login_required
def moderation():
    return render_template(
        'moderation.html',
        title='Moderation'
        )


@app.route('/analytics')
@login_required
def analytics():
    return render_template(
        'analytics.html',
        title='Analytics'
        )
