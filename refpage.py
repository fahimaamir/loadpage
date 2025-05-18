import streamlit as st
from streamlit_js_eval import streamlit_js_eval

st.header("Testing =======")

if st.button("Reload page"):
    streamlit_js_eval(js_expressions="parent.window.location.reload()")