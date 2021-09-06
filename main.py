import streamlit as st
import extra_streamlit_components as stx
import pandas as pd
from sklearn.linear_model import LogisticRegression


@st.cache
def load_data(data_name):
    return pd.read_csv(data_name)

    # @st.cache
    # def train_model(features, labels):
    #     model = LogisticRegression()
    #     model.fit(features, labels)
    #     return model


cookie_manager = stx.CookieManager()


def get_cookie_if_not_none(cookie_name):
    try:
        value = cookie_manager.get(cookie_name)
    except AttributeError:
        value = 0
    return value


# data = load_data('train.csv')
# x_train = data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']]
# y_train = data['Survived']
# model = train_model(x_train, y_train)

pclass = get_cookie_if_not_none('pclass')
sex = get_cookie_if_not_none('sex')
age = get_cookie_if_not_none('age')
sib_sp = get_cookie_if_not_none('sibSp')
par_child = get_cookie_if_not_none('parch')

sexes = ['Female', 'Male']
pclasses = [1, 2, 3]

st.title('What would be your chances to survive on the Titanic?')
st.image('assets/background.jpg', use_column_width=True)

st.sidebar.subheader('Write Data')
age = st.sidebar.slider('Enter an age', min_value=0, max_value=100, step=1)
sex = st.sidebar.radio('Sex', options=sexes)
pclass = st.sidebar.selectbox('Select ticket class', options=pclasses, index=0)
siblings = st.sidebar.number_input('How many siblings would you take with you?', min_value=0, max_value=20,
                                   step=1)
with_loved = st.sidebar.radio('Would you take a husband/wife with you?', ['Yes', 'No'])
sib_sp = siblings + 1 if with_loved == 'Yes' else siblings
parents_answer = {'Yes': 2, 'Only mother': 1, 'Only father': 1, 'No': 0}
parents_answer_key = st.sidebar.radio('Would you take a parents with you?', parents_answer.keys())
parents = parents_answer[parents_answer_key]
children = st.sidebar.number_input('How many children would you take with you?', min_value=0, max_value=10,
                                   step=1)
par_child = parents + children

# test = pd.DataFrame({'Pclass': pclass,
#                      'Sex': sex,
#                      'Age': age,
#                      'SibSp': sib_sp,
#                      'Parch': par_child})
# test
# prediction = model.predict_proba(test)

cookie_manager.set('pclass', pclass, key=10)
cookie_manager.set('sex', sex, key=11)
cookie_manager.set('age', age, key=12)
cookie_manager.set('sibSp', sib_sp, key=13)
cookie_manager.set('parch', par_child, key=14)

st.sidebar.subheader('All Cookies:')
cookies = cookie_manager.get_all()
st.sidebar.write(cookies)
