from flask import Flask, render_template, g, redirect, flash, url_for, session, logging, request
# from flask_socketio import SocketIO
import os

lan_pass = input("Please input the LAN Pass for the session \n")
sign_in = False

def find_local():
	import subprocess
	return subprocess.check_output("hostname -I", shell=True).decode('utf-8').split(' ')[0]

app = Flask(__name__)
# socketio = SocketIO(app)

@app.route('/')
def main():
	return redirect(url_for('signin'))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	if request.method == 'POST':
		if request.form['pass'] == lan_pass:
			session['name'] = request.form['name']
			session['sign_in'] = True
			return redirect(url_for('main_menu'))
	return render_template('signin.html')

@app.route('/mainmenu')
def main_menu():
	if 'sign_in' in session:
		return render_template('main_menu.html')
	return redirect(url_for('signin'))

@app.route('/aboutus')
def aboutus():
	if 'sign_in' in session:
		return render_template('aboutus.html')
	return redirect(url_for('signin'))




if __name__ == "__main__":
	ip_ = find_local()
	print("Please connect to the following IP Address: {}".format(ip_))
	app.secret_key = os.urandom(36)
	app.run(host='0.0.0.0', debug=True)
