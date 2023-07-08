import streamlit 
streamlit.title('My parents new healthy dinner')

streamlit.header('Breakfast meanu')
streamlit.text('🥣 Omega 3  & Blueberry oatmeal')
streamlit.text('🥗klae, spinach and rocket smoothie ')
streamlit.text('🐔har-boiled free-range eggs')
streamlit.text('🥑🍞 avacado toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list=pandas.read_csv(' https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])

streamlit.dataframe(my_fruit_list)
