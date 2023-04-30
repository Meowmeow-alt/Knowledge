import streamlit as st
from PIL import Image

st.sidebar.success("This is the second page.")

#_________________OPENING_________________

st.title("> How our brain and thoughts affect out life?")
st.write("""
     Psychology is the study of human behavior. It has roots in healthcare and 
     the scientific method, helping uncover the processes of the mind. Through 
     research and observation, psychologists can help answer questions about the 
     brain's mysteries and improve mental health standards for communities.
          """)
st.write("###")
st.write("---")

#_________________DREAMS_________________

with st.container():
     st.header("Why do we dream?")
     leftcol, rightcol = st.columns((1,2))
     with rightcol:
          st.write("""
          After a great deal of scientific research, technological advancement and persistence, 
          we still don't have any definite answers, but we have some interesting theories:
          - We dream to fulfill our wishes.
          - We dream to remember.
          - We dream to forget.
          """)
     with leftcol:
          img = Image.open("Images/tải xuống.png")
          st.image(img)

with st.container():
     st.write("###")
     leftcol, rightcol = st.columns((2,1))
     with leftcol:
          st.write("""
          In the early 1900s, Sigmund Freud proposed that while all of our dreams, including 
          our nightmares are a collection of images from our daily conscious lives.
          - They also have symbolic meanings which relate to the fulfillment of our subconscious wishes.
          - Freud theorized that everything we remember when we wake up from a dream is a symbolic 
          representation of our unconscious primitive thoughts, urges, and desires.
          ###
          In 2010, researchers found that subjects were much better at getting through a complex 3-D 
          maze if they had napped and dreamed of the maze prior to their second attempt.
          - In fact, they were up to ten times better at it than those who only thought of the maze 
          while awake between attempts and those who napped but did not dream about the maze.
          - Researchers theorize that certain memory processes can happen only when we are asleep and 
          our dreams are a signal that these processes are taking place.
          ###
          A 1983 neurobiological theory of dreaming, called reverse learning, holds that while sleeping, 
          and mainly during REM sleep cycles, your neocortex reviews these neural connections and dumps 
          the unnecessary ones.\n
          There are even more reasons lead us to dream but these are the main ones.
          """)
     with rightcol:
          img1 = Image.open("Images/images.jpeg")
          st.image(img1)
          st.write("###")
          img2 = Image.open("Images/dream-of-someone.jpeg")
          st.image(img2)
          st.write("""
          ###
          - Without this unlearning process, your brain could be overrun by useless connections 
          and parasitic thoughts could disrupt the necessary thinking you need to do while you're awake.
          """)

st.write("###")
st.write("---")







