import streamlit as st
from PIL import Image
from streamlit_extras.let_it_rain import rain

rain(
     emoji = "🌸",
     font_size = 22,
     falling_speed = 7,
     animation_length = "infinite"
)

#_____________SIDEBAR____________

st.sidebar.success("Chào mừng bạn đến với điểm cuối của trang.")
st.sidebar.image(Image.open("Images/Bản sao 1261665.jpeg"))
st.sidebar.header("Thông tin liên hệ:")
st.sidebar.info(""" Email: baotiendancer@gmail.com
                    Discord ID: meowmeow_alt """)

# ___________ PHẦN 1 _____________

with st.container():
     left, right = st.columns((2,1))
     with left:
          st.title("Thông tin của mình :3")
          st.subheader("Mình là Bảo Tiên, sinh năm 2005\n:point_right:	:point_left: :heart_on_fire:")
          st.write("- Mình rất thích lập trình, tạo web và làm dự án.")
          st.write("- Mình có kiến thức về Python và CSS cơ bản (mình tự học)")
          st.write("- Mình vừa tốt nghiệp THPT Chuyên Lê Hồng Phong và đã đậu Bách Khoa TP.HCM")
          st.write("- Mình thích uống rau má sữa và ăn bánh ngọt~ :cake: :sparkles:")
          st.write("[Muốn tìm hiểu thêm về mình qua facebook >](https://www.facebook.com/baotiendancer/)")
     with right:
          img1 = Image.open("Images/a.jpg")
          st.image(img1)

