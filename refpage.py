import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from st_aggrid import AgGrid
import pandas as pd

st.header("Testing =======")
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(df, editable = True)




if st.button("Reload page"):
    streamlit_js_eval(js_expressions="parent.window.location.reload()")
    