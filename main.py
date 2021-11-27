from flask import Flask, redirect, url_for, render_template, request
from branch import *
import time
app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    if request.method=="POST":
        if request.form.get("Start"):
            return redirect(url_for("room_one"))
    return render_template("home.html")

@app.route("/start", methods=["POST","GET"])
def room_one():
    if request.method=="POST":
        email=request.form["email"]
        if email=="" or not "." in email:
            return render_template("room_one.html") 
        for i in range(1,4):
            room_1.checkboxes.append(True if request.form.get("exampleCheck"+str(i))=="on" else False)
        room_1.update_traits()
        result.email = email
        return redirect(url_for("room_two",user_email=email))
    return render_template("room_one.html")

@app.route("/<user_email>", methods=["POST","GET"])
def room_two(user_email):
    if request.method=="POST":
        if request.form.get("Skip"):
            return redirect(url_for("room_three",Skip="True"))
    room_2.send_email(user_email)
    return render_template("room_two.html")

@app.route("/Wakeup",methods=["POST","GET"])
def room_three(Skip=None):
    if request.method=="POST":
        room_3.selection(request.form.get("option_select"))
        return redirect(url_for("room_four"))
    if Skip:
        room_2.update_traits()
    return render_template("room_three.html",room_3=room_3)

@app.route("/Puzzle",methods=["POST","GET"])
def room_four():
    if request.method=="POST":
        return redirect(url_for("room_five"))
    room_4.start_time=time.time()
    return render_template("room_four.html",room_4=room_4,cards=4)

@app.route("/Carstop",methods=["POST","GET"])
def room_five():
    if request.method=="POST":
        if (request.form.get("Fix Me"))!=None:
            return redirect(url_for("room_six"))
        return redirect(url_for("room_five_body"))
    end=time.time()
    room_4.update_traits((end-room_4.start_time)*2)
    return render_template("room_five.html",room_5=room_5)

    
@app.route("/Roomfivebody",methods=["POST","GET"])
def room_five_body():
    if request.method=="POST":
        if room_5_body.count <= 50:
            room_5_body.count += 1
        else:
            room_5_body.update_traits()
            return redirect(url_for("room_six"))
    return render_template("room_five_body.html",room5_body=room5_body)

@app.route("/Fixcar",methods=["POST","GET"])
def room_six():
    if request.method=="POST":
        print(True)
        return redirect(url_for("results_room"))
    return render_template("room_six.html",room_6=room_6)

@app.route("/Fixpuzzle",methods=["POST","GET"])
def room_six_puzzle():
    return render_template("puzzle_six.html",room_6_puzzle=room6())

@app.route("/Results",methods=["POST","GET"])
def results_room():
    result.send_result_email()
    return render_template("results.html",result=results)

room_1=room1()
room_2=room2()
room_3=room3()
room_4=room4()
room_5=room5()
room_5_body=room5_body()
room_6=room6()
room_6_puzzle=room6()
result=results()

if __name__ == "__main__":
    app.run(debug=True)

    