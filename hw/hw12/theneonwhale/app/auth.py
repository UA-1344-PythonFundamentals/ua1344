from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, db
from flask_login import login_user, login_required, logout_user
from .forms import LoginForm

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash("Username and Password are required!")
        elif User.query.filter_by(username=username).first():
            flash("Username already exists!")
        else:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(username=username, password_hash=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful! Please log in.")
            return redirect(url_for('auth.login'))
    return render_template('register.html')

@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("routes.index"))
        else:
            flash("Invalid credentials", "danger")

    return render_template("login.html", form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('routes.index'))
