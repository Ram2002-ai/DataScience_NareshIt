# import streamlit as st
# import pickle
# import numpy as np
# # load the saved model
# model =pickle.load(open(r"C:\Users\USER\DataScience_NareshIt\Machine_learning\linear_regressor_model.pkl",'rb'))

# # set the title of the streamlit app
# st.title('Salary Prediction App')

# # adding brief description
# st.write('This is the salary prediction app which build by the model called simple linear regression .', 
# 'The simple linear Regression accept only one input year of experiance and predict the salary')

# # add input widget for user to enter year of experiance
# year_experience=st.number_input('Enter the Experiance in years',min_value=0.0,max_value=50.0,value=1.0,step=0.5)

# # button & prediction model
# if st.button('Predict Salary'):
#     # make a prediction using the trained model
#     experience_input=np.array([[year_experience]]) # convert the input to a 2D for prediction 
#     prediction=model.predict(experience_input)

#     # Display the result
#     st.success(f'the predicted salary for {year_experience} years of experience is:${prediction[0]:,.2f}')

# # Display information about the model
# st.write('The model was trained using a dataset of salaries and years of experiance.')

# # -------------------this is my main code--------------------------


# for intrative User interface code is


import streamlit as st
import pickle
import numpy as np

# Page config
st.set_page_config(page_title="Salary Predictor", page_icon="💰", layout="centered")

# Load model
model = pickle.load(open(r"C:\Users\USER\DataScience_NareshIt\Machine_learning\linear_regressor_model.pkl",'rb'))

# Title
st.title("💰 Salary Prediction App")

st.write("This app predicts salary using Simple Linear Regression.")

# Sidebar input
st.sidebar.header("Input Details")
year_experience = st.sidebar.slider(
    "Select Years of Experience",
    min_value=0.0,
    max_value=50.0,
    value=1.0,
    step=0.5
)

import time

if st.button("Predict Salary",key='time'):
    with st.spinner("Predicting Salary..."):
        time.sleep(1)
        experience_input = np.array([[year_experience]])
        prediction = model.predict(experience_input)

    st.success("Prediction Completed!")
    st.metric("Predicted Salary", f"${prediction[0]:,.2f}")


st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    </style>
""", unsafe_allow_html=True)