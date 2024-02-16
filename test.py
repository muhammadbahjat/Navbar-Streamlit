import streamlit as st
import base64

logo_path = r'logo1.png'
with open(logo_path, "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode('utf-8')

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
    <style>
    .stApp header {
            z-index: 1;
            background: transparent;
    }
            </style>
            """,unsafe_allow_html=True)
st.markdown(
        """1
        <style>
        .st-d4.st-b8.st-d5 {
        width: 30%;
        }
        .navbar {
        position: fixed;
        top: 0px;
        left: 0px;
        width: 96%;
        padding: 0px;
        z-index: 1;
        padding-left: 20px;
        padding-right: 39px;
        background: transparent;
        }
        .navbar img {
            width: 70px;
            height: 50px;  
        }
        .navbar-brand img {
        max-height: 45px !important;
        }
        [data-testid="stHeader"] {{
        z-index: 0;
        background: rgba(0,0,0,0);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.markdown(f"""
    <style>
        form {{
            onsubmit: "Streamlit.button.click(() => alert('Get in Touch clicked!'))";
        }}
        .navbar {{
            padding-right: 10px;
            padding-left: 30px;
        }}
        .navbar-brand img {{
            max-height: 50px; 
        }}
    </style>
    <form action="mailto:syedmbahjat848@gmail.com" method="get">
        <nav class="navbar">
            <a class="navbar-brand" href="#">
                <img src="data:image/png;base64,{encoded_logo}" alt="">
            </a>
            <button class="btn btn-outline-danger" type="submit">Get in Touch</button>
        </nav>
    </form>
    """, unsafe_allow_html=True)