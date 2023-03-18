import pandas as pd
import numpy as np
import streamlit as st

st.title("Tugas 2")

st.subheader("Latihan 1")

# Chart
st.subheader("Chart")
st.subheader ("Line-Chart CSGO Player & Twitch Viewer Count 2022")
chart_data = pd.DataFrame({"Player": [906966, 989793, 993808, 1016762, 875790, 906968, 881284, 1039889, 1062931, 1090858, 1132952, 1001231], 
                           "Twitch Viewer": [153256, 368535, 353011, 374474, 1647563, 519694, 1162600, 179830, 349588, 237433, 1324828, 280823]})
st.line_chart(chart_data,)

# Widget
st.subheader("Widget")
st.subheader ("Select Box CSGO Player & Twitch Viewer Count 2022")
option = st.selectbox(
    'Select the Chart that you wanted to see?',
    ('Player', 'Twitch Viewer'))

st.write('You selected:', option)

if option == 'Player':
    chart_data = pd.DataFrame({"Player": [906966, 989793, 993808, 1016762, 875790, 906968, 881284, 1039889, 1062931, 1090858, 1132952, 1001231]})
    st.line_chart(chart_data)
else:
    chart_data = pd.DataFrame({"Twitch Viewer": [153256, 368535, 353011, 374474, 1647563, 519694, 1162600, 179830, 349588, 237433, 1324828, 280823]})
    st.line_chart(chart_data)

# Layout
st.subheader("Layout")
st.subheader ("Layout CSGO Player Count 2022")
col1, col2 = st.columns([3, 1])
data = pd.DataFrame({"Player": [906966, 989793, 993808, 1016762, 875790, 906968, 881284, 1039889, 1062931, 1090858, 1132952, 1001231]})

col1.subheader("Wide column with CSGO Player count data")
col1.line_chart(data)

col2.subheader("Narrow column with CSGO Player count data")
col2.table(data)