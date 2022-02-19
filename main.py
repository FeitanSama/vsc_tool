import pandas as pd
import streamlit as st

st.title("Visual Scraper Tool")

url = st.text_input("URL")

if url != "":
    st.info(url)