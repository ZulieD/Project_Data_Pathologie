
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Sidebar ####
with st.sidebar:
    st.title('Auteur du projet :')
    st.write("")
    st.write("Julie DANIEL")
    st.write("21 ans ")
    st.write("Sexe féminin")
    st.write("")
    st.subheader('Comment me contacter :')
    st.write("")
    linkedin_url = "https://www.linkedin.com/in/julie-daniel-9003961b6/"
    st.markdown(f"[LinkedIn]( {linkedin_url} )")
    email_address = "julie.daniel@efrei.net"
    st.markdown(f"[Par e-mail](mailto:{email_address})")
    st.write("")
    st.subheader("Votre avis sur le projet :")
    color = st.select_slider(
        '',
        options=['médiocre', 'moyen', 'passable', 'correct', 'satisfaisant', 'excellent', 'remarquable'])
    st.write('Vous pensez que mon projet est ', color)
    
    ColorMinMax = st.markdown(''' <style> div.stSlider > div[data-baseweb = "slider"] > div[data-testid="stTickBar"] > div {
        background: rgb(99 1 1 / 0%); } </style>''', unsafe_allow_html = True)


    Slider_Cursor = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
        background-color: rgb(14, 38, 74); box-shadow: rgb(14 38 74 / 20%) 0px 0px 0px 0.2rem;} </style>''', unsafe_allow_html = True)

    
    Slider_Number = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div > div
                                { color: rgb(14, 38, 74); } </style>''', unsafe_allow_html = True)
    

    col = f''' <style> div.stSlider > div[data-baseweb = "slider"] > div > div {{
        background: linear-gradient(to right, rgb(1, 183, 158) 0%, 
                                rgb(99, 183, 195), 
                                rgba(99, 166, 195), 
                                rgba(14, 38, 74) 100%); }} </style>'''

    ColorSlider = st.markdown(col, unsafe_allow_html = True)
    
### Sidebar ###

### Introduction ###


st.title('Premier essais de site')


if st.checkbox('Show dataframe'):
    st.write("Tableau")

    
expander = st.expander("Explication")
expander.write("Explication des colonnes")

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.write('Plotting a matplotlib histogram with st.pyplot :')
st.pyplot(fig)

#st.dataframe
code_1 = '''
    df = pd.DataFrame(
                np.random.randn(10, 20),
                columns=('col %d' % i for i in range(20)))
    st.dataframe(df.style.highlight_max(axis=0))
    '''
st.code(code_1, language='python')
df = pd.DataFrame(
            np.random.randn(10, 20),
            columns=('col %d' % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))


col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

