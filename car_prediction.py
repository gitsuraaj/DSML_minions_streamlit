import streamlit as st
import pickle


st.header("Car Prediction Application")


col1, col2= st.columns(2)

with col1:
    fuel= col1.selectbox(
    'Select Fuel Type',
    ('Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'))

with col2:
    transmission= col2.selectbox(
    'Select Transmission',
    ('Manual','Automatic'))

col1, col2= st.columns(2)

with col1:
    engine = col1.slider('Select Engine Power', 500, 5000, step=100)

with col2:
    seats= st.selectbox(
    'Select the no. of seats',
   [4,5,6,7,8,9])


encoding_dict= {

    "fuel": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric':5},
    "transmission": {"Manual":1, "Automatic":2}

}

def model_pred (fuel, transmission, engine, seats ):
    with open ("car_pred", "rb") as file:
        model=pickle.load(file)

    input_values=[[2012.0, 1 , 120000 , fuel , transmission, 19.7, engine,46.3, seats]]

    return model.predict (input_values)


if st.button('Predict Car Price'):
    fuel = encoding_dict['fuel'][fuel]
    transmission=encoding_dict['transmission'][transmission]
    price= model_pred(fuel, transmission, engine, seats )

    st.text(f"Predicted price is: {price}")