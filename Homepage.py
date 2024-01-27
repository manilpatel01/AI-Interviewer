import streamlit as st
from streamlit_option_menu import option_menu
from app_utils import switch_page
import streamlit as st
from PIL import Image

mn=Image.open("AI.webp")
st.set_page_config(page_title = "AI Interviewer", layout = "centered",page_icon=mn)
if True:
    home_title = "AI Interviewer"
    home_introduction = "Welcome to AI Interviewer, empowering your interview preparation with generative AI."
    with st.sidebar:
        st.markdown('## AI Interviewer')
        st.markdown(""" 
        #### Contact Us:
        [Manil Patel] (https://www.linkedin.com/in/manilpatel1501)
                    """)
    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )

    col1, col2, col3= st.columns([1,7,1])

    with col1:
        st.write("")

    with col2:
        st.image(mn, width=500)

    with col3:
        st.write("")

    st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5></font></span>""",unsafe_allow_html=True)
    st.markdown("""\n""")
    st.markdown("Welcome to AI Interviewer! Driven by Generative AI, it acts as your personal mock interviewer that focuses on Technical and Behavioral skills. By uploading your resume and job descriptions, you'll receive tailored questions to conduct mock interview.")
    st.markdown("""\n""")
    st.markdown("#### Get started!")
    st.markdown("Select one of the following options to start your interview!")
    selected = option_menu(
            menu_title= None,
            options=["Technical", "Resume", "Behavioral"],
            icons = ["cast", "cloud-upload", "cast"],
            default_index=0,
            orientation="horizontal",
        )
    if selected == 'Technical':
        st.info("""
            In this session, The AI Interviewer will evaluate your technical abilities with respect to job description.
                
            Note: You may only answer with a maximum length of 4097 tokens!
            - It will take 10 to 15 minutes for each interview.
            - Refreshing the page will initiate a new session.
            - Select your preferred mode of communication (voice or chat). 
            - Begin by introducing yourself and have fun！ """)
        if st.button("Start Interview!"):
            switch_page("Technical Interview")
    if selected == 'Resume':
        st.info("""
        In this session, The AI Interviewer will review your resume, assess your abilities based on your previous experiences.
        
        Note: You may only answer with a maximum length of 4097 tokens!
        - It will take 10 to 15 minutes for each interview.
        - Refreshing the page will initiate a new session.
        - Select your preferred mode of communication (voice or chat).
        - Begin by introducing yourself and have fun！ """
        )
        if st.button("Start Interview!"):
            switch_page("Resume based Interview")
    if selected == 'Behavioral':
        st.info("""
        In this session, The AI Interviewer will evaluate your behavioral skills with respect to job description.
        
        Note: You may only answer with a maximum length of 4097 tokens!
        - It will take 10 to 15 minutes for each interview.
        - Refreshing the page will initiate a new session.
        - Select your preferred mode of communication (voice or chat).
        - Begin by introducing yourself and have fun！ 
        """)
        if st.button("Start Interview!"):
            switch_page("Behavioral Interview")
    st.markdown("""\n""")
  