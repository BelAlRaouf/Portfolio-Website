import streamlit as st
import pandas

st.set_page_config(layout="wide")


st.header("My Portfolio")

content2 = "Here are my some projects that I have done.You can check them with thier links."
st.warning(content2)

col3, empty_col, col4 = st.columns([1.5, 0.6, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
