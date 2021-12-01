from flask import Flask, request,render_template
import pickle
import numpy as np
import sklearn

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Cancer')
def cancer():
    return render_template('cancer.html')

@app.route('/prdict', methods=['POST'])
def predict():
    model = pickle.load(open("./breast_cancer_pred.pickle", 'rb'))
    features = [x for x in request.form.values()]
    np_array = np.asarray(features)
    reshaped_array = np_array.reshape(1,-1)

    prediction = model.predict(reshaped_array)
    if prediction>0:
        pred_text = "Cancer Positive"
    else:
        pred_text = "Cancer Negative"

    return render_template('cancer.html', prediction_text=pred_text)

@app.route('/Heart')
def heart():
    return render_template('heart.html')

@app.route('/heart_pred', methods=['POST'])
def predict_heart():
    model = pickle.load(open("./heart_disease_pred.pickle", 'rb'))
    features = [x for x in request.form.values()]
    np_array = np.asarray(features)
    reshaped_array = np_array.reshape(1,-1)

    prediction = model.predict(reshaped_array)
    if prediction>0:
        pred_text = "Heart Disease Positive"
    else:
        pred_text = "Heart Disease Negative"

    return render_template('heart.html', prediction_text=pred_text)

@app.route('/Diabetes')
def diabetes():
    return render_template('diabetes.html')

@app.route('/diabetes_pred', methods=['POST'])
def predict_diabetes():
    model = pickle.load(open("./diabetes_pred.pickle", 'rb'))
    features = [x for x in request.form.values()]
    np_array = np.asarray(features)
    reshaped_array = np_array.reshape(1,-1)

    prediction = model.predict(reshaped_array)
    if prediction>0:
        pred_text = "Diabetes Positive"
    else:
        pred_text = "Diabetes Negative"

    return render_template('diabetes.html', prediction_text=pred_text)



if __name__ == "__main__":
    print("Starting Flask Server")
    app.run(debug=True)