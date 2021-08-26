import streamlit as st
import extra_streamlit_components as stx
import pandas as pd
from PIL import Image


@st.cache
def load_data(data_name):
    df = pd.read_csv(data_name)
    return df


cookie_manager = stx.CookieManager()
data = load_data('train.csv')
background = Image.open('assets/background.jpg')

st.title('What would be your chances to survive on the Titanic?')
st.image(background, use_column_width=True)
data

st.sidebar.subheader('Write Data')
age = st.sidebar.number_input('Enter an age', min_value=0, max_value=100, step=1, value=int(cookie_manager.get('age')))
sex = st.sidebar.radio('Sex', options=['Female', 'Male', 'waiting till marriage'])
pclass = st.sidebar.selectbox('Select ticket class', [1, 2, 3])
sib_sp = st.sidebar.number_input('How many siblings do you have?', min_value=0, max_value=20, step=1)
married = st.sidebar.radio('Are you married', ['Yes', 'No'])
sib_sp += 1 if married == 'Yes' else 0

clicked = st.button('CHECK OUT')
if clicked:
    cookie_manager.set('age', age)

st.sidebar.subheader('All Cookies:')
cookies = cookie_manager.get_all()
st.sidebar.write(cookies)
