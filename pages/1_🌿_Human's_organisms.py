import streamlit as st
from PIL import Image

st.sidebar.success("This is the first page.")

#_________________OPENING_________________

st.title("> Have you ever wondered how our bodies work?")
st.write("""To survive and reproduce, the human body relies on major internal body organs to 
             perform certain vital functions. When two or more organs along with their associated 
             structures work together they become component parts of a body system.""")
st.write("###")
st.write("---")

#________________PANCREAS__________________

with st.container():
    st.write("Beneath your ribs, you'll find, among other things,")
    st.header("THE PANCREAS")
    leftcol, rightcol = st.columns((2,1))
    with leftcol:
        st.write("""
        An organ that works a lot like a personal health coach:
        - This organ controls your sugar levels and produces a special juice that releases the
        nutrients from your food.
        - To help keep you in the best possible shape.
        - One of its jobs is to break down the food you eat.
        - It aids digestion by producing a special tonic made of water, sodium bicarbonate and
        digestive enzymes.
        - Sodium bicarbonate neutralizes the stomach's natural acidity so these digestive enzymes
        can perform their jobs.
        - Lipase breaks down fatty substances, protease splits up proteins and amylase divides
        carbohydrates to create energy-rich sugars.
        Most of those nutrients get absorbed into the blood stream and go on to enrich the body.
        ###
        The pancreas also works on controlling the amount of sugar in your blood:
        - It achieves this with the hormones insulin and glucagon which are produced in special
        cells called the Islets of Langerhans.
        - Having too much or too little sugar can be life threatening, so the pancreas must stay
        on constant alert.
        - After big meals, the blood often becomes flushed with sugar. To bring us back to normal,
        the pancreas releases insulin.
        - This makes the excess sugar move into cells, where it's either used as an energy source,
        or stored for later.
        - Insulin also tells the liver to shut down sugar production.
        - If blood sugar is low, the pancreas releases glucagon then body's cells and liver release
        stored sugars back into the bloodstream.
        """)
    with rightcol:
        img = Image.open("Images/gettyimages-188057956-612x612.jpeg")
        st.image(img)
        img1 = Image.open("Images/gettyimages-168832814-612x612.jpeg")
        st.image(img1)

st.write("###")
st.write("---")

#_________________KIDNEY___________________

with st.container():
    st.write("Behind the sudden urge that follows are two bean-shaped organs that work as fine-tuned internal sensors.")
    st.header("THE KIDNEYS")
    leftcol, gap, rightcol = st.columns((0.8,0.2,2))
    with rightcol:
        st.write("""
        An organ that balance the amount of fluid in your body, detect waste in your blood, and
        know when to release the vitamins, minerals and hormones you need to stay alive:
        - These organs dispose of waste products and to turn them into urine.
        - These organs filter about 180 liters of blood every 24 hours.
        - Blood enters each kidney through arteries that branch and branch, until they form tiny vessels 
        that entwine with special internal modules, called nephrons.
        - In each kidney, 1 million of nephrons form a powerful array of filters and sensors that carefully 
        sift through the blood.
        - To filter the blood, each nephron uses two powerful pieces of equipment: a blob-like structure 
        called a glomerulus, and a long, stringy, straw-like tubule.
        - The glomerulus works like a sieve, allowing only certain ingredients, such as vitamins and minerals, 
        to pass into the tubule.
        - this vessel's job is to detect whether any of those ingredients are needed in the body.
        - If so, they're reabsorbed in amounts that the body needs, so they can circulate in the blood again.
        ###
        But the blood doesn't only carry useful ingredients. It also contains waste products.
        - The tubules sense compounds the body doesn't need, like urea, left over from the breakdown of proteins, 
        and redirects them as urine out of the kidneys and through two long sewers called ureters.
        - The tubes empty their contents into the bladder to be discharged, ridding your body of that waste once 
        and for all.
        - If the kidney detects too much water in your blood, it sends extra liquid to the bladder to be removed.
        - On the other hand, low water levels in the blood prompt the kidney to release some back into the blood 
        stream, meaning that less water makes it into the urine.
        """)
    with leftcol:
        img2 = Image.open("Images/gettyimages-1190674216-612x612.jpeg")
        st.image(img2)
        img3 = Image.open("Images/thinkstockphotos501058323_869001.jpeg")
        st.image(img3)
        st.write("""
        ###
        Fine balancing act isn't the kidney's only skill.
        - These organs have the power to activate vitamin D to secrete a hormone called renin that raises blood 
        pressure and another hormone called erythropoietin, which increases red blood cell production.
        - Without the kidneys, our bodily fluids would spiral out of control.""")

#__________________LUNGS___________________



#__________________LIVER__________________



#__________________HEART___________________




