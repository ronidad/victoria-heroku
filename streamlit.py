import streamlit as st
import pandas as pd
import plotly.express as px




crops=pd.read_csv("df_crops.csv").set_index("Produce_Variety")


selected_status = st.sidebar.selectbox(
    "Select Data to view",
    options=[
        "Average Prices Chart",
        "Average Prices Table",
    ],
)

if selected_status=="Average Prices Chart":
    st.title("Average Prices chart")
    st.subheader("subhead average prices")
    st.bar_chart(crops)
if selected_status=="Average Prices Table":
    st.title("Average Prices Table")
    st.subheader("subhead average prices")
    st.table(crops)

