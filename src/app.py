from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('home')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/trabalhos')
def trabalhos():
    return render_template('trabalhos.html')