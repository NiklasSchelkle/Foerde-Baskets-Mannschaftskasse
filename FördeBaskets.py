import streamlit as st
import urllib.parse
from PIL import Image

# --- SEITENKONFIGURATION ---
st.set_page_config(
    page_title="Mannschaftskasse Aufpolierer",
    page_icon="🏀",
    layout="centered"
)

# --- BILD UND TITEL ---

col1, col2 = st.columns([1, 2])

with col1:
    try:
        image = Image.open('KFB3.jpg')
        st.image(image)
    except FileNotFoundError:
        st.error("Bild 'KFB3.jpg' nicht gefunden.")

with col2:
    st.write("")
    st.write("")
    st.header("Alles für den KFB!")

st.title("🏀 Mannschaftskasse aufpolieren!")
st.markdown(
    """
    Generiert für jeden Einkauf über Amazon einen kleinen Bonus für die Teamkasse.  
    **Transparenzhinweis:** Diese Website enthält sogenannte *Affiliate-Links*.  
    Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.
    """
)

# --- AMAZON AFFILIATE LINK GENERATOR ---
st.header("1. Amazon Affiliate-Link erstellen")

# Dein Amazon-Partner-Tag
affiliate_tag = "affiliatesche-21"  # <- Anpassen, falls sich euer Tag ändert

# Eingabefeld
search_term = st.text_input(
    "Was möchtet ihr bei Amazon suchen?",
    placeholder="z.B. Nike Basketball, Taktiktafel, etc."
)

# Button zum Generieren
if st.button("Link für die Mannschaftskasse generieren"):
    if search_term:
        encoded_search_term = urllib.parse.quote_plus(search_term)
        amazon_link = f"https://www.amazon.de/s?k={encoded_search_term}&tag={affiliate_tag}"
        st.success("Erfolgreich erstellt! Kopiert diesen Link und teilt ihn:")
        st.code(amazon_link, language="text")
        st.markdown(f"➡️ **[Hier klicken, um den Link zu testen]({amazon_link})**")
    else:
        st.warning("Bitte gebt einen Suchbegriff ein, um einen Link zu erstellen.")

# --- FOOTER / RECHTLICHE HINWEISE ---
st.markdown("---")

st.info(
    """
    **Impressum (§ 5 TMG):**  
    Betreiber dieser Website:  
    **Niklas Schelkle**  
    Spichernstraße 9  
    24116 Kiel  
    Deutschland  
    📧 E-Mail: [niklasschelkle@gmail.com](mailto:niklasschelkle@gmail.com)

    **Verantwortlich für den Inhalt nach § 55 Abs. 2 RStV:**  
    Niklas Schelkle

    **Affiliate-Transparenz:**  
    Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.  
    Für euch entstehen dadurch *keine Mehrkosten*.

    **Datenschutz:**  
    Diese Seite verwendet keine Cookies oder Tracking außerhalb des Amazon-Partnerprogramms.  
    Beim Klick auf einen Amazon-Link werden Cookies von Amazon gesetzt, um den Einkauf korrekt zuordnen zu können.  
    Weitere Informationen findet ihr in der [Datenschutzerklärung von Amazon](https://www.amazon.de/gp/help/customer/display.html?nodeId=201909010).

    **Haftungsausschluss:**  
    Trotz sorgfältiger inhaltlicher Kontrolle übernehme ich keine Haftung  
    für die Inhalte externer Links. Für den Inhalt der verlinkten Seiten sind ausschließlich deren Betreiber verantwortlich.
    """
)

st.markdown("---")
st.caption("© 2025 Niklas Schelkle – Alle Rechte vorbehalten.")
