# Trigger rebuild

import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

import joblib

def load_model():
    model = joblib.load('model.pkl')  # Make sure the path is correct
    return model


# Streamlit app for prediction
st.title("Titanic Survival Prediction")
pclass = st.selectbox('Pclass', [1, 2, 3])
sex = st.selectbox('Sex', ['male', 'female'])
age = st.slider('Age', 1, 100)
fare = st.slider('Fare', 0, 500)
embarked = st.selectbox('Embarked', ['C', 'Q', 'S'])

if st.button('Predict'):
    sex_val = 1 if sex == 'female' else 0
    embarked_val = {"C": 0, "Q": 1, "S": 2}[embarked]
    input_data = pd.DataFrame({
        'Pclass': [pclass],
        'Sex': [sex_val],
        'Age': [age],
        'Fare': [fare],
        'Embarked': [embarked_val]
    })

    prediction = model.predict(input_data)
    st.write(f"Survived: {'Yes' if prediction == 1 else 'No'}")
