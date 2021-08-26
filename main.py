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

st.sidebar.subheader('Write Data')
age = st.sidebar.slider('Enter an age', min_value=0, max_value=100, step=1,
                        value=int(cookie_manager.get('age') if cookie_manager.get('age') else 0))
sex = st.sidebar.radio('Sex', options=['Female', 'Male', 'waiting till marriage'])
pclasses = {'Upper': 1, 'Middle': 2, 'Lower': 3}
pclass_key = st.sidebar.selectbox('Select ticket class', pclasses.keys())
pclass = pclasses[pclass_key]
sib_sp = st.sidebar.number_input('How many siblings would you take with you?', min_value=0, max_value=20,
                                 step=1)
with_loved = st.sidebar.radio('Would you take a husband/wife with you?', ['Yes', 'No'])
sib_sp += 1 if with_loved == 'Yes' else 0
parents_answer = {'Yes': 2, 'Only mother': 1, 'Only father': 1, 'No': 0}
parents_answer_key = st.sidebar.radio('Would you take a parents with you?', parents_answer.keys())
parents = parents_answer[parents_answer_key]
children = st.sidebar.number_input('How many children would you take with you?', min_value=0, max_value=10,
                                   step=1)
parchar = parents + children

cookie_manager.set('age', age, key=11)
cookie_manager.set('sex', sex, key=12)
cookie_manager.set('pclass', pclass, key=13)
cookie_manager.set('sib_sp', sib_sp, key=14)

st.sidebar.subheader('All Cookies:')
cookies = cookie_manager.get_all()
st.sidebar.write(cookies)
