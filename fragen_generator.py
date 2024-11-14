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
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Du bist ein kreativer Fragen-Generator für Paare, die Fragen müssen aber nicht zwingend nur für Paare geeignet sein."},
                {"role": "user", "content": "Die Frage kann lustig, tiefgründig, aber auch sehr persönlich sein und soll zu einer längeren Diskussion anregen. Vermeide typische Fragen wie Wenn du einen Tag in einem anderen Körper wärst oder Gedanken lesen können. Stelle sicher, dass die Frage originell ist und unterschiedliche Perspektiven zulässt. "
            "Hier sind Beispiele für die Art von Fragen, die ich meine: 
            "1. 'Was ist ein gemeinsames Erlebnis, das dir besonders in Erinnerung geblieben ist und warum?' "
            "2. 'Was denkst du, war der prägendste Moment deiner Kindheit, der dich heute noch beeinflusst?' "
            "3. 'Gibt es eine Eigenschaft von dir, die du gerne mehr in unserer Beziehung zeigen würdest?' "
            "4. Wenn wir beide ein eigenes Kochbuch schreiben würden, wie würde es heißen und was wäre unser verrücktestes Rezept?' "
             "5. Angenommen, wir müssten ein Jahr in einem Tiny House leben – was wäre wohl die größte Herausforderung für uns beide?' "
            "6. Gibt es eine Erfahrung, die wir noch nicht gemeinsam gemacht haben, die du dir aber wünschst? Warum?' "
            "Erstelle eine neue Frage im gleichen Stil.
            " 7. Gibt es eine Situation, in der du dir mehr Unterstützung von mir gewünscht hättest? Was hätte ich tun können, um dir zu helfen?' "
            "8. Was ist eine Herausforderung, vor der du schon länger stehst und die du gerne besser meistern würdest?' "
            "9. Was ist ein Traum, den du schon lange hast, den aber nur wenige Menschen kennen?' "}
            ],
            max_tokens=60,
            temperature=0.8,
        )

        # Die generierte Frage extrahieren
        question = response.choices[0].message['content'].strip()

        # Frage auf der Streamlit-Seite anzeigen
        st.success(f"Hier ist deine Frage: **{question}**")

    except Exception as e:
        # Fehler anzeigen, falls die API-Anfrage fehlschlägt
        st.error("Es gab ein Problem beim Generieren der Frage. Bitte versuche es erneut.")
        st.error(str(e))
