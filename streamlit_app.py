import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
     "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)


# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
         
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/codingisfun_logo.png")
st.sidebar.markdown(" [Thumbnail Image Generator](https://youtube.com/@codingisfun)")
st.sidebar.markdown(" [Rust in Streamlit](https://youtube.com/@codingisfun)")
st.sidebar.markdown(" [Abdelkhaliq](https://youtube.com/@codingisfun)")
st.sidebar.markdown(" [Abdelkhaliq](https://youtube.com/@codingisfun)")
st.sidebar.markdown(" [Abdelkhaliq](https://youtube.com/@codingisfun)")
st.sidebar.markdown(" [Abdelkhaliq](https://youtube.com/@codingisfun)")
st.sidebar.markdown(" [Abdelkhaliq](https://youtube.com/@codingisfun)")
st.sidebar.markdown(" [Abdelkhaliq](https://youtube.com/@codingisfun)")
st.sidebar.markdown(" [Abdelkhaliq](https://youtube.com/@codingisfun)")
st.sidebar.markdown("Copyright © 2025 Novaxion ®")
pg.run()

