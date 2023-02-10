import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Belal Raouf")
    st.subheader("Software Developer", )
    content = """
    Dedicated and performance-driven Software Engineer with a pro-active approach and determination to successfully finish all assigned projects with budget and schedule.
    Effective team player offering extraordinary analytical skills and the important ability to think critically. 
    With a keen interest in coding.
    """
    st.info(content)

content2 = "Here are my some projects that I have done.You can check them with thier links."
st.warning(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])