from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the pre-trained machine learning model
model = joblib.load('my_model.pkl')

@app.route('/predict', methods=['POST'])
def predict_temperature():
    # Get the humidity and pressure values from the request
    humidity = request.json['humidity']
    pressure = request.json['pressure']

    # Make a prediction using the pre-trained model
    temperature = model.predict([[humidity, pressure]])

    # Return the predicted temperature as a JSON response
    return jsonify({'temperature': temperature[0]})

if __name__ == '__main__':
    app.run(debug=True)