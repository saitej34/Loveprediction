import streamlit as st
import requests
import time
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
def get(a,b):
    x=st.info("Loading....")
    a=str(a)
    b=str(b)

    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"sname":a,"fname":b}

    headers = {
        'x-rapidapi-host': "love-calculator.p.rapidapi.com",
        'x-rapidapi-key': "721bd46ec5msh1895563b314a99cp14eeecjsn9260f8ff52a3"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    k=response.json()
    st.write("The Percentage of love or relationship is  {}".format(k["percentage"]))
    st.write("{}".format(k["result"]))
    st.info("Data fetched successfully")
st.title("Love Percentage Prediction Application")
a=st.text_input("Hey! Enter your Name : ")
b=st.text_input("Enter your Crush or the Lover name : ")
if st.button("Calculate the Love"):
    get(a,b)



