import requests
import streamlit as st
import requests
import json
import time
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from flask import Flask, request, jsonify, render_template
import pickle

# Set up the URL for the Flask app
URL = 'http://localhost:5000/predict'

# Define the Streamlit app
tab1, tab2 = st.tabs(['user entered data', 'live graph'])
with tab1:
    st.title('Temperature Predictor')

    # Get the user input for humidity and pressure
    humidity = st.slider('Humidity', min_value=0.0, max_value=100.0, value=50.0, step=1.0)
    pressure = st.slider('Pressure', min_value=0.0, max_value=200.0, value=100.0, step=1.0)

    # Make a POST request to the Flask app to get the predicted temperature
    payload = {'humidity': humidity, 'pressure': pressure}
    response = requests.post(URL, json=payload)

    # Display the predicted temperature to the user
    temperature = response.json()['temperature']
    st.write(f'Predicted temperature: {temperature:.2f} degrees Celsius')

with tab2:
    st.write('tab2')
    api_key = "60eb549ed8e17f9a8914a4ef2a98d1e4"
    city = "London"
    def get_live_weather():
        global city
        global api_key
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
        response = requests.get(url)
        data = json.loads(response.text)
        return data
    # Set the number of data points to collect and the time interval between data points
    n = 10
    # interval = 60

    # Collect live weather data and store in a pandas dataframe
    weather_data = pd.DataFrame(columns=["predicted temperature", 'pressure', 'humidity'])
    placeholder = st.empty()
    for i in range(n):
        with placeholder.container():
            data = get_live_weather()
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            temp = requests.post(URL, json={'humidity':humidity, 'pressure':pressure})
            res = temp.json()["temperature"]
            st.write(res)
            weather_data.loc[i] = [res, humidity, pressure]
            st.line_chart(weather_data)

        
        # time.sleep(interval)
    

