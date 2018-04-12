from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'davids_assignment'  

@app.route('/')
def index():
    if 'random_num' not in session:
        import random
        session['random_num'] = random.randrange(0, 101) 
    return render_template("index.html", random=session['random_num'])

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = request.form['guess']
    if int(session['random_num']) == int(request.form['guess']):
        session['response'] = "You GOT IT!"
        return render_template('index.html', random=session['random_num'], guess=request.form['guess'], response=session['response'])
        return redirect ('/win')
    elif int(session['random_num']) > int(request.form['guess']):
        session['response'] = "too low"
        return render_template('index.html', random=session['random_num'], guess=request.form['guess'], response=session['response'])
        return redirect ('/')
    elif int(session['random_num']) < int(request.form['guess']):
        session['response'] = "too high"
        return render_template('index.html', random=session['random_num'], guess=request.form['guess'], response=session['response'])
        return redirect ('/')
    else:
        return render_template('index.html', random=session['random_num'], guess=request.form['guess'], response=session['response'])
        return redirect ('/')

@app.route('/win')
def win():
    print 'you Win!!!'
    # //change display to you win! 
    return redirect('/reset')
    
@app.route('/reset')
def reset():
    session.pop('random_num')
    return redirect('/')

# @app.route('/check')
# def check():
#     if //checked number(from their input we store in session) = session['random_num]
#         return redirect ('/win')
#     else:
#         return redirect ('/')
app.run(debug=True)