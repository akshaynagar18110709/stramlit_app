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
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header("FruityVice Fruit Advice !")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
