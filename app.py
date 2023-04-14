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

# tak the json version and normalize it to pandas dataframe.
normalized_dataframe = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(normalized_dataframe)

# enter a fruit choice and display its information.
fruit_choice = streamlit.text_input('What fruit would you like information about?')
fruit_choice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
streamlit.text("Information abount " + fruit_choice)
streamlit.dataframe(pandas.json_normalize(fruit_choice_response.json()))

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The fruit load list contains")
streamlit.dataframe(my_data_row)

select_new_fruits = streamlit.text_input("What fruit would you like to add ?")
streamlit.text("Thanks for adding " + select_new_fruits)
