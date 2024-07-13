from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/success/<name>')
def login_success(name):
   return 'Hello %s!' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('login_success', name=user))
    else:
        user = request.args.get('username')
        return redirect(url_for('login_success', name=user))


if __name__ == '__main__':
    app.run()
