🚢 Titanic Survival Prediction
📌 Project Overview
This project predicts whether a passenger on the Titanic would have survived or not based on features such as passenger class, age, sex, fare, and embarkation point. The model is built using Random Forest Classifier, and the app is deployed using Streamlit.

🧰 Tech Stack
Programming Language: Python

Libraries:

Scikit-learn (machine learning)

Pandas (data handling)

Streamlit (web app interface)

Joblib (model serialization)

Deployment: Streamlit Cloud

📊 Dataset
This project uses the Titanic dataset from Kaggle. Key features include:

Passenger Class (Pclass)

Sex

Age

Fare

Embarked (C, Q, S)

🧠 Model
A Random Forest Classifier is trained on the dataset to predict survival probability based on passenger features.

🧪 Features for Prediction
Pclass: Passenger class (1, 2, or 3)

Sex: Male or Female

Age: Age of the passenger

Fare: Ticket fare

Embarked: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)

⚙️ Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Titanic-Survival-Prediction.git
   cd Titanic-Survival-Prediction
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run app.py
   
4. Open your browser and visit the provided local address (usually http://localhost:8501) to interact with the app.
   

🚀 Usage
1. Fill out the form with:

Pclass: 1, 2, or 3

Sex: Male or Female

Age: e.g., 28

Fare: e.g., 72.50

Embarked: C, Q, or S

Click Predict to view the result.

✅ Prediction Result
The app will display one of the following:

🟢 "The passenger would have survived."

🔴 "The passenger would not have survived."

🤝 Contributing
Feel free to fork this repository and submit pull requests with improvements or new features!

📄 License
This project is licensed under the MIT License.
