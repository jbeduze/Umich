import streamlit as st
import base64
from PIL import Image
from streamlit_extras.stylable_container import stylable_container
from tabs import Main, Personal_Stats_and_Plan, Profile, Team, AI_Analysis, Coach

#styled button. Copy and create new buttons with stylable_button1,2,3...
def stylable_button(button_text):
    css_style = """
        button {
            background-color: green;
            color: white;
            border-radius: 20px;
        }
    """
    st.markdown(f'<style>{css_style}</style>', unsafe_allow_html=True)
    st.button(button_text)

#styled containers. Copy and create new containers with stylable_container1,2,3...
def stylable_container(container_content):
    css_styles = """
        {
            border: 1px solid rgba(49, 51, 63, 0.2);
            border-radius: 0.5rem;
            padding: calc(1em - 1px)
        }
    """
    st.markdown(f'<style>{css_styles}</style>', unsafe_allow_html=True)
    st.markdown(container_content, unsafe_allow_html=True)

def set_background_1():
    """
    Set the background of the Streamlit app using a locally stored image.
    """
    image_path = 'homepage.png'  # Update this path
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """

    st.markdown(background_style, unsafe_allow_html=True)


def hide_streamlit_header():
    """
    Hide the Streamlit header and menu button.
    """
    hide_header_style = """
        <style>
            header[data-testid="stHeader"] {
                display: none;
            }
        </style>
        """
    st.markdown(hide_header_style, unsafe_allow_html=True)

def Menu_tabs_display():
    with st.container():
        tabs = st.tabs(["Main", "Personal Stats and Plan", "Profile", "Team", "AI Analysis", "Coach"])
        pages = [Main, Personal_Stats_and_Plan, Profile, Team, AI_Analysis, Coach]
        for tab, page in zip(tabs, pages):
            with tab:
                page.show()