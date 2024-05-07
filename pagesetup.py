import streamlit as st
import base64
from PIL import Image
from streamlit_extras.stylable_container import stylable_container
from tabs import Main, Team, AI_Analysis

def Menu_tabs_display():
        tabs = st.tabs(["Main Profile", "Team", "AI Analysis"])
        pages = [Main, Team, AI_Analysis]
        for tab, page in zip(tabs, pages):
            with tab:
                page.show()

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




def example(vartext):
    with stylable_container(
        key="green_button",
        css_styles="""
         {
                box-shadow: 0px 0px 6px #FFCB0B;
                background-color: #30588580;
                color: white;
                border-radius: 10px;
                border: 2px solid #ccc;
                margin: 10px;
                padding: 10px;
        }
        """,
    ):
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1,10,1,5,1,7,1])
        st.header(vartext)
        st.markdown("this is markdown")

def stylable_container_master():
    with stylable_container(
        key= "master_container",
        css_style = """
            {
                background-color: #3F9EED;
                color: #3FED43;
                border-radius: 15px;
                padding: 15px;
                margin: 10px;
                border: 2px solid #ccc;
                box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1);
                font-family: 'Arial', sans-serif;
                font-size: 14px;
                transition: background-color 0.3s ease, box-shadow 0.3s ease;
            }
            """,
    ):
        st.write("yep")

def page_stylable_container():
    with stylable_container(
    css_style = """
        {
            background-color: #3F9EED;
            color: #3FED43;
            border-radius: 15px;
            padding: 15px;
            margin: 10px;
            border: 2px solid #ccc;
            box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1);
            font-family: 'Arial', sans-serif;
            font-size: 14px;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
        }
        div.st-container:hover {
            background-color: #e0e0e0;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        }
    """,
    ):
        st.markdown("this is a container")
        col1_1, col2_1, col3_1, col4_1, col5_1, col6_1, col7_1 = st.columns([1,5,1,3,1,3,1], gap = "small")

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





