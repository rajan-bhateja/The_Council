import streamlit as st
from agents import workflow
import json

st.title("The Council")
st.caption("Powered by OpenAI and Swarms")

st.set_page_config(layout="wide", page_title="The Council")

home_tab, overview_tab, pros_cons_tab, practical_tab, expert_tab = st.tabs(["Home", "Overview", "Pros & Cons", "Practical", "Expert"])

with home_tab:
    with st.form(key="my_form"):
        chat = ""
        query = st.text_input("Enter a query:", placeholder="How do I build a cheese house?")
        submitted = st.form_submit_button("Submit")

    if query!="":
        chat = workflow.run(query)
        with open("response.txt", "w") as file:
            json.dump(chat, file, ensure_ascii=True)

        with overview_tab:
            st.header("Overview")
            with st.spinner():
                st.markdown(chat[2]["content"])

        with pros_cons_tab:
            st.header("Pros & Cons")
            with st.spinner():
                st.markdown(chat[3]["content"])

        with practical_tab:
            st.header("Practical")
            with st.spinner():
                st.markdown(chat[4]["content"])

        with expert_tab:
            st.header("Expert")
            with st.spinner():
                st.markdown(chat[5]["content"])

        if chat:
            st.success("Response generated!")
    else:
        st.info("Please submit a query to continue")