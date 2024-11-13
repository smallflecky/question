import streamlit as st
import openai
import os

# API-Schlüssel setzen (Umgebungsvariable empfohlen, um den Schlüssel zu schützen)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Alternativ: direkt openai.api_key = 'dein_openai_api_schlüssel'

st.title("Fragen für Paare – Dynamisch generiert mit ChatGPT")

# Anweisung für den Benutzer
st.write("Drücke auf den Button, um eine neue Frage für Paare zu generieren. Diese Fragen können lustig, tiefgründig oder persönlich sein – perfekt für interessante Gespräche!")

# Button zum Generieren einer neuen Frage
if st.button("Neue Frage generieren"):
    try:
        # Anfrage an die OpenAI-API senden, um eine Frage zu generieren
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Du bist ein kreativer Fragen-Generator für Paare."},
                {"role": "user", "content": "Erstelle eine neue Frage für Paare, die sie diskutieren können. Die Frage kann lustig, tiefgründig oder persönlich sein."}
            ],
            max_tokens=60,
            temperature=0.7,
        )

        # Die generierte Frage extrahieren
        question = response.choices[0].message['content'].strip()

        # Frage auf der Streamlit-Seite anzeigen
        st.success(f"Hier ist deine Frage: **{question}**")

    except Exception as e:
        # Fehler anzeigen, falls die API-Anfrage fehlschlägt
        st.error("Es gab ein Problem beim Generieren der Frage. Bitte versuche es erneut.")
        st.error(str(e))
