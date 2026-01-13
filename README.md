# 🏀 Mannschaftskasse Aufpolierer (Amazon Affiliate Link Generator)

Erreichbar unter: https://foerdebaskets.streamlit.app/

Diese einfache Streamlit-Webanwendung hilft dem Team, die **Mannschaftskasse (KFB)** aufzubessern, indem sie Amazon-Einkäufe automatisch mit unserem Affiliate-Tag verknüpft.

Jedes Mal, wenn ein Teammitglied oder ein Fan über den generierten Link einkauft, erhält das Team eine kleine Provision von Amazon, ohne dass dem Käufer Mehrkosten entstehen. **Alles für den KFB!**

## 🎯 Zweck und Zielgruppe

* **Zweck:** Generierung von **Amazon-Affiliate-Links** mit dem Team-Tag.
* **Zielgruppe:** Teammitglieder, Trainer und Unterstützer, die ihre regulären Amazon-Einkäufe tätigen möchten, während sie gleichzeitig die Mannschaftskasse unterstützen.

## ✨ Funktionen

* **Link-Generator:** Erstellt einen sofort nutzbaren Amazon-Suchlink, basierend auf der eingegebenen Produktbezeichnung.
* **Automatischer Tagging:** Der Amazon-Partner-Tag (`affiliatesche-21`) wird automatisch in den generierten Link eingebettet.
* **Transparenz:** Klarer Hinweis auf die Funktionsweise der Affiliate-Links direkt auf der Startseite.

---

## 🚀 Wie es funktioniert

1.  **Produkt eingeben:** Man gibt das Produkt in das Textfeld ein, das man bei Amazon sucht (z.B. "Neue Laufschuhe" oder "Proteinriegel").
2.  **Link generieren:** Klickt auf den Button "Link für die Mannschaftskasse generieren".
3.  **Shoppen:** Kopiert den generierten Link und nutzt ihn für den Einkauf auf Amazon.

**Der gesamte Einkauf, den Sie über diesen Link tätigen, trägt zur Mannschaftskasse bei!**

---

## 🛠️ Technische Details

* **Framework:** Streamlit
* **Logik:** Die App verwendet das Python-Modul `urllib.parse` und den fest hinterlegten Affiliate-Tag:
    ```python
    affiliate_tag = "affiliatesche-21"
    ```
    Der generierte Link hat die Form: `https://www.amazon.de/s?k=[SUCHBEGRIFF]&tag=[AFFILIATE_TAG]`
* **Bild:** Die App versucht, das Bild `KFB3.jpg` für eine bessere visuelle Darstellung zu laden.

---

## 📢 Rechtliche Hinweise & Transparenz

**Wichtig: Diese Informationen sind für die Einhaltung der Vorschriften des Amazon-Partnerprogramms und deutscher Gesetze notwendig und werden im Footer der App angezeigt.**

### Affiliate-Transparenz

Diese Website enthält sogenannte **Affiliate-Links**. Als Betreiber und Amazon-Partner wird an qualifizierten Verkäufen verdient. **Für euch entstehen dadurch keinerlei Mehrkosten**. Der Preis des Produkts bleibt exakt derselbe.

### Impressum und Datenschutz

Der Betreiber der Website ist:

**Niklas Schelkle**
Spichernstraße 9
24116 Kiel
📧 E-Mail: [niklasschelkle@gmail.com](mailto:niklasschelkle@gmail.com)

Die Anwendung selbst verwendet **kein eigenes Tracking oder Cookies**. Beim Klick auf einen Amazon-Link werden jedoch die notwendigen Cookies von Amazon gesetzt, um den Einkauf dem Partnerkonto zuordnen zu können.
