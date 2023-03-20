import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# Write and magic
st.subheader (':green[Write]')
st.write('Hello, *World!* :sunny:')

st.subheader (':green[Magic]')
df = pd.DataFrame({'col1': [1,2,3]})
df  

x = 10
'x', x  #

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig 

# Text Element
st.title (':green[Text Element]')
# markdown
st.subheader (':green[Markdown]')
st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :star2:")

# Title
st.subheader (':green[Title]')
st.title('This is a title')
st.title('A title with _italics_ :blue[colors] and emojis :sun_with_face:')

# Header
st.subheader (':green[Header]')
st.header('This is a header')
st.header('A header with _italics_ :blue[colors] and emojis :sun_with_face:')

# SubHeader
st.subheader (':green[SubHeader]')
st.subheader('This is a subheader')
st.subheader('A subheader with _italics_ :blue[colors] and emojis :sun_with_face:')

#Caption
st.subheader (':green[Caption]')
st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sun_with_face:')

# Code
st.subheader (':green[Code]')
code = '''def hello():
    print("Hello, World!")'''
st.code(code, language='python')

# Text 
st.text('This is some text.')

# Latex
st.subheader (':green[Latex]')
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# Data Display Element
st.title (':green[Data Display Element]')
# DataFrame
st.subheader (':green[DataFrame]')
df = pd.DataFrame({"Month": ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Des'], 
                   "Player": [906966, 989793, 993808, 1016762, 875790, 906968, 881284, 1039889, 1062931, 1090858, 1132952, 1001231], 
                   "Twitch Viewer": [153256, 368535, 353011, 374474, 1647563, 519694, 1162600, 179830, 349588, 237433, 1324828, 280823]})

st.dataframe(df)  

# Table
st.title (':green[Table]')
st.subheader (':green[Table]')
st.table(df)

# Metric
st.subheader (':green[Metric]')
st.metric(label="Temperature", value="69 °C", delta="-1.2 °C", delta_color='normal')

# Json
st.subheader (':green[Json]')
st.json({
    'SHOTGUN': ['Nova', 'XM1014', 'Mag-7', 'Sawed-Off'],
    'SUBMACHINE GUN': ['MAC-10', 'MP9', 'MP7', 'MP5-SD', 'UMP-45', 'P90', 'PP-Bizon'],
    'RIFLE': ['Galil AR', 'FAMAS', 'AK-47', 'M4A4', 'M4A1-S', 'SSG 08', 'SG 553', 'AUG', 'AWP', 'G3SG1','SCAR-20'],
})

# Chart Element
st.title (':green[Chart Element]')
chart_data = pd.DataFrame({"Player": [906966, 989793, 993808, 1016762, 875790, 906968, 881284, 1039889, 1062931, 1090858, 1132952, 1001231], 
                           "Twitch Viewer": [153256, 368535, 353011, 374474, 1647563, 519694, 1162600, 179830, 349588, 237433, 1324828, 280823]})

st.subheader(':green[Line Chart]')
st.line_chart(chart_data)

st.subheader(':green[Area Chart]')
st.area_chart(chart_data)

st.subheader(':green[Bar Chart]')
st.bar_chart(chart_data)


# Input Widget
st.title (':green[Input Widget]')
st.subheader (':green[Button]')
if st.button('Press me'):
    st.write('you pressed me')
else:
    st.write('You didnt pressed me')

st.subheader (':green[Checkbox]')
agree = st.checkbox('Did you pressed the button')

if agree:
    st.write('Thats Great')

# Media Element
st.title ('green[Media Element]')
st.subheader (':green[Video]')
st.video("https://youtu.be/ZOnQohTePwo")

# Layout and Container
st.title (':green[Layout and Container]')
st.subheader (':green[Column]')
st.subheader("Layout")
st.subheader ("Layout CSGO Player Count 2022")
col1, col2 = st.columns([3, 1])
data = pd.DataFrame({"Player": [906966, 989793, 993808, 1016762, 875790, 906968, 881284, 1039889, 1062931, 1090858, 1132952, 1001231]})

col1.subheader("Wide column with CSGO Player count data")
col1.line_chart(data)

col2.subheader("Narrow column with CSGO Player count data")
col2.table(data)

# Status Element
st.title (':green[Status Element]')
st.subheader (':green[Progress]')
progress_text = "Loading..."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)

st.subheader (':green[Spinner]')
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Access Given!')

# Control Flow
st.title (':green[Control Flow]')
st.subheader (':green[Form]')
with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

# Utilities
st.title (':green[Utilities]')
st.subheader (':green[Echo]')
with st.echo():
    st.write('This will print the code that is written inside "st.echo():" ')