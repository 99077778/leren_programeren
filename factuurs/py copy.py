import json
import datetime
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet




def generate_pdf(order_data):
    output_folder = "outputs"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    doc = SimpleDocTemplate(os.path.join(output_folder, "output.pdf"), pagesize=A4)
    styles = getSampleStyleSheet()
    content = []


    # Voeg een witte A4 pagina toe
    content.append(Spacer(1, 0.5*inch))

    # Voeg de ordergegevens toe aan de PDF
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

    # Voeg de productgegevens toe aan de PDF als tabel
    content.append(Paragraph("Producten:", styles['Title']))
    content.append(Spacer(1, 0.2*inch))

    table_data = [["Productnaam", "Aantal", "Prijs per stuk (excl. btw)", "Btw-percentage"]]
    for product in order_data['order']['producten']:
        table_data.append([
            product['productnaam'],
            product['aantal'],
            product['prijs_per_stuk_excl_btw'],
            product['btw_percentage']
        ])

    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    content.append(table)
    content.append(Spacer(1, 0.4*inch))

    # Voeg de datum en tijd toe
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    content.append(Paragraph(f"Datum en tijd: {current_datetime}", styles['Normal']))

    doc.build(content)

    # Sla JSON-bestand op
    with open(os.path.join(output_folder, "output.json"), 'w') as json_output:
        json.dump(order_data, json_output, indent=4)

# JSON-gegevens laden vanuit een bestand
with open('test_set_softwareleverancier/test_set_softwareleverancier/2001-534.json') as json_file:
    order_data = json.load(json_file)

# Roep de functie aan met de gegevens uit de JSON
generate_pdf(order_data)

print("PDF en JSON-bestanden gegenereerd met de ingevoerde gegevens.")
