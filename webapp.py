from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('mpg_kmpl.html')

@app.route("/pressure") #annotations tell which function goes with which request
def render_page1():
    return render_template('atm_torr.html')

@app.route("/volume")
def render_page2():
    return render_template('gal_lit.html')

if __name__=="__main__":
    app.run(debug=False)
