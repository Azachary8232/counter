from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "skittles"



@app.route('/')
def hello():
    if 'count' in session:
        session['count'] = session['count'] +1
    else:
        session['count'] = 0
    if 'count2' in session:
        session['count2'] = session['count2'] +1
    else:
        session['count2'] = 0
    return render_template("index.html")

@app.route('/add')
def add_count():
    session['count'] = session['count'] + 1
    session['count2'] = session['count2'] + 1
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.pop('count')
    return redirect("/",)

@app.route('/user_add', methods = ["POST"])
def user_input():
    session['count'] += int(request.form['input']) - 1
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)