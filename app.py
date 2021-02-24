import streamlit as st

import pandas as pd
import plotly.express as px

df= pd.read_csv(r"C:/Users/Abhinav/Desktop/lol.csv")
df['count'] = 1
st.title("First App")

if(st.button('View Dataframe')):
  st.write(df)

st.text('This is my first app.')

#st.text('Fixed width text')
#st.markdown('_Markdown_') # see *
#st.latex(r''' e^{i\pi} + 1 = 0 ''')
#st.write('Most objects') # df, err, func, keras!
#st.write(['st', 'is <', 3]) # see *
#st.title('My title')
#st.header('My header')
#st.subheader('My sub')
#st.code('for i in range(8): foo()')

#st.table(df)


#a = st.button('Hit me')
#st.checkbox('Check me out')
#b = st.radio('Radio', [1,2,3])
#st.write(b)
#st.selectbox('Select', [1,2,3])
#st.multiselect('Multiselect', [1,2,3])
#c=st.slider('Slide me', min_value=0, max_value=70)

#st.select_slider('Slide to select', options=[1,'2'])
#st.text_input('Enter some text')
#st.number_input('Enter a number')
#st.text_area('Area for textual entry')
#st.date_input('Date input')
#st.time_input('Time entry')
#st.file_uploader('File uploader')
#st.color_picker('Pick a color')


if(st.button('Show Gender Ratio Chart')):
   fig = px.pie(df, values='count', names='Sex')
   st.plotly_chart(fig, use_container_width=True)