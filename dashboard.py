import streamlit as st
from agents import workflow
import json

st.title("The Council")
st.caption("Powered by OpenAI and Swarms")

st.set_page_config(layout="wide", page_title="The Council")

home_tab, overview_tab, pros_cons_tab, practical_tab, expert_tab, arbitrator_tab = st.tabs(["Home", "Overview", "Pros & Cons", "Practical", "Expert", "Arbitrator"])
tabs = [overview_tab, pros_cons_tab, practical_tab, expert_tab, arbitrator_tab]
headers = ["Overview", "Pros & Cons", "Practical", "Expert", "Arbitrator"]

with home_tab:
    with st.form(key="my_form"):
        chat = ""
        query = st.text_input("Enter a query:", placeholder="How do I build a cheese house?")
        submitted = st.form_submit_button("Submit")

    if query!="":
        with st.spinner("Council is deliberating..."):
            chat = workflow.run(query)

        if chat:
            for i, tab in enumerate(tabs):
                with tab:
                    st.header(headers[i])
                    st.markdown(chat[2+i]["content"])   # 0 and 1 contains prompt & agents information respectively


            with open("response.txt", "w") as file:
                json.dump(chat, file, ensure_ascii=True)
                print("Response saved to response.txt")

            st.success("Response generated!")
    else:
        st.info("Please submit a query to continue")