from flask import Flask, render_template, g, redirect, flash, url_for, session, logging, request, flash
from flask_mail import Mail, Message, Attachment
# from wtforms import Form, StringField, PasswordField, validators
from passlib.hash import sha256_crypt
import sys, os
import dataclass

app = Flask(__name__)
app.secret_key = os.urandom(36)


app.config.update(DEBUG=True,
                  MAIL_SERVER='smtp.gmail.com',
                  MAIL_PORT=465,
                  MAIL_USE_SSL=True,
                  MAIL_USERNAME = 'yatharthrai16@gmail.com',
                  MAIL_PASSWORD = 'everyoneknowsiminovermyheadovermyhead')

@app.route('/')
def main():
    return redirect(url_for('signin'))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        if request.form['employee_ID'] == '9415':
            if request.form['employee_pass'] == 'hello':
                session['user'] = request.form['employee_ID']
                session['name'] = 'Yatharth'
                return redirect(url_for('employee'))
        session['user'] = request.form['employee_ID']
    return render_template('signin.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        dept = request.form['dept']
        hod = request.form['hod']
        passw = sha256_crypt.encrypt(request.form['passw'])
        flash('Account Created')
        return redirect(url_for('signin'))
    return render_template('register.html')

@app.route('/employee', methods=['GET', 'POST'])
def employee():
    if g.user:
        return render_template('employee.html', username=g.user,
                                name='Yatharth',
                                dept='Computer Science',
                                email='yatharthrai16@gmail.com',
                                hod_email='yatharthrai16@ducic.ac.in')
    return redirect(url_for('signin'))

@app.route('/leave', methods=['GET', 'POST'])
def leave():
    if g.user:
        if request.method == 'POST':
            mail = Mail(app)
            from_date, to_date = request.form['from_date'], request.form['to_date']
            place = "{}, {}, {}".format(request.form['place_'], request.form['city_'], request.form['state_'])
            message = "I, {} shall be on a field trip from {} to {} in {}.".format(session['name'], from_date, to_date, place)
            subject = "Field Trip - {}".format(session['name'])
            msg = Message(subject,
                          sender="<"+session['name']+">",
                          recipients=["yatharthrai16@ducic.ac.in"])
            msg.body = message
            mail.send(msg)
        return render_template('leave.html')
    return redirect(url_for('signin'))


@app.route('/fieldtrip', methods=['GET', 'POST'])
def fieldtrip():
    if g.user:
        if request.method == 'POST':
            mail = Mail(app)
            from_date, to_date = request.form['from_date'], request.form['to_date']
            place = "{}, {}, {}".format(request.form['place_'], request.form['city_'], request.form['state_'])
            message = "I, {} shall be on a field trip from {} to {} in {}.".format(session['name'], from_date, to_date, place)
            subject = "Field Trip - {}".format(session['name'])
            msg = Message(subject,
                          sender="<"+session['name']+">",
                          recipients=["yatharthrai16@ducic.ac.in"])
            msg.body = message
            mail.send(msg)
        return render_template('fieldtrip.html')
    return redirect(url_for('signin'))

@app.route('/editprofile')
def editprofile():
    return render_template('editprofile.html')

@app.route('/admin')
def admin():
    if g.user:
        return render_template('admin.html')
    return redirect(url_for('signin'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

if __name__ == "__main__":
    app.run(debug=True)
