from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from market import db
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    if request.method == "POST":
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.owner = current_user.id
                current_user.budget -= p_item_object.price
                db.session.commit()
                flash(f"You have purchased {p_item_object.name} for {p_item_object.price}", category="success")
            else:
                flash(f"You don't have enough money", category="danger")

    # if request.method == "GET":
    items = Item.query.filter_by(owner=None)
    return render_template('market.html', items=items, purchase_form=purchase_form)


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
        attempted_user = User.query.filter_by(username=form.username.data).first()
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
