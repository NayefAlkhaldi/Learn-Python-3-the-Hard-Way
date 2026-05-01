from time import perf_counter
from secrets import token_urlsafe

from flask import Flask, session, redirect, url_for, request
from flask import render_template
import flask_login


from gothonweb.planisphere import *
from gothonweb.parser import sentence, ParserError

# NOTE: I actually stored the users data in a text file (Not recommended at all. Not even with uneccessary data.)
# I did this because I actually needed to learn sql (I will do that later and modify my app.)
# However, I have already made the base code used with sql.
# I would also like to mention that saving data in a safe way is possible with AWS (Amazon Web Services)

# NOTE: leaderboard was too hard to make, so I skipped it.

login_manager = flask_login.LoginManager()
app = Flask(__name__)
login_manager.init_app(app)

users = {'Ahmed@gmail.com': {'username': 'Ahmed', 'password': 'ahmed123', 'time': 50.41}}
user_signed_in = False
start = None
current_user = None

class User(flask_login.UserMixin):
    pass

@app.route('/')
def index():
    if not user_signed_in:
        return redirect(url_for("login"))
    if user_signed_in:
        session['room_name'] = START
        return redirect(url_for("games"))



@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return
    
    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return
    
    user = User()
    user.id = email
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    global current_user
    if request.method == 'GET':
        return render_template("login.html")

    email = request.form['email']

    if email in users and request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        current_user = email
        flask_login.login_user(user)
        return redirect(url_for('protected'))

    return 'Bad Login'

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    global current_user
    if request.method == 'GET' and not user_signed_in:
        return render_template("signin.html", error=False)
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    if username and email and password:
        user = User()
        user.id = email
        users[email] = {'username': username, 'password': password}
        current_user = email
        flask_login.login_user(user)
        return redirect(url_for('protected'))
    else:
        return render_template('signin.html', error=True)

@app.route('/protected')
@flask_login.login_required
def protected():
    global user_signed_in
    user_signed_in = True
    return redirect(url_for("games"))

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401

@app.route("/games")
def games():
    if not user_signed_in:
        return redirect(url_for("signin"))
    return render_template("games.html")

@app.route("/planet_percal", methods=['GET', 'POST'])
def planet_percal():
    global start
    global current_user
    if not user_signed_in:
        return redirect(url_for("login"))
    
    if user_signed_in:
        if not start:
            start = perf_counter()

        if not session.get('room_name'):
            session['room_name'] = START

        room = rooms[session.get('room_name')]

        if request.method == "GET":
            return render_template("show_room.html", room=room, \
                                    users=users)

        else:
            try:
                action = sentence(request.form.get('action'))
                action.cut(full=True)
                action = action.show()

            except:
                try:
                    action = sentence(request.form.get('action'))
                    action.cut(full=False)
                    action = action.show()
                except IndexError:
                    action = ''

            if room.go(action):
                
                next_room = room.go(action)
                if next_room.name == "The End Winner":
                    try:
                        if float(users[current_user].get('time')) > round(perf_counter()-start, 3):
                            users[current_user]['time'] = round(perf_counter()-start, 3)
                            start = None
                    except TypeError:
                        users[current_user].update({'time': round(perf_counter()-start, 3)})
                        start = None
                
                if next_room.name in ["The End Loser", "death"]:
                    perf_counter()
                    start = None

                if not next_room:
                    session['room_name'] = room.name
                else:
                    session['room_name'] = next_room.name

            return redirect(url_for("planet_percal"))

app.secret_key = f'{token_urlsafe(16)}'

if __name__ == "__main__":
    app.debug = True
    app.run()