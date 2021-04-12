# Create website route.
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


# auth, url_prefix='/auth'
# If we want to access to the bellow pages, URL: https://localhost/auth/xxx
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # If the user login
    if request.method == 'POST':
        # Get the login info from frontend.
        email = request.form.get('email')
        password = request.form.get('password')

        # Check login info
        # Use login info to find the record.
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                # Store the user's info
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect username or password.', category='error')
        else:
            flash('Email does not exsit.', category='error')

    # Show Login page and transfer user to the frontend.
    return render_template('login.html', user=current_user)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # If the user click 'submit' button to sign up
    if request.method == 'POST':
        # Get the sign up info from frontend
        first_name = request.form.get('firstName')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Check sign up info
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exsit.', category='error')
        # Each columns restrictions
        elif len(first_name) < 1:
            flash('First name must be greater than 1 character.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 5:
            flash('Password must be greater than 5 characters.', category='error')
        else:
            # Add new user to database
            new_user = User(first_name=first_name, email=email,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            # Store the user's info
            login_user(new_user, remember=True)
            flash('Account created!', category='success')

            return redirect(url_for('views.home'))
    # Show Sign Up page and transfer user to the frontend.
    return render_template('sign_up.html', user=current_user)


@auth.route('/logout')
@login_required  # User can't access to '/logout' if user does not log in.
def logout():
    # Clear user's info
    logout_user()
    # Redirect to the Login Page
    return redirect(url_for('auth.login'))
