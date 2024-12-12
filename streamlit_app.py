import streamlit as st

left ,right=st.columns(2)

left.image("image.jpg", width= 100)
right.header("Harry Chouhan")
st.title("🎈 My new app😎", anchor=False)
st.header("Ich bin ein neue Überschrift💀", anchor=False)
st.subheader("Noch eine kleinere Überschrift🤣", anchor=False)
st.write("Das ist mein Streamlit-App")

st.markdown("<p>Ich bin ein Text</p>",unsafe_allow_html=True)

st.markdown("<a href=´https://www.google.at`>link</a>", unsafe_allow_html=True)

st.header("IT-Kompetenzen", anchor=False, divider="blue")

st.write("""
 - Webentwicklung: Fundierte Grundkenntnisse in HTML, CSS und Streamlit (Fullstack-Framework)
 - Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
 - Office-Suite: Versierter Umgang mit Microsoft Word, Excel und PowerPoint
 - Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
 - Schulprojekte: Erstellung datenbasierter Präsentationen und interaktiver Tabellenkalkulationen
            """, unsafe_allow_html=True)

st.header("Schulbildung", anchor=False, divider="blue")
st.subheader("Fachmittelschule Schaumburgergasse, Wien")
st.write("""
         
► Schwerpunkt: Intensive IT-Spezialisierung, Fokus auf modernen Webtechnologien und Wirtschaft
►Zeitraum: September 2024 - Juli 2025
         """)

st.subheader("Mittelschule Sechshaus, Wien", anchor=False)
st.write("""
► Schwerpunkt Informatik
► Zeitraum: September 2020 – Juli 2024        
""")
st.header("Arbeitserfahrung", anchor=False, divider="blue")
st.write("""
         
 - Berufspraktische Tage 1: Bei Bawag P.S.K von 18. bis 22. Nov. 2024
 - Berufspraktische Tage 2: Bei XYZ von 24. bis 28. Feb. 2025
         """)

