from flask import Blueprint, render_template, request, redirect, url_for, flash
from drone_inventory.forms import UserLoginForm
from flask import request
from drone_inventory.models import User, db

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    userform = UserLoginForm()

    try:
        if request.method == 'POST' and userform.validate_on_submit():
            email = userform.email.data
            username = userform.username.data
            password = userform.password.data
            print(email, password)

            user = User(email, username, password)

            db.session.add(user)
            db.session.commit()
    
            flash(f'You have successfully created a user account {email}', 'user-created')
            
            return redirect(url_for('site.home'))

         
    except:
        raise Exception('Invalid Form Data. Please Check your form')
    
    return render_template('signup.html', form=userform)

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    return render_template('signin.html')

    

