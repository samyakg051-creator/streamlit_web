import streamlit as st
import pandas as pd
import numpy as np

st.title("my first streamlit app")
st.write("hello samyak jiiii")
st.text("lets start")
name = st.text_input("enter name")
if st.button("Greet"):
 st.success(f"hello,{name}!")
df= pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
st.line_chart(df)
st.bar_chart(df)
st.sidebar.title("navigation")
st.image("image.png",caption="sample image")
st.video("https://www.youtube.com/watch?v=85X1_7DIKcA")
st.header("this is header")
st.subheader("this is subheader")
st.markdown("**bold**,**italic**,'code',[Link](https://streamlit.in)")
st.code("for i in range(5):print(i)",language="python")
st.text_input("what is your name?")
st.text_area("Write something...")
st.number_input("Pick a number",min_value=0,max_value=100)
st.slider("Choose a range",0,100)
st.selectbox("Select a fruit",["Apple","Banana","Mango"])
st.multiselect("Choose toppings",["Cheese","Tomato","Olives"])
st.radio("Pick one",["Option A","Option"])
st.checkbox("I agree to the terms")
if st.checkbox("show details"):
 st.info("here are more details....")
 option = st.radio("choose view", ["show chart","show table"])
 if option == "show chart":
  st.write("chart would appear here")
else:
 st.write("table would appear here")