from flask import Flask, render_template, request
import numpy as np
import pickle
import math

app = Flask(__name__)
model = pickle.load(open('taxi.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    # features = [int(x) for x in request.form.values()]
    var1 = request.values.get('Priceperweek')
    var2 = request.values.get('Population')
    var3 = request.values.get('Monthlyincome')
    var4 = request.values.get('Averageparkingpermonth')
    final_features = np.array([var1,var2,var3,var4]).reshape(1,4)
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text=math.floor(output))


if __name__ == '__main__':
    app.run(debug=True)