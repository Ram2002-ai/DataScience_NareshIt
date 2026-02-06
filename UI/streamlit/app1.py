import streamlit as st

st.title('welcome to first app')

st.write('this app calculate the square of a number')

st.header('select a number')

number=st.slider('pick a number',0,100,5) # min max ,default

st.subheader('Result')

squared_number=number*number

st.write(f'the square of {number} is ** {squared_number}')