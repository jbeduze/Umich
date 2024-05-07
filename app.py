import streamlit as st
import pagesetup as ps
from PIL import Image
from pagesetup import stylable_container_master
from streamlit_extras.stylable_container import stylable_container
#Page icon
IMG = Image.open('M.png')
st.set_page_config(page_title="University of Michigan Wrestling", page_icon=IMG, layout="wide", menu_items=None)

ps.set_background_1()
ps.hide_streamlit_header()
ps.Menu_tabs_display()