import streamlit as st
import pagesetup as ps
from PIL import Image

#Page icon
IMG = Image.open('M.png')
st.set_page_config(
    page_title="University of Michighan Wrestling", page_icon=IMG, layout="wide", menu_items=None)


def local_css(file_name):
    with open(file_name, "r") as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

def display_fonts():
    # Load the local CSS file
    local_css("style.css")
display_fonts()
# def load_css():
#     """Loads an external CSS file and injects it into the Streamlit app."""
#     with open("style.css", "r") as f:
#         css = f.read()
#         st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


ps.set_background_1()
ps.hide_streamlit_header()

col3_1, col3_2 = st.columns([3,1], gap= "small")

col1_1, col1_2, col1_3, col1_4 = st.columns([2,1,1,1], gap= "small")

col2_1, col2_2, col2_3, col2_4 = st.columns([2,1,1,2], gap= "small")



with col3_1:
    ps.Menu_tabs_display()


st.write("UMich")
with col1_3:
    st.write("hello there")

ps.stylable_container("write this")
content = "this is the content I want in container 1"
ps.stylable_container(content)

ps.stylable_button("customize your button with this")