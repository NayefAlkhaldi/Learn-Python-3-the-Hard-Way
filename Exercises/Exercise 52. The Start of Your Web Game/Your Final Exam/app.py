# Modules and Packages =============================================================================
from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from re import *
from gothonweb.planisphere import *
from gothonweb import lexicon
from gothonweb.remover import *
from leaderboards.GFPP_leaderboard import *
from leaderboards.GFPP_leaderboard_display import *
from tools import start_time, end_time, calculate_time, get_real_time
from time import time
from secrets import token_urlsafe
import data.data as data
import data.save as save
import data.user_data as user_data
# ==================================================================================================

# App
app = Flask(__name__)

def reset_rooms(OnlySession=False):
    global save
    global data
    global session

    if OnlySession:
        dictionary_data = {}
        rooms_list = ['laser_weapon_armory', 'the_bridge', 'escape_pod']
        for element in rooms_list:
            if element not in session:
                try:
                    dictionary_data['GFPP'][element] = 'locked'
                except KeyError:
                    dictionary_data['GFPP'] = {element: 'locked'}
                
        session.update(dictionary_data)
        return session

    username = user_data.username
    rooms_list = ['laser_weapon_armory', 'the_bridge', 'escape_pod']
    
    if username:
        # User is signed in
        for room in rooms_list:
            try:
                save.completed[str(username)]['GFPP'][room] = 'locked'
            except KeyError:
                save.completed[username] = {'GFPP': {}}
                save.completed[str(username)]['GFPP'][room] = 'locked'

            with open("c:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercises\\Exercise 52. The Start of Your Web Game\\Your Final Exam\\data\\save.py", 'w') as file:
                file.write(f"completed = {save.completed}")
    else:
        # User not
        dictionary_data = {}
        for element in rooms_list:
            if element not in session:
                dictionary_data['GFPP'] = {element: 'locked'}

        session.update(dictionary_data) 
        return session
# Main
@app.route("/")
def main_menu():
    return render_template("main.html")


# Log in
@app.route("/login", methods=['POST', 'GET'])
def login():
    global session
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        found = False
        count = 0

        try:
            for item in range(len(data.system_logins.items())):
                if item:
                    count += 1
                    user = data.system_logins[f"{'username'}{str(count)}"]
                    pass_ = data.system_logins[f"{'password'}{str(count)}"]
                    if username == user and password == pass_:
                        found = True
                        break
                        

        except KeyError:
            pass

        if found:
            user_data.username = username
            user_data.email = data.system_emails[username]

            with open("c:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercises\\Exercise 52. The Start of Your Web Game\\Your Final Exam\\data\\user_data.py", 'w') as file:
                file.write(f"username = '{user_data.username}'\n")
                file.write(f"email = '{user_data.email}'")

            session.clear()
            return redirect(url_for("games"))

        else:
            return render_template("login.html", warning=True)
    else:
        try:
            if session['username'] or user_data.username and not request.args.get('link'):
                return redirect(url_for("games"))
            else:
                return render_template("login.html")
        except KeyError:
            return render_template("login.html")


# Sign Up
@app.route("/SignUp", methods=['POST', 'GET'])
def SignUp():
    global session
    global data
    global save
    global user_data

    # When data is given
    if request.method == "POST":
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        password_confirm = request.form['PasswordConfirm']
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        # Check email validation
        for item in data.system_emails.values():
            if email == item:
                return render_template("SignUp.html", warning=True,
                                       text=f"{email} is already in use. Please try another one.")

        if fullmatch(regex, str(email)):
            pass
        else:
            return render_template("SignUp.html", warning=True, 
                                    text="Please enter a valid email.")

        # Check username validation
        if len(username) >= 4 and username not in data.system_emails.keys():
            pass
        else:
            if len(username) < 4 or len(username) > 15:
                return render_template("SignUp.html", warning=True,
                                       text="Username length must be between 4-15 characters.")
            else:
                return render_template("SignUp.html", warning=True,
                                       text=f"{username} is already used. Please try a different username.")

        # Check password validation
        if 5 <= len(password) <= 18:
            pass
        else:
            return render_template("SignUp.html", warning=True, 
                                    text="Password must be between 5-18 characters")
        if password != password_confirm:
            return render_template("SignUp.html", warning=True, 
                                    text="The password confirming entered doesn't match.")

        user_data.username = username
        user_data.email = email

        with open("c:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercises\\Exercise 52. The Start of Your Web Game\\Your Final Exam\\data\\user_data.py", 'w') as file:
            file.write(f"username = '{user_data.username}'\n")
            file.write(f"email = '{user_data.email}'")

        data.system_emails[user_data.username] = user_data.email
        data.system_logins[f'username{data.users_number + 1}'] = user_data.username
        data.system_logins[f'password{data.users_number + 1}'] = password

        updated_users_number = f"users_number = {str(data.users_number + 1)}\n\n"
        updated_system_logins = f"system_logins = {str(data.system_logins)}\n\n"
        updated_system_emails = f"system_emails = {str(data.system_emails)}"

        # Save data to the file
        with open("c:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercises\\Exercise 52. The Start of Your Web Game\\Your Final Exam\\data\\data.py", 'w') as file:
            file.write(updated_users_number)
            file.write(updated_system_logins)
            file.write(updated_system_emails)
        # FILE WILL BE CLOSED AUTOMATICALLY

        # No need for session
        session.clear()
        return render_template("games.html")

    # Main webpage
    else:
        try:
            if session['username'] or user_data.username and not request.args.get('link'):
                return redirect(url_for("games"))
            else:
                return render_template("SignUp.html", warning=False, text=None)

        except KeyError:
            return render_template("SignUp.html", warning=False, text=None)

# Profile
@app.route("/profile")
def profile():
    username = user_data.username
    email = user_data.email

    if not username and email:
        return render_template("profile.html", name=username, email=email, not_signed_in=True)
    else:   
        return render_template("profile.html", name=username, email=email, not_signed_in=False)



# Games Section  
@app.route("/games")
def games():
    try:
        if user_data.username:
            return render_template("games.html", greeting=f"""
                Welcome, {user_data.username}! \N{grinning face with smiling eyes}
            """)

    except KeyError:
        return render_template("games.html")
    else:
        return render_template("games.html")

@app.route("/GothonsFromPlanetPercal/rooms")
def rooms():
    try:
        session['GFPP']['laser_weapon_armory'] and session['GFPP']['the_bridge'] and session['GFPP']['escape_pod']
    except KeyError:
        reset_rooms(OnlySession=True)

    try:
        if user_data.username:
            for key, value in (save.completed[user_data.username]['GFPP']).items():
                if value == 'unlocked':
                    __completed__ = True
                    pass
                else:
                    __completed__ = False
                    break

        else:
            for key, value in (session['GFPP']).items():
                if value == 'unlocked':
                    session['GFPP Completed'] = True
                else:
                    session['GFPP Completed'] = False
                    break

        return render_template("rooms.html",
                                laser_weapon_armory=\
                                save.completed[user_data.username]['GFPP']['laser_weapon_armory'],
                                the_bridge=\
                                save.completed[user_data.username]['GFPP']['the_bridge'],
                                escape_pod=\
                                save.completed[user_data.username]['GFPP']['escape_pod'], 
                                completed=__completed__)
    except KeyError:
        if not user_data.username:
            # I'm 100% Sure that user is not signed in
            reset_rooms(OnlySession=True)
            return render_template("rooms.html",
                                    laser_weapon_armory=session['GFPP']['laser_weapon_armory'],
                                    the_bridge=session['GFPP']['the_bridge'],
                                    escape_pod=session['GFPP']['escape_pod'],
                                    completed=session['GFPP Completed'])
        else:
            reset_rooms()
            return redirect(url_for('rooms'))

@app.route("/GothonsFromPlanetPercal", methods=['GET', 'POST'])
def gothons_from_planet_percal():
    global start_time
    global time
    global START
    global death_text
    global session

    start_time = time()
    session['start_time'] = start_time
    # Check for that
    # this is used to "setup" the session with starting values
    try:
        session['room_name'] = request.args.get('room_name')
    except Exception:
        session['room_name'] = START

    death_text = None

    return redirect(url_for('game'))


@app.route("/GothonsFromPlanetPercal/leaderboard")
def leaderboard():
    return render_template("leaderboard.html", 
                            __winners__= winners,
                            winners=enumerate(winners_display.keys()),
                            winning_times=list(winners_display.values()))

@app.route("/GothonsFromPlanetPercal/help")
def help():
    room = load_room(session['room_name'])
    return render_template("help.html", room=room)

@app.route("/game", methods=['GET', 'POST'])
def game():
    global start_time
    global time
    global winners
    global calculate_time
    global death_text
    global session

    if request.args.get('room_name'):
        session['room_name'] = request.args.get('room_name')
    else:
        try:
            if not session['room_name']:
                session['room_name'] = START

        except KeyError:
            return redirect(url_for("gothons_from_planet_percal"))

    room_name = session['room_name']
        

    if request.method == "GET":
        if room_name and not death_text:
            room = load_room(room_name)
            return render_template("show_room.html", room=room, 
                                    death_text=None)

        elif room_name and death_text:
            room = load_room(room_name)
            death_text__copy__ = death_text
            death_text = None
            return render_template("show_room.html", room=room, 
                                    death_text=death_text__copy__)

    else:
        action = request.form.get('action')
        action = lexicon.scan(action)
        remove(action, 'error')
        remove(action, 'stop')
        action = str(action)

        if room_name and action:
            room = load_room(room_name)
            next_room = room.go(action)

            if next_room == the_end_winner:
                if user_data.username:
                    for room in save.completed[user_data.username]['GFPP']:
                        save.completed[user_data.username]['GFPP'][room] = 'unlocked'
                        with open("c:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercises\\Exercise 52. The Start of Your Web Game\\Your Final Exam\\data\\save.py", 'w') as file:
                            file.write(f'completed = {save.completed}')
                    else:
                        try:
                            for room in session['GFPP']:
                                session['GFPP'][room] = 'unlocked'
                        except KeyError:
                            session['GFPP'] = {}
                            session['GFPP'][room] = 'unlocked'
                        session['GFPP Completed'] = True

                try:
                    end_time = time()
                    result = abs(session['start_time'] - end_time)
                    
                    try: 
                        print("I am working!\n")
                        winners[user_data.username] = int(result)
                        winners_ordered = {}

                        while True:
                            try:
                                lowest = min(winners.values())
                            except ValueError as error:
                                print(error)
                            if not winners:
                                break
                            try:
                                for winner in winners:
                                    if not winners:
                                        break
                                    if winners[winner] == lowest:
                                        winners_ordered[winner] = lowest
                                        winners.pop(winner)
                                        
                            except RuntimeError:
                                pass

                        with open("c:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercises\\Exercise 52. The Start of Your Web Game\\Your Final Exam\\leaderboards\\GFPP_leaderboard.py", 'w') as file:
                            file.write(f"winners = {winners_ordered}")
                            
                        for key, value in winners_ordered.items():
                            winners_ordered[key] = calculate_time(value)

                        winners_display = winners_ordered
                            
                        with open("c:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercises\\Exercise 52. The Start of Your Web Game\\Your Final Exam\\leaderboards\\GFPP_leaderboard_display.py", 'w') as file:
                            file.write(f"winners_display = {winners_display}")

                        if not user_data.username:
                            session['GFPP Completed'] = True
                        print(winners_display, winners_ordered)

                    except KeyError:
                        pass

                except Exception:
                    pass

                try:
                    if room_name == 'laser_weapon_armory':
                        way = str(lexicon.scan('incorrect'))

                        death_text = eval(f"{room_name}.death_texts[way]")
                    else:
                        death_text = eval(f"{room_name}.death_texts[action]")

                except KeyError:
                    pass

                if not next_room:
                    return render_template("you_died.html")

            else:
                if next_room != generic_death:
                    death_text = None

                session[name_room(next_room)] = 'unlocked'
                session['room_name'] = name_room(next_room)

        return redirect(url_for("game"))


app.secret_key = token_urlsafe(16)


if __name__ == "__main__":
    app.run(debug=True)