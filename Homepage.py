import streamlit as st
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title = "General knowledge",
                   page_icon = ":crown:",
                   layout = "wide")


#___________THONG TIN____________

st.sidebar.success("Select a page above")
st.sidebar.image('Images/tải xuống.jpeg', output_format='jpeg')
st.sidebar.header('📸 Caution')
st.sidebar.info(
    'This page is made by Tran Bao Tien\n\n'
    'No stolen please.\n\n'
    'For more information, sent me messages through my email.'
    )

rain(
     emoji = "*",
     font_size = 44,
     falling_speed = 7,
     animation_length = "infinite"
    )


st.title("'The river of knowledge has no depth' ― Chinonye J. Chidolue")
st.write("""
###
- If you ever have a thought of giving up. Remember back to the days you try your best to achieve it.
- Stand still means you already fall behind.
- If you stop chasing your dreams, someone else will.
""")

