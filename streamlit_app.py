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

project_3_page = st.Page(
    "views/pro1.py",
    title="pro1",
    icon=":material/smart_toy:",
)

project_4_page = st.Page(
    "views/pro2.py",
    title="pro2",
    icon=":material/smart_toy:",
)

project_5_page = st.Page(
    "views/pro3.py",
    title="pro3",
    icon=":material/smart_toy:",
)

project_6_page = st.Page(
    "views/pro4.py",
    title="pro4",
    icon=":material/smart_toy:",
)


project_7_page = st.Page(
    "views/pro5.py",
    title="pro5",
    icon=":material/smart_toy:",
)

project_8_page = st.Page(
    "views/pro6.py",
    title="pro6",
    icon=":material/smart_toy:",
)


project_9_page = st.Page(
    "views/pro7.py",
    title="pro7",
    icon=":material/smart_toy:",
)

project_10_page = st.Page(
    "views/pro8.py",
    title="pro8",
    icon=":material/smart_toy:",
)




# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page,project_3_page,project_4_page, project_5_page,project_6_page,project_7_page,project_8_page, project_9_page,project_10_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/codingisfun_logo.png")
st.sidebar.markdown("Made with ❤️ by [Abdelkhaliq](https://youtube.com/@codingisfun)")
pg.run()

