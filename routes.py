from app import app
from flask  import Flask, render_template,request,redirect,url_for
from flask_login import LoginManager , login_user , logout_user , login_required, current_user
from user_manager import UserManager
from appointments import Appointment
user_manager = UserManager()
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(username):
    return user_manager.get_user(username)

@app.route('/',methods =['POST','GET'])
def index():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        if user_manager.verify(username,password):
            login_user(user_manager.get_user(username))
            print(current_user.name)
            return redirect(url_for("home"))

        sucess = False
        error = "Invalid details were provided"
        return render_template('login.html',sucess = False , error = error)
    return render_template('login.html')


@app.route('/home', methods=['POST', 'GET'])
@login_required
def home():
    user = current_user
    return render_template('home.html',name=user.name)

@app.route('/patient_list')
@login_required
def patients():
    return render_template('patients.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route('/patient/<user>', methods=["POST", "GET"])
@login_required
def history(user):
    patient = current_user.get_patient(user)
    if request.method == 'POST':
        task = request.form["task"]
        print(task)
        patient.add_task(task)
    return render_template('history.html', user=patient)

@login_required
@app.route('/appointment/<user>', methods=["POST", "GET"])
def new_appointment(user):
    user = current_user.get_patient(user)
    if request.method == 'POST':
        date = request.form["date"]
        meds = request.form["meds"]
        notes = request.form["notes"]
        user.add_appointment(Appointment(date,meds,notes))
        return redirect(url_for("history",user=user.get_name()))
    return render_template('appointment.html', user = user)
