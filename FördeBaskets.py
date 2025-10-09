import streamlit as st
import urllib.parse
from PIL import Image

# --- SEITENKONFIGURATION ---
st.set_page_config(
    page_title="Mannschaftskasse Aufpolierer",
    page_icon="⚽",
    layout="centered"
)

# --- BILD UND TITEL ---

# Öffnen des Bildes
try:
    image = Image.open('KFB3.jpg')
    st.image(image, use_column_width=True)
except FileNotFoundError:
    st.error("Fehler: Die Bilddatei 'KFB3.jpg' wurde nicht gefunden. Bitte stellen Sie sicher, dass die Datei im selben Ordner wie das Skript liegt.")

st.title("⚽ Mannschaftskasse aufpolieren!")
st.markdown("Generiert für jeden Einkauf über Amazon einen kleinen Bonus für die Teamkasse.")


# --- AMAZON AFFILIATE LINK GENERATOR ---
st.header("1. Amazon Affiliate-Link erstellen")

# Ihr fester Affiliate-Tag
affiliate_tag = "affiliatesche-21" # Diesen bei Bedarf anpassen

# Eingabefeld für das Produkt
search_term = st.text_input(
    "Was möchtet ihr bei Amazon suchen?",
    placeholder="z.B. Nike Fußball, Taktiktafel, etc."
)

# Button zum Generieren
if st.button("Link für die Mannschaftskasse generieren"):
    if search_term:
        # Suchbegriff für die URL sicher kodieren
        encoded_search_term = urllib.parse.quote_plus(search_term)
        
        # Den finalen Affiliate-Link für amazon.de zusammenbauen
        amazon_link = f"https://www.amazon.de/s?k={encoded_search_term}&tag={affiliate_tag}"
        
        st.success("Erfolgreich erstellt! Kopiert diesen Link und teilt ihn:")
        # Den Link in einem Code-Block anzeigen, damit er einfach kopiert werden kann
        st.code(amazon_link, language="text")
        # Zusätzlich einen klickbaren Link zum Testen anbieten
        st.markdown(f"➡️ **[Hier klicken, um den Link zu testen]({amazon_link})**")
    else:
        # Fehlermeldung, wenn kein Suchbegriff eingegeben wurde
        st.warning("Bitte gebt einen Suchbegriff ein, um einen Link zu erstellen.")

# --- FOOTER ---
st.markdown("---")
st.info(
    """
    **Hinweis:** Bei jedem Kauf, der über einen hier generierten Link getätigt wird, 
    erhält unsere Mannschaftskasse eine kleine Provision von Amazon, ohne dass für euch Mehrkosten entstehen.
    Vielen Dank für die Unterstützung!
    """
)