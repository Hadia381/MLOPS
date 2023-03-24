**<h1>README for Temperature Predictor App</h1>**

**Overview**
This code is a Streamlit app that predicts the temperature based on user-inputted humidity and pressure values using a linear regression model. It also collects live weather data for a specified city and displays it in a line chart.

**Prerequisites**
The app requires the following Python packages to be installed:
requests
streamlit
pandas
sklearn
flask

**Installation**
Clone the repository to your local machine
Install the required packages using pip install -r requirements.txt
Start the app using streamlit run app.py

**Usage**
The app consists of two tabs, "user entered data" and "live graph".
In the "user entered data" tab, the user can input the humidity and pressure values and receive a predicted temperature value in degrees Celsius.
In the "live graph" tab, the app collects live weather data for a specified city (default is London) and displays it in a line chart. The chart shows the predicted temperature, pressure, and humidity for the previous 10 data points.

**Notes**
The linear regression model was trained on a dataset containing temperature, humidity, and pressure values. It may not be accurate for all locations and weather conditions.
The live weather data is collected from the OpenWeatherMap API using an API key. If you wish to use a different API or city, you will need to modify the code accordingly.
The app is currently set up to make requests to a Flask app running locally on port 5000. If you wish to use a different endpoint, you will need to modify the URL variable at the top of the code.

