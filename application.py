import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta


app = Flask(__name__)
app.config['SECRET_KEY'] = b'\x0f\xc2\x1ca\xb2\xf4\xfbi\x9c\x17L\x10\xc5uJU\xb9q\x96r,\xb8\x01u'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///final.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=30)
db = SQLAlchemy(app)


class users(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.TEXT, unique=True, nullable=False)
    hash = db.Column('hash', db.TEXT, unique=True, nullable=False)

    def __init__(self, username, hash):
        self.username = username
        self.hash = hash


class entries(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer,
                        db.ForeignKey('users.id'), nullable=False)
    date = db.Column('date', db.DateTime, default=datetime.utcnow)
    journal_entry = db.Column('journal_entry', db.TEXT, nullable=False)

    def __init__(self, user_id, date, journal_entry):
        self.user_id = user_id
        self.date = date
        self.journal_entry = journal_entry


class Addresses(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer,
                        db.ForeignKey('users.id'), nullable=False)
    first_name = db.Column('first_name', db.TEXT, nullable=False)
    last_name = db.Column('last_name', db.TEXT, nullable=True)
    street1 = db.Column('street1', db.TEXT, nullable=False)
    street2 = db.Column('street2', db.TEXT, nullable=True)
    city = db.Column('city', db.TEXT, nullable=True)
    state = db.Column('state', db.CHAR(2), nullable=True)
    zip_code = db.Column('zip_code', db.VARCHAR(10), nullable=True)
    phone = db.Column('phone', db.VARCHAR(22), nullable=False)
    email = db.Column('email', db.TEXT, nullable=True)
    notes = db.Column('notes', db.TEXT, nullable=True)

    def __init__(self, user_id, first_name, last_name, street1, street2, city, state, zip_code, phone, email, notes):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email
        self.notes = notes


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return wrap


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route('/verses')
def verses():
    return render_template("verses.html")


@app.route("/journal", methods=["GET", "POST"])
@login_required
def journal():
    if request.method == "POST":
        user_id = session["user_id"]
        date = request.form.get("date")
        entry = request.form.get("entry")

        # Confirm journal entry
        if not entry:
            flash(f"Nothing entered for today \U0001F928!")
            return redirect("/")

         # Insert journal entry into datebase
        ent = entries(user_id=user_id, date=date, journal_entry=entry)

        db.session.add(ent)
        db.session.commit()

        flash(f"Today's entry has been submitted \U0001F600!")
        return redirect("/")

    else:
        return render_template("journal.html")


@app.route("/entries")
@login_required
def journal_entries():
    user_id = session["user_id"]
    entry = entries.query.filter_by(user_id=user_id).all()

    return render_template("entries.html", entries=entry)


@app.route('/delete_entry/<int:id>')
def delete_entry(id):
    entry_to_delete = entries.query.get_or_404(id)
    try:
        db.session.delete(entry_to_delete)
        db.session.commit()
        flash(f"Entry has been deleted \U0001F600!")
        return redirect("/")

    except:
        flash(f"There was a problem deleting that entry \U0001F928!")
        return redirect("/")


@app.route("/address_book", methods=["GET", "POST"])
@login_required
def address():

    if request.method == "POST":
        user_id = session["user_id"]
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        street1 = request.form.get("street1")
        street2 = request.form.get("street2")
        city = request.form.get("city")
        state = request.form.get("state")
        zip_code = request.form.get("zip")
        phone = request.form.get("phone")
        email = request.form.get("email")
        notes = request.form.get("notes")

        # Confirm necessary info provided
        if not fname:
            flash(f"Please provide first name \U0001F928!")
            return render_template("address_book.html")

        if not street1:
            flash(f"Please provide street address \U0001F928!")
            return render_template("address_book.html")

        if not phone:
            flash(f"Please provide phone number \U0001F928!")
            return render_template("address_book.html")

        # Insert contact info into datebase

        contact = Addresses(user_id=user_id, first_name=fname, last_name=lname, street1=street1,
                            street2=street2, city=city, state=state, zip_code=zip_code, phone=phone, email=email, notes=notes)

        db.session.add(contact)
        db.session.commit()

        flash(f"Contact has been added \U0001F600!")
        return redirect("/")

    else:
        return render_template("address_book.html")


@app.route("/address_list")
@login_required
def address_list():
    user_id = session["user_id"]

    contact = Addresses.query.filter_by(
        user_id=user_id).order_by(Addresses.last_name).all()

    return render_template("address_list.html", contacts=contact)

# Users can update their contacts


@app.route("/edit_contact/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    contact_to_edit = Addresses.query.get_or_404(id)
    if request.method == "POST":
        contact_to_edit.first_name = request.form.get("first_name")
        contact_to_edit.last_name = request.form.get("last_name")
        contact_to_edit.street1 = request.form.get("street1")
        contact_to_edit.street2 = request.form.get("street2")
        contact_to_edit.city = request.form.get("city")
        contact_to_edit.state = request.form.get("state")
        contact_to_edit.zip_code = request.form.get("zip")
        contact_to_edit.phone = request.form.get("phone")
        contact_to_edit.email = request.form.get("email")
        contact_to_edit.notes = request.form.get("notes")

        # Confirm necessary info provided
        if not contact_to_edit.first_name:
            flash(f"Please provide first name \U0001F928!")
            return render_template("edit_contact.html", contact_to_edit=contact_to_edit, id=id)

        if not contact_to_edit.street1:
            flash(f"Please provide street address \U0001F928!")
            return render_template("edit_contact.html", contact_to_edit=contact_to_edit, id=id)

        if not contact_to_edit.phone:
            flash(f"Please provide phone number \U0001F928!")
            return render_template("edit_contact.html", contact_to_edit=contact_to_edit, id=id)

        try:
            db.session.commit()
            flash(f"Contact has been edited \U0001F600!")
            return render_template("edit_contact.html", contact_to_edit=contact_to_edit, id=id)

        except:
            flash(f"Sorry, something went wrong! Contact not edited \U0001F928!")
            return redirect("/")

    else:
        return render_template("edit_contact.html", contact_to_edit=contact_to_edit, id=id)


@app.route('/delete/<int:id>')
def delete(id):
    contact_to_delete = Addresses.query.get_or_404(id)
    try:
        db.session.delete(contact_to_delete)
        db.session.commit()
        flash(f"Contact has been deleted \U0001F600!")
        return redirect("/")

    except:
        flash(f"Oops! There seems to be a problem. Contact NOT deleted \U0001F928!")
        return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        name = request.form.get("username")
        hash = request.form.get("password")

        user = users.query.filter_by(username=name).first()

        if not user or not check_password_hash(user.hash, hash):
            flash(f"Username and/or password invalid, please try again \U0001F928!")
            return render_template("login.html")

        # Remember which user has logged in
        session["user_id"] = user.id

        # Welcome user
        name = request.form.get("first_name").capitalize()
        flash(f"Nice to see you today, {name} \U0001F600!")

        # Redirect user home
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()

    # Say good-bye to users
    flash(f"See you again soon \U0001F600!")

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")

        user = users.query.filter_by(username=name).first()
        if user:
            return redirect("login")

        new_user = users(username=name, hash=generate_password_hash(
            password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()

        # Let users know they are registered
        flash(f"You are registered \U0001F600!")
        return redirect("/")

    else:
        return render_template("register.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
        flash(e.name, e.code)
        return redirect("/")


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == "__main__":
    db.create_all()
    app.run()
