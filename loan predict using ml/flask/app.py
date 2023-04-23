import numpy as np 
import pickle
import pandas
import os

from flask import Flask, request, render_template


app = Flask(__name__)
model = pickle.load(open(r'rdf.pkl', 'rb'))
scale = pickle.load(open(r'scale.pkl', 'rb'))



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=["POST", "GET"])
def predict():
    return render_template("prediction.html")

@app.route('/submit',methods=["POST", "GET"])
    
def submit():

    input_feature=[int(x) for x in request.form.values()]
    
    input_feature[np.array(input_feature)]
    print(input_feature)
    names = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']

    data = pandas.DataFrame(input_feature,columns=names)
    print(data)

    data_scaled = scale.fit_transform(data)
    data = pandas.DataFrame(data,columns=names)




    prediction=model.predict(data)

    print(prediction)
    prediction = int(prediction)
    print(type(prediction))
    
    if(prediction ==0):
        return render_template("prediction.html",result = "Loan will Not be Approved")
    else:
                return render_template("prediction.html",result = "Loan will be Approved")
if __name__=="__main__":

    app.run(debug=False)                

 