import json
import datetime
import os
import sqlite3

def create_database():
    conn = sqlite3.connect('order_database.db')
    cursor = conn.cursor()

    # Tabel klanten
    cursor.execute('''CREATE TABLE IF NOT EXISTS klanten (
                    klant_id INTEGER PRIMARY KEY,
                    naam TEXT,
                    adres TEXT,
                    postcode TEXT,
                    stad TEXT,
                    KVK_nummer TEXT
                    )''')

    # Tabel facturen
    cursor.execute('''CREATE TABLE IF NOT EXISTS facturen (
                    factuur_id INTEGER PRIMARY KEY,
                    ordernummer INTEGER,
                    orderdatum DATE,
                    betaaltermijn DATE,
                    klant_id INTEGER,
                    FOREIGN KEY (klant_id) REFERENCES klanten(klant_id)
                    )''')

    # Tabel factuurregels
    cursor.execute('''CREATE TABLE IF NOT EXISTS factuurregels (
                    regel_id INTEGER PRIMARY KEY,
                    factuur_id INTEGER,
                    productnaam TEXT,
                    aantal INTEGER,
                    prijs_per_stuk_excl_btw REAL,
                    btw_percentage REAL,
                    FOREIGN KEY (factuur_id) REFERENCES facturen(factuur_id)
                    )''')

    conn.commit()
    conn.close()

def insert_data(order_data):
    conn = sqlite3.connect('order_database.db')
    cursor = conn.cursor()

    # Voeg klantgegevens toe
    klant = order_data['order']['klant']
    cursor.execute('''INSERT INTO klanten (naam, adres, postcode, stad, KVK_nummer)
                    VALUES (?, ?, ?, ?, ?)''', (klant['naam'], klant['adres'], klant['postcode'], klant['stad'], klant['KVK-nummer']))
    klant_id = cursor.lastrowid

    # Voeg factuurgegevens toe
    order = order_data['order']
    cursor.execute('''INSERT INTO facturen (ordernummer, orderdatum, betaaltermijn, klant_id)
                    VALUES (?, ?, ?, ?)''', (order['ordernummer'], order['orderdatum'], order['betaaltermijn'], klant_id))
    factuur_id = cursor.lastrowid

    # Voeg factuurregelgegevens toe
    for product in order['producten']:
        cursor.execute('''INSERT INTO factuurregels (factuur_id, productnaam, aantal, prijs_per_stuk_excl_btw, btw_percentage)
                        VALUES (?, ?, ?, ?, ?)''', (factuur_id, product['productnaam'], product['aantal'], product['prijs_per_stuk_excl_btw'], product['btw_percentage']))

    conn.commit()
    conn.close()

create_database()

# JSON-gegevens laden vanuit een bestand
with open('test_set_softwareleverancier/test_set_softwareleverancier/2000-018.json') as json_file:
    order_data = json.load(json_file)

# Gegevens invoegen in de database
insert_data(order_data)

print("Database aangemaakt en gegevens ingevoegd.")
