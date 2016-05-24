# This contains our frontend; since it is a bit messy to use the @app.route
# decorator style when using application factories, all of our routes are
# inside blueprints. This is the front-facing blueprint.
#
# You can find out more about blueprints at
# http://flask.pocoo.org/docs/blueprints/

from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from markupsafe import escape

from .forms import SignupForm, InfoForm
from .nav import nav, ExtendedNavbar
from .utils import *

frontend = Blueprint('frontend', __name__)

# We're adding a navbar as well through flask-navbar. In our example, the
# navbar has an usual amount of Link-Elements, more commonly you will have a
# lot more View instances.
nav.register_element('frontend_top', ExtendedNavbar(
    title=View('ParkTrack', '.index'),
    root_class='navbar navbar-inverse',
    items=(
        View('Home', '.index'),
        View('Tracker', '.tracker'),
        View('Summary', '.summary'),
        View('Admin', '.admin'),
        View('About', '.about')
    ),
    right_items=(
        Text('ParkTrack version 1 Beta'),
        View('SignIn', '.signin'),
        View('Register', '.register')
    )
))

# Our index-page just shows a quick explanation. Check out the template
# "templates/index.html" documentation for more details.
@frontend.route('/')
def index():
    return render_template('index.html')


# Shows a long signup form, demonstrating form rendering.
@frontend.route('/register', methods=['GET', 'POST'])
def register():
    form = SignupForm()

    if form.validate_on_submit():
        # We don't have anything fancy in our application, so we are just
        # flashing a message when a user completes the form successfully.
        #
        # Note that the default flashed messages rendering allows HTML, so
        # we need to escape things if we input user values:
        flash('Hello, {}. You have successfully signed up'
              .format(escape(form.name.data)))

        # In a real application, you may wish to avoid this tedious redirect.
        return redirect(url_for('.index'))

    return render_template('signup.html', form=form)

@frontend.route('/admin', methods=['GET', 'POST'])
def admin():
    form = InfoForm()
    if request.method == 'GET':
        return render_template('admin.html', form=form)
    elif request.method == 'POST':
        try:
            insert(request.form['rid'], request.form['cid'], request.form['uid'])
            flash("Success!")
        except:
            flash('Failed!')
        return redirect(url_for('.admin')) 

@frontend.route('/summary', methods=['GET', 'POST'])
def summary():
    if request.method == 'GET':
        return render_template('summary.html', result=get_num())
    if request.method == 'POST':
        if request.json:
            data = request.get_json()
            insert_summary(data['out'], data['in'])
        return 'Success'

@frontend.route('/tracker', methods=['GET'])
def tracker():
    return render_template('tracker.html', result=get_all_entry())

# Shows a long signup form, demonstrating form rendering.
@frontend.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignupForm()

    if form.validate_on_submit():
        # We don't have anything fancy in our application, so we are just
        # flashing a message when a user completes the form successfully.
        #
        # Note that the default flashed messages rendering allows HTML, so
        # we need to escape things if we input user values:
        flash('Hello, {}. You have successfully signed up'
              .format(escape(form.name.data)))

        # In a real application, you may wish to avoid this tedious redirect.
        return redirect(url_for('.index'))

    return render_template('signup.html', form=form)


@frontend.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        if request.json:
            data = request.get_json()
            for uid in data:
                update_slot(uid, True if data[uid] == 'True' else False)
    #return "Success"

@frontend.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
