import streamlit as st
import requests

st.title("Iris Flower Classifier")

sl = st.slider("Sepal length", 4.0, 8.0, 5.1)
sw = st.slider("Sepal width", 2.0, 4.5, 3.5)
pl = st.slider("Petal length", 1.0, 7.0, 1.4)
pw = st.slider("Petal length", 0.1, 2.5, 0.2)

if st.button("Predict"):
    res = requests.post("https://iris-api-nth4.onrender.com/predict",
                        json={"sepal_length": sl, "sepal_width": sw,
                              "petal_length":pl, "petal_width":pw})
    st.success(f"Prediction: {res.json()['prediction']}")