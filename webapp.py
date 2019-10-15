from flask import Flask, url_for, render_template, request

app = Flask(__name__)
responseFromServer = 0

@app.route("/")
def render_fuel_economy():
    if('fuel_economy' in request.args):
        mpg = float(request.args['fuel_economy'])
        kmpl = mpg * .425144
        return render_template('mpg_kmpl.html', responseFromServer = kmpl)
    else:
        return render_template('mpg_kmpl.html')

@app.route("/pressure") #annotations tell which function goes with which request
def render_pressure():
    if('pressure' in request.args):
        atmosphere = float(request.args['pressure'])
        torr = atmosphere * 760
        return render_template('atm_torr.html', responseFromServer = torr)
    else:
        return render_template('atm_torr.html')

@app.route("/volume")
def render_volume():
    if('volume' in request.args):
        gallon = float(request.args['volume'])
        liter = gallon * 3.78541
        return render_template('gal_lit.html', responseFromServer = liter)
    else:
        return render_template('gal_lit.html')

if __name__=="__main__":
    app.run(debug=False)
