import json
import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

from sqlite3 import *


# maak de outputs folder als die nog niet bestaat
def generate_pdf(order_data):
    output_folder = "outputs"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # opslaglocatie maken voor pdf
    doc = SimpleDocTemplate(os.path.join(output_folder, "output.pdf"), pagesize=A4)
    styles = getSampleStyleSheet()
    content = []

    # voeg een witte A4 pagina toe
    content.append(Spacer(1, 0.5*inch))

    # voeg de ordergegevens toe aan de pdf
    content.append(Paragraph("Ordergegevens:", styles['Title']))
    content.append(Spacer(1, 0.2*inch))

    content.append(Paragraph(f"Ordernummer: {order_data['order']['ordernummer']}", styles['Normal']))
    content.append(Paragraph(f"Orderdatum: {order_data['order']['orderdatum']}", styles['Normal']))
    content.append(Paragraph(f"Betaaltermijn: {order_data['order']['betaaltermijn']}", styles['Normal']))
    content.append(Paragraph(f"Klantnaam: {order_data['order']['klant']['naam']}", styles['Normal']))
    content.append(Paragraph(f"Klantadres: {order_data['order']['klant']['adres']}", styles['Normal']))
    content.append(Paragraph(f"Klantpostcode: {order_data['order']['klant']['postcode']}", styles['Normal']))
    content.append(Paragraph(f"Klantstad: {order_data['order']['klant']['stad']}", styles['Normal']))
    content.append(Paragraph(f"KVK-nummer: {order_data['order']['klant']['KVK-nummer']}", styles['Normal']))
    content.append(Spacer(1, 0.2*inch))

    # voeg de productgegevens toe aan de pdf
    content.append(Paragraph("Producten:", styles['Title']))
    content.append(Spacer(1, 0.2*inch))

    # datum en tijd ophalen                   # tijd afronden op minuten
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    for product in order_data['order']['producten']:
        content.append(Paragraph(f"Productnaam: {product['productnaam']}", styles['Normal']))
        content.append(Paragraph(f"Aantal: {product['aantal']}", styles['Normal']))
        content.append(Paragraph(f"Prijs per stuk (excl. btw): {product['prijs_per_stuk_excl_btw']}", styles['Normal']))
        content.append(Paragraph(f"Btw-percentage: {product['btw_percentage']}", styles['Normal']))
        content.append(Spacer(1, 0.4*inch))

        # datum en tijd weergeven
        content.append(Paragraph(f"Datum en tijd: {current_datetime}", styles['Normal']))

    doc.build(content)

    # json bestand opslaan
    with open(os.path.join(output_folder, "output.json"), 'w') as json_output:
        json.dump(order_data, json_output, indent=4)

# json gegevens laden vanuit een bestand
with open('test_set_softwareleverancier/test_set_softwareleverancier/2001-534.json') as json_file:
    order_data = json.load(json_file)

# aanroepen van de functie met de gegevens uit de json
generate_pdf(order_data)

print("PDF en JSON-bestanden gegenereerd met de ingevoerde gegevens.")

