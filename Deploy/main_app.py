from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('customer_clustering', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/getresult', methods=['POST'])
def getresult():
    cost = [float(x) for x in request.form.values()]
    prediction = model.predict([cost])
    if(prediction[0] == 0):
        result = "Small Business/Private"
        return render_template('index.html', output ='You are in the : {} group'.format(result))
    elif(prediction[0] == 1):
        result = "Business"
        return render_template('index.html', output ='You are in the : {} group'.format(result))
    else:
        result = "Big Business"
        return render_template('index.html', output ='You are in the : {} group'.format(result))

if __name__ == "__main__":
    app.run(debug=True)