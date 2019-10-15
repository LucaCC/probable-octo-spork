from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_fuel_economy():
    mpg = request.args['fuel_economy']
    kmpl = mpg * .425144
    return render_template('mpg_kmpl.html', responseFromServer = kmpl)

@app.route("/pressure") #annotations tell which function goes with which request
def render_pressure():
    atmosphere = request.args['pressure']
    torr = atmosphere * 760
    return render_template('atm_torr.html', responseFromServer = torr)

@app.route("/volume")
def render_volume():
    gallon = request.args['volume']
    liter = gallon * 3.78541
    return render_template('gal_lit.html', responseFromServer = liter)

if __name__=="__main__":
    app.run(debug=False)
