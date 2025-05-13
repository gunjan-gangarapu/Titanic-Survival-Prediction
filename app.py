import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load pre-trained model
def load_model():
    model = joblib.load('model.pkl')  # Ensure this path is correct
    return model

# Function to make prediction
def predict_survival(pclass, sex, age, fare, embarked):
    # Create a DataFrame with user input
    input_data = pd.DataFrame({
        'Pclass': [pclass],
        'Sex': [sex],
        'Age': [age],
        'Fare': [fare],
        'Embarked': [embarked]
    })

    # Preprocess data: label encoding for 'Sex' and 'Embarked'
    le_sex = LabelEncoder()
    le_sex.fit(['male', 'female'])
    input_data['Sex'] = le_sex.transform(input_data['Sex'])

    le_embarked = LabelEncoder()
    le_embarked.fit(['C', 'Q', 'S'])
    input_data['Embarked'] = le_embarked.transform(input_data['Embarked'])

    # Load model
    model = load_model()

    # Make a prediction
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit UI
st.title("🚢 Titanic Survival Predictor")
st.write("Enter passenger details to predict survival probability.")

# Input fields
pclass = st.selectbox("Pclass", [1, 2, 3])
sex = st.radio("Sex", ["male", "female"])
age = st.number_input("Age", min_value=0, max_value=100)
fare = st.number_input("Fare", min_value=0)
embarked = st.selectbox("Embarked", ['C', 'Q', 'S'])

# Prediction button
if st.button('Predict'):
    survival = predict_survival(pclass, sex, age, fare, embarked)
    if survival == 1:
        st.success("The passenger would have survived.")
    else:
        st.error("The passenger would not have survived.")
