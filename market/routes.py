from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
@login_required
def market_page():
    # This line below will give all the real data from the database
    # items = Item.query.all()
    # This data below is not in the database, it's just in here
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password_hash.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        # we use flash for all the messages for the users
        flash(f'Account created successfully, you are logged in as {user_to_create.username}', category='success')
        return redirect(url_for('market_page'))
    # Check that we don't have any errors in the validation for registers
    if form.errors != {}:
        for err_message in form.errors.values():
            flash(f'Error creating a user: {err_message}', category='problem')

    return render_template(('register.html'), form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username = form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password_hash.data):
            login_user(attempted_user)
            # we use flash for all the messages for the users
            flash(f'hi {attempted_user.username}, you are now logged in.', category='success')
            return redirect((url_for('market_page')))
        else:
            flash('Username and password mismatch', category='danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You are logged out", category='info')
    return redirect(url_for("home_page"))
