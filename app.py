import streamlit
streamlit.title("My Parent new healthy diner")
streamlit.header("Breakfast Menu")
streamlit.text("Banana, Milk, Eggs")
streamlit.text("Omega-3 Fatty")

streamlit.header("Build your own Fruit Smoothie")

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

## set index to fruits
my_fruit_list = my_fruit_list.set_index('Fruit')

## create a multiselect wizard.
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
streamlit.dataframe(my_fruit_list)
