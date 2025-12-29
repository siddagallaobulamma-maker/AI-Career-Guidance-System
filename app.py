import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Title
st.title("AI-Based Career Guidance System")
st.write("Enter your skills to get a career recommendation")

# Load dataset
data = pd.read_csv("career_data.csv")

X = data.drop("Career", axis=1)
y = data["Career"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# User Inputs
math = st.slider("Math Skills", 1, 10, 5)
programming = st.slider("Programming Skills", 1, 10, 5)
creativity = st.slider("Creativity", 1, 10, 5)
communication = st.slider("Communication Skills", 1, 10, 5)
marks = st.slider("Marks (%)", 40, 100, 70)

# Predict button
if st.button("Recommend Career"):
    input_data = pd.DataFrame(
        [[math, programming, creativity, communication, marks]],
        columns=["Math", "Programming", "Creativity", "Communication", "Marks"]
    )

    prediction = model.predict(input_data)
    st.success(f"Recommended Career: {prediction[0]}")
