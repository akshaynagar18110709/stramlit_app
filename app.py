import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

streamlit.title("View Our Fruit List : Add Your Favorites!")
streamlit.header("Breakfast Menu")
streamlit.text("Banana, Milk, Eggs")
streamlit.text("Omega-3 Fatty")

streamlit.header("Build your own Fruit Smoothie")

# import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

## set index to fruits
my_fruit_list = my_fruit_list.set_index('Fruit')

## create a multiselect wizard.
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
def get_fruit_info(fruit):
  fruit_choice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  return pandas.json_normalize(fruit_choice_response.json())
    
streamlit.header("FruityVice Fruit Advice !")
try:
  # enter a fruit choice and display its information.
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("please enter a fruit to get information")
  else:
    streamlit.dataframe(get_fruit_info(fruit_choice))
except URLError as e:
  streamlit.error()

# import snowflake.connector

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

if streamlit.button("Get Fruit List"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)

def insert_fruit_in_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    query = f"insert into fruit_load_list values ('{new_fruit}')"
    my_cur.execute(query)
    return "Thanks for adding new fruit : " + new_fruit

add_fruit_to_list = streamlit.text_input("What fruit would you like to add ?")
if streamlit.button("Add Fruit to List"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  streamlit.text(insert_fruit_in_snowflake(add_fruit_to_list))
  my_cnx.close()
streamlit.stop()


my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The fruit load list contains")
streamlit.dataframe(my_data_row)

select_new_fruits = streamlit.text_input("What fruit would you like to add ?")
streamlit.text("Thanks for adding " + select_new_fruits)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
