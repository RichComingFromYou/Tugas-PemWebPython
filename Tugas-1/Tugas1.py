import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

st.title("Tugas 1")

#Line_Chart
st.subheader ("Line-Chart CSGO Player & Twitch Viewer Count 2022")
df = pd.DataFrame({"Month": ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Des'], 
                   "Player": [906966, 989793, 993808, 1016762, 875790, 906968, 881284, 1039889, 1062931, 1090858, 1132952, 1001231], 
                   "Twitch Viewer": [153256, 368535, 353011, 374474, 1647563, 519694, 1162600, 179830, 349588, 237433, 1324828, 280823]})

st.table(df)

st.header("Line Chart")
chart_data = pd.DataFrame({"Player": [906966, 989793, 993808, 1016762, 875790, 906968, 881284, 1039889, 1062931, 1090858, 1132952, 1001231], 
                           "Twitch Viewer": [153256, 368535, 353011, 374474, 1647563, 519694, 1162600, 179830, 349588, 237433, 1324828, 280823]})
st.line_chart(chart_data,)

st.subheader ("Bar-Chart CSGO Player & Twitch Viewer Count 2022")
st.bar_chart(chart_data)

#Altair_Chart
df = pd.DataFrame({"Player": [906966, 989793, 993808, 1016762, 875790, 906968, 881284, 1039889, 1062931, 1090858, 1132952, 1001231], 
                   "Twitch Viewer": [153256, 368535, 353011, 374474, 1647563, 519694, 1162600, 179830, 349588, 237433, 1324828, 280823]})
# generate a date range to be used as the x axis
df['date'] =  pd.date_range("2022-01-01", periods=12, freq="m")
df_melted = pd.melt(df,id_vars=['date'],var_name='parameter', value_name='value')
c = alt.Chart(df_melted, title='Altair-Chart CSGO Player & Twitch Viewer Count 2022').mark_line().encode(
     x='date', y='value', color='parameter')

st.altair_chart(c, use_container_width=True)

