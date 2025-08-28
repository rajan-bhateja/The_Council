import streamlit as st
from agents import workflow

st.title("The Council")
st.caption("Powered by OpenAI and Swarms")

st.set_page_config(layout="wide", page_title="The Council")

home_tab, overview_tab, pros_cons_tab, practical_tab, expert_tab = st.tabs(["Home", "Overview", "Pros & Cons", "Practical", "Expert"])

with home_tab:
    with st.form(key="my_form"):
        chat = ""
        query = st.text_input("Enter a query:", placeholder="How do I build a house from cheese?")
        submitted = st.form_submit_button("Submit")

    if query!="":
        chat = workflow.run(query)
        with overview_tab:
            st.header("Overview")
            with st.spinner():
                if chat!="":
                    st.markdown(chat)
                    print(chat)

        with pros_cons_tab:
            st.header("Pros & Cons")
            st.markdown(chat)

        with practical_tab:
            st.header("Practical")
            st.markdown(chat)

        with expert_tab:
            st.header("Expert")
            st.markdown(chat)
    else:
        st.info("Please submit a query to continue")