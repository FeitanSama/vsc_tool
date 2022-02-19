# PRE PROS
import pandas as pd

# WEB 
import streamlit as st

# SCRAP
from bs4 import BeautifulSoup
import requests
import selenium

st.title("Visual Scraper Tool")

url = st.text_input("URL")

if url != "":
    result = requests.get(url)
    st.info(result.text)