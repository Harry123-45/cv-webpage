import streamlit as st
from pathlib import Path

def get_file_content_as_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()


# Pfad zur PDF-Datei
file_path = 'cv.pdf'

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)

left, right=st.columns(2)
right.markdown(""" <h3> Harry Chouhan </h3> 
               <br>
               <em> Ich bin Faziniert von IT weil es die Welt in große wegen verändern kann.</em>""", unsafe_allow_html=True)
with right: 
    # Der Download-Button, der die Datei zur Verfügung stellt
    st.download_button(
        label="📄 Download Lebenslauf",
        data=file_bytes,
        file_name=file_path,
        mime='application/pdf'
    )

left.image("profile-pic.png", width= 200)
st.markdown("<style> .stAppHeader {display:none;} ul {list-style-type: none; } </style>", unsafe_allow_html=True)


right.write("Kontakt daten:")
st.write("E-Mail: chouhanharry2010@gmail.com")

st.header("IT-Kompetenzen", anchor=False, divider="blue")

st.write("""
 - Webentwicklung: Fundierte Grundkenntnisse in HTML, CSS und Streamlit (Fullstack-Framework)
 - Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
 - Office-Suite: Versierter Umgang mit Microsoft Word, Excel und PowerPoint
 - Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
 - Schulprojekte: Erstellung datenbasierter Präsentationen und interaktiver Tabellenkalkulationen0
            """, unsafe_allow_html=True)

st.header("Schulbildung", anchor=False, divider="blue")
st.subheader("Fachmittelschule Schaumburgergasse, Wien")
st.write("""
         
► Schwerpunkt: Intensive IT-Spezialisierung, Fokus auf modernen Webtechnologien und Wirtschaft
►Zeitraum: September 2024 - laufend
         """)

st.subheader("Mittelschule Sechshaus, Wien", anchor=False)
st.write("""
         ► Schwerpunkt Informatik  
         ► Zeitraum: September 2020 – Juli 2024        
""")
st.header("Arbeitserfahrung", anchor=False, divider="blue")
st.write("""
         
 ► Berufspraktische Tage 1 : Bei Pagro diskont von 18. bis 22. Nov. 2023
 ► Berufspraktische Tage 2 : Bei Bawag P.S.K von 18. bis 22. Nov. 2024
         """)

st.header("Fähigkeiten", anchor=False, divider="blue")
st.markdown(r'''
►  teamfähig: Kann sehr gut in einem teamarbeiten
►  schnelle auffassung: Kann verstehe aufgaben schnell ohne viel hilfe
►  Zielstrebig: Mache alles um mein ziel zu schaffen
''')

st.header("Interessen und Hobbys", anchor=False, divider="blue")
st.markdown(r'''
- Video spiele: Ich spiele gerne video spiele in meine Freizeit
            
- Programmieren: Ich schaue gerne videos über programmieren und lerne gerne immer was neue über das Programmieren
            
- Fitness: Ich gehe sehr gerne ins Fitness studio
            
''')