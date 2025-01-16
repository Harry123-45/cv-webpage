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
               <em> Ich bin faziniert von IT weil es die Welt auf große Weise verändern kann.</em>""", unsafe_allow_html=True)
with right: 
    # Der Download-Button, der die Datei zur Verfügung stellt
    st.download_button(
        label="📄 Download Lebenslauf",
        data=file_bytes,
        file_name=file_path,
        mime='application/pdf'
    )

left.image("shared image.jpg", width= 200)
st.markdown("<style> .stAppHeader {display:none;} ul {list-style-type: none; } </style>", unsafe_allow_html=True)


right.write("Kontaktdaten:")
st.write("+43 688 64260400")
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
         
 ► Berufspraktische Tage 2 : Bei BAWAG P.S.K von 18. bis 22. Nov. 2024
         """)

st.header("Fähigkeiten", anchor=False, divider="blue")
st.markdown(r'''
►  Teamfähig: Kann sehr gut im Team arbeiten.
            
►  schnelle Auffassungsgabe: Kann Aufgaben schnell verstehen, ohne viel Hilfe.
            
►  Zielstrebig: Mache alles um meine Ziele zu erreichen.
            
''')

st.header("Interessen und Hobbys", anchor=False, divider="blue")
st.markdown(r'''
- Videospiele: Ich spiele gerne Videospiele in meiner Freizeit.
            
- Programmieren: Ich schaue Videos über das Thema Programmieren und lerne gerne draus.
            
- Fitness: Ich gehe sehr gerne ins Fitnessstudio.
            
''')