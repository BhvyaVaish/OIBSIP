from flask import Flask, render_template, request
import pickle
import numpy as np 
app = Flask(__name__)
model = pickle.load(open('car_price_model.pkl', 'rb'))
@app.route('/')
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    present_price = float(request.form['present_price'])
    driven_kms = int(request.form['driven_kms'])
    owner = int(request.form['owner'])

    fuel_type = request.form['fuel_type']
    seller_type = request.form['seller_type']
    transmission = request.form['transmission']

    fuel_diesel = 1 if fuel_type == "Diesel" else 0
    fuel_petrol = 1 if fuel_type == "Petrol" else 0

    selling_individual = 1 if seller_type == "Individual" else 0

    transmission_manual = 1 if transmission == "Manual" else 0

    sample = [[
        present_price,
        driven_kms,
        owner,
        fuel_diesel,
        fuel_petrol,
        selling_individual,
        transmission_manual
    ]]

    prediction = model.predict(sample)[0]

    return render_template(
        "result.html",
        prediction=round(prediction,2),
        present_price=present_price,
        driven_kms=driven_kms,
        owner=owner,
        fuel_type=fuel_type,
        seller_type=seller_type,
        transmission=transmission
    )
if __name__ == '__main__':
    app.run(debug=True)