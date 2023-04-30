import streamlit as st
from Pages import Human as human
from Pages import Psychology as psy

def main():
    st.sidebar.header('Documantaries')
    pages = {
        "🌿 Human's organisms" :  [human.main, []],     
        "🧠 Psychology":          [psy.main, []], 
    }

#___________THONG TIN____________

    st.sidebar.header('📘 About')
    st.sidebar.info(
        'This page is made by Tran Bao Tien\n\n'
        'No stolen please\n\n'
        'For more information, sent me messages through my email.'
    )

st.set_page_config(page_title = "General knowledge",
                   page_icon = ":crown:",
                   layout = "wide")

st.sidebar.success("Select a page above")

st.title("'The river of knowledge has no depth' ― Chinonye J. Chidolue")
st.write("""
###
- If you ever have a thought of giving up. Remember back to the days you try your best to achieve it.
- Stand still means you already fall behind.
- If you stop chasing your dreams, someone else will.
""")

