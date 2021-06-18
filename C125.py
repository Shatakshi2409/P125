from flask import Flask, jsonify, request
from Classifier import getPred

app=Flask(__name__)
@app.route('/predict',methods=['POST'])
def predict_data():
    image=request.files.get('digit')
    prediction=getPred(image)
    return jsonify({
        'prediction':prediction
    }), 200

if (__name__=='__main__'):
    app.run(debug=True)