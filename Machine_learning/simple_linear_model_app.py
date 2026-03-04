import streamlit as st
import pickle
import numpy as np
model =pickle.load(open(r"C:\Users\USER\DataScience_NareshIt\Machine_learning\linear_regressor_model.pkl",'rb'))

year_exp=st.number_input('enter exp',min_value=0,max_value=50,value=1,step=0.5)

if st.button('predict'):
    e_in=np.array([[year_exp]])
    predict=model.predict(e_in)
    st.success(predict[0])