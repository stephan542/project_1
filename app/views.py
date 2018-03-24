from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import CreationForm
from models import UserProfile
from werkzeug.utils import secure_filename
import datetime
import os

@app.route('/',methods=["GET","POST"])
def home():
    form = CreationForm()
    if request.method == "POST":
        if True:
            return profile()
    
    return render_template('home.html',form=form)
    
@app.route('/about/')
def about():
    return render_template('about.html')

    
@app.route('/profile' , methods=["GET","POST"])
def profile():
       form = CreationForm()
       if current_user.is_authenticated:
            return render_template("profile.html",form=form)
            
       if True:
           user = UserProfile(first_name=request.form['first_name'],last_name=request.form['last_name'],
                                email=request.form['email'],location=request.form['location'],
                                photo=request.form['photo'],bio=request.form['bio'],gender=request.form['gender'],datte=datetime.datetime.now().strftime("%B %d,%Y"))
           db.session.add(user)
           db.session.commit()
            
           file = request.files['file']
           filename = secure_filename(file.filename)
          
           file.save(os.path.join(
                app.config['UPLOAD_FOLDER'], filename
            ))
           print("ok")
           flash('You have successfully filled out the form', 'success')
           return render_template("profile.html",first_name=request.file['first_name'],last_name=request.form['last_name'],
                                email=request.form['email'],location=request.form['location'],
                                photo=request.form['photo'],bio=request.form['bio'],datte=datetime.datetime.now().strftime("%B %d,%Y"))
      
       return redirect(url_for('home'))
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")