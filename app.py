from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

app = Flask(__name__, template_folder='templates')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods = ["GET",'POST'])
def predict():
    if request.method == 'GET':
        return render_template('credit_model.html')

    if request.method == 'POST':
        try:
            int_features = [[float(x) for x in request.form.values()]]
            if model.predict(np.array(int_features))[0] == 0:
                prediction = "Good Customer for Bank"
            else:
                prediction = "Not a good Customer for Bank"
        except:
            prediction = "Invalid Data"

        return render_template('credit_model.html', prediction_text=prediction)
    
app.run()
