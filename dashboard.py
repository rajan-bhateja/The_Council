import streamlit as st

st.title("The Council of the LLMs")
st.caption("Powered by OpenAI, Gemini, Mistral, Groq, and Hugging Face")
st.caption("Orchestration by Swarms")

st.set_page_config(layout="wide", page_title="The Council of the LLMs")

home_tab, openai_tab, gemini_tab, mistral_tab, groq_tab, hf_tab, final_tab = st.tabs(["Home", "OpenAI", "Gemini", "Mistral", "Groq", "Hugging Face", "Final"])

with home_tab:
    with st.form(key="my_form"):
        query = st.text_input("Enter a query:", placeholder="Suggest 5 most popular places to visit in London")
        submitted = st.form_submit_button("Submit")

    if query!="":
        pass
    else:
        st.info("Please submit a query to continue")

    with openai_tab:
        st.header("OpenAI's Opinions")

    with gemini_tab:
        st.header("Gemini's Opinions")

    with mistral_tab:
        st.header("Mistral's Opinions")

    with groq_tab:
        st.header("Groq's Opinions")

    with hf_tab:
        st.header("Hugging Face's Opinions")

    with final_tab:
        st.header("Final Opinion")