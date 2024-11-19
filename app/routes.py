from flask import Blueprint, render_template, redirect, url_for, jsonify, request, flash
from flask_login import login_user, logout_user, login_required, fresh_login_required, current_user
from .models import db, User
from app.scripts.publicpositions import get_public_positions

bp = Blueprint('main', __name__)

# UPLOAD_FOLDER = 'app/uploads'

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/loadPositions')
# Maybe need login_remembered or something if it makes you double login
@fresh_login_required
def loadPositions():
    return render_template('publicPositions.html')

@bp.route('/fetch-public-positions', methods=['POST'])
# Maybe need login_remembered or something if it makes you double login
@fresh_login_required
def fetch_public_positions():
    data = get_public_positions()
    return jsonify(data)

@bp.route('/automations')
@fresh_login_required
def automations():
    return render_template('automations.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists')
            return redirect(url_for('main.register'))

        # Create a new user
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('main.login'))

    return render_template('register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.automations'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('main.login'))

    return render_template('login.html')


@bp.route('/logout')
@fresh_login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))
    