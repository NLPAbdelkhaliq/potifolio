import streamlit as st

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/dp.jpg", width=230)

with col2:
    st.title("Abdelkhaliq Sharawy Maysara", anchor=False)
    st.write(
        "Senior Data Analyst, assisting enterprises by supporting data-driven decision-making."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    '''
   - Years experience extracting actionable insights from data
   - Strong hands-on experience and knowledge in Python and Excel
   - Good understanding of statistical principles and their respective applications
   - Excellent team-player and displaying a strong sense of initiative on tasks
   '''
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    '''
    - Programming: Python (Scikit-learn, Pandas), SQL, VBA
    - Data Visualization: PowerBi, MS Excel, Plotly
    - Modeling: Logistic regression, linear regression, decision trees
    - Databases: Postgres, MongoDB, MySQL
    '''
)
st.write("\n")
st.subheader("links", anchor=False)
st.write(
    '''
- ('LinkedIn', 'https://www.linkedin.com/in/chanin-nantasenamat')
- ('Twitter', 'https://twitter.com/thedataprof')
- ('GitHub', 'https://github.com/chaninn/')
- ('', 'https://github.com/chaninlab/')
- ('', 'https://github.com/dataprofessor')
- ('ORCID', 'http://orcid.org/0000-0003-1040-663X')
- ('Scopus', 'http://www.scopus.com/authid/detail.url?authorId=12039071300')
- ('ResearcherID', 'http://www.researcherid.com/rid/F-1021-2010')
- ('ResearchGate', 'https://www.researchgate.net/profile/Chanin_Nantasenamat')
- ('Publons', 'https://publons.com/a/303133/')
'''
)


