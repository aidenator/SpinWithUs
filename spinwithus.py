# Main python source code for spinwith.us
# Written by Aiden Hoopes, February 2017
# Co-opted for spinwith.us, October 2017

from flask import Flask, render_template
from words import *
from myhtml import *
from myutils import *
import random

app = Flask(__name__)

@app.route('/')
def index():
    if len(adj_list) == 0:
        adj = "test"
    else:
        adj = random.choice(adj_list)
    funnytext="DELETE ME"

    return render_template('index.html', funnytext=funnytext, adj=adj, header=header, footer=footer)

@app.route('/<name>/<adj>')
def name_adj(name, adj):
    return render_template('name_adj.html', name=name, adj=adj, header=header, footer=footer)

@app.route('/test')
def test_page():
    return render_template('test.html') 

@app.route('/nerd_stuff')
def uptime_page():
    mystring = ("{}<br>"
                "Current connections: <b>{}</b>").format(get_uptime(), get_connections())
    return render_template('generic.html', header=header, footer=footer, string=mystring) 

@app.route('/connect4')
def connect4():
    return render_template('connect4.html', header=header, footer=footer)

@app.route('/trump/<maga>')
def trump():
    return render_template('trump.html', header=header, footer=footer)

@app.errorhandler(500)
def internal_error(exception):
    return render_template("500.html", exception=exception, header=header, footer=footer), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
