from flask import Blueprint,redirect,request,url_for,flash
from flask.templating import render_template
from app.forms import Signupform,Signinform,updateUsernameForm,updatePasswordForm
from app.models import db,User
from flask_login import login_user, logout_user,current_user,login_required
from werkzeug.security import check_password_hash,generate_password_hash

auth=Blueprint('auth',__name__,template_folder='auth_templates',url_prefix='/auth')

@auth.route('/signin',methods=['GET','POST'])
def signin():
    form= Signinform()
    if request.method=='POST':
        if form.validate_on_submit():
            print('Correct UserName and Password')
            print(form.username.data,form.password.data)
            user=User.query.filter_by(username=form.username.data).first()
            if user is None or not check_password_hash(user.password, form.password.data):
                flash('Username or Password did not match', category='danger')
                return redirect(url_for('auth.signin'))
            login_user(user)
            flash(f'Thanks for loggin in {user.username}.',category="info")
            return redirect(url_for('home'))
        else:
            flash('Incorrect User name and Password',category="danger")
            return redirect(url_for('auth.signin'))
    return render_template('signin.html', form=form)  


@auth.route('/register',methods=['GET','POST'])
def signup():
    form= Signupform()
    if request.method=='POST':
        if form.validate_on_submit():
            #print("Correct User Input")      
            #print(form.username.data,form.first_name.data,form.last_name.data)      
            new_user=User(form.first_name.data,form.last_name.data,form.email.data,form.username.data,form.password.data)
            #print(f'New user created-{new_user.__dict__}')
            try:
                db.session.add(new_user)
                db.session.commit()
                
            except:
               flash('UserName or email taken',category='warning')
               return redirect(url_for('auth.signup'))
            login_user(new_user)
            flash(f'Thanks for signing up, {new_user.first_name} {new_user.last_name}!', category='info')

            return redirect(url_for('home'))         

        else:
            flash('Bad form Input', category='warning')
            return redirect(url_for('auth.signup'))
    return render_template('signup.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been Logged out.',category="info")
    return redirect(url_for('auth.signin'))

@auth.route('/userinfo')
@login_required
def userinfo():
    return render_template('userinfo.html')

@auth.route('/profile',methods=['GET','POST'])
@login_required
def profile():
    form=updateUsernameForm()
    if request.method =='POST':
        if form.validate_on_submit() and check_password_hash(current_user.password, form.password.data):
            if User.query.filter_by(username=form.newusername.data).first():
                flash('Username already taken. Please try a different one.', category='danger')
                return redirect(url_for('auth.userinfo'))
            else:
                current_user.username=form.newusername.data
                db.session.commit()
                flash('Your user name has been updated',category="info")
                return redirect(url_for('auth.userinfo'))             
        else: 
            flash('Incorrect Password, Please try again',category="danger")
            return redirect(url_for('auth.userinfo'))              
    return render_template('profile.html',form=form)


@auth.route('/change_password',methods=['GET','POST'])
@login_required
def change_password():
    form=updatePasswordForm()
    if request.method =='POST':
        if form.validate_on_submit():
            current_user.password=generate_password_hash(form.newpassword.data  ) 
            flash('Your password has been updated',category="info")
            db.session.commit()
            return redirect(url_for('auth.userinfo'))           

        else: 
            flash('Password did not match, Please try again',category="warning")
            return redirect(url_for('auth.userinfo'))    
    return render_template('change_password.html',form=form)