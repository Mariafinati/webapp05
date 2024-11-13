import streamlit as st
import requests
from io import BytesIO
import pandas as pd
urlCSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSE9-TpgudGYbsQtGsI6JNdusZYfCLZHNYvRbSd8NaT10h3-mosU-nhxrIi8gnnbU5v98v2my4hDQHd/pub?gid=883688627&single=true&output=csv"
rD = requests,get(urlCSV)
db = rD.content
st.write(db)
