import random
import os
import string
import pandas as pd
import numpy as np


df_prov = pd.read_excel('Comuni.ods')
len = df_prov.shape[0]
pop_tot = df_prov.Popolazione.sum()
df_prov['Distribuzione'] = df_prov.Popolazione / pop_tot
array_prob = df_prov.Distribuzione.values


def gen_sent():
    sentenza = []

    # feature_1

    feature_1 = np.random.choice(['persona fisica', 'ente'], p=[0.8, 0.2])
    sentenza.append(feature_1)

    # feature_2

    feature_2 = random.choice(["persona fisica", "ente"])
    sentenza.append(feature_2)

    # feature_3

    if feature_1 == "persona fisica":
        feature_3 = "privato"
    else:
        feature_3 = random.choice(["privato", "pubblico"])

    sentenza.append(feature_3)

    # feature_4

    sentenza.append("privato")

    # feature_5

    if feature_3 == "pubblico":
        feature_5 = "no"
    else:
        feature_5 = random.choice(["si", "no"])

    sentenza.append(feature_5)

    # feature_6

    if feature_5 == "si":
        feature_6 = 100
    else:
        feature_6 = random.randrange(10, 100, 5)

    sentenza.append(feature_6)

    # feature_7

    feature_7 = random.randrange(10, 100, 5)

    sentenza.append(feature_7)

    # feature_8

    feature_8 = random.choice(["si", "no"])

    sentenza.append(feature_8)

    # feature_9

    if feature_8 == "no":
        feature_9 = "no"
    else:
        feature_9 = random.randrange(10, 100, 5)

    sentenza.append(feature_9)

    # feature_10

    feature_10 = random.choice(
        ["45.1", "46.4", "46.5", "47.4", "47.5", "47.7", "55.2", "56.1", "56.3", "79.1", "93.1", "93.2", "96.0"])

    sentenza.append(feature_10)

    # feature_11

    if feature_10 == "45.1":
        feature_11 = random.choice(["Commercio all'ingrosso di autovetture", "Commercio al dettaglio di autovetture"])

    elif feature_10 == "46.4":
        feature_11 = random.choice(["Commercio all'ingrosso di tessuti", "Commercio all'ingrosso di abbigliamento",
                                    "Commercio all'ingrosso di calzature",
                                    "Commercio all'ingrosso di profumi e cosmetici", "Commercio all'ingrosso di mobili",
                                    "Commercio all'ingrosso di elettrodomestici", "Commercio all'ingrosso di giochi",
                                    "Commercio all'ingrosso di articoli sportivi"])

    elif feature_10 == "46.5":
        feature_11 = random.choice(["Commercio all'ingrosso di computer", "Commercio all'ingrosso di software",
                                    "Commercio all'ingrosso di apparecchi telefonici",
                                    "Commercio all'ingrosso di mobili per l'ufficio"])

    elif feature_10 == "47.4":
        feature_11 = random.choice(["Commercio al dettaglio di computer", "Commercio al dettaglio di software",
                                    "Commercio al dettaglio di apparecchiature per telecomunicazioni",
                                    "Commercio al dettaglio di apparecchi audio e video",
                                    "Commercio al dettaglio di attrezzature per ufficio in esercizi specializzati"])

    elif feature_10 == "47.5":
        feature_11 = random.choice(["Commercio al dettaglio di tessuti", "Commercio al dettaglio di abbigliamento",
                                    "Commercio al dettaglio di strumenti musicali", "Commercio al dettaglio di mobili",
                                    "Commercio al dettaglio di elettrodomestici", "Commercio al dettaglio di giochi",
                                    "Commercio al dettaglio di articoli sportivi"])

    elif feature_10 == "47.7":
        feature_11 = random.choice(
            ["Commercio al dettaglio di calzature e accessori", "Commercio al dettaglio di profumeria",
             "Commercio al dettaglio di fiori e piante", "Commercio al dettaglio di gioielleria",
             "Commercio al dettaglio di mobili per ufficio"])

    elif feature_10 == "55.2":
        feature_11 = random.choice(["Villaggi Turistici", "Ostelli della Gioventù", "Affittacamere per brevi soggiorni",
                                    "Case ed appartamenti per vacanze", "Bed & Breakfast", "Residence"])

    elif feature_10 == "56.1":
        feature_11 = random.choice(["Ristorazione con somministrazione", "Gelaterie e Pasticcerie"])

    elif feature_10 == "56.3":
        feature_11 = random.choice(["Bar senza cucina"])

    elif feature_10 == "79.1":
        feature_11 = random.choice(["Attività delle agenzie di viaggio e dei tour operator"])

    elif feature_10 == "93.1":
        feature_11 = random.choice(
            ["Gestione di piscine", "Gestione di impianti sportivi polivalenti", "Gestione di palestre",
             "Gestione di attività di club sportivi"])

    elif feature_10 == "93.2":
        feature_11 = random.choice(
            ["Parchi di divertimento e parchi tematici", "Discoteche", "Sale da ballo", "Nigth Club",
             "Sale giochi e biliardi"])

    elif feature_10 == "96.0":
        feature_11 = random.choice(["Attività delle lavanderie industriali", "Lavanderie, tintorie",
                                    "Servizi dei saloni di barbiere e parrucchiere",
                                    "Servizi degli istituti di bellezza", "Servizi di manicure e pedicure",
                                    "Servizi di centri per il benessere fisico",
                                    "Stabilimenti termali"])

    sentenza.append(feature_11)

    # feature_12

    rand_prov = np.random.choice(len, p=array_prob)

    feature_12 = df_prov.loc[rand_prov, "\xa0Città"]

    sentenza.append(feature_12)

    # feature_13

    rand_affitto = np.random.choice(3, p=[0.7, 0.25, 0.05])

    if rand_affitto == 0:
        if feature_11 in ["Residence", "Villaggi Turistici", "Ostelli della Gioventù", "Gestione di piscine",
                          "Gestione di impianti sportivi polivalenti",
                          "Gestione di attività di club sportivi", "Parchi di divertimento e parchi tematici",
                          "Discoteche", "Sale da ballo", "Nigth Club",
                          "Sale giochi e biliardi", "Attività delle lavanderie industriali", "Stabilimenti termali"]:
            feature_13 = random.randrange(5000, 10000, 100)
        else:
            feature_13 = random.randrange(500, 10000, 100)
    elif rand_affitto == 1:
        feature_13 = random.randrange(10100, 30000, 100)
    elif rand_affitto == 2:
        feature_13 = random.randrange(30100, 50000, 100)

    sentenza.append(feature_13)

    # feature_14

    mode = random.choice(["mensili", "semestrali", "annuali"])
    if mode == "mensili":
        feature_14 = feature_13
    elif mode == "semestrali":
        feature_14 = feature_13 * 6
    elif mode == "annuali":
        feature_14 = feature_13 * 12

    sentenza.append(mode)
    sentenza.append(feature_14)

    # feature_15

    feature_15 = random.randint(3, 12)

    sentenza.append(feature_15)

    # feature_16

    feature_16 = random.choice(["si", "no"])

    sentenza.append(feature_16)

    # feature_17

    feature_17 = random.choice(["si", "no"])

    sentenza.append(feature_17)

    # feature_18

    feature_18 = random.choice(["si", "no"])

    sentenza.append(feature_18)

    # feature_19

    feature_19 = random.choice(
        ["garanzia bancaria / assicurativa", "garanzia prestata da soggetto non professionale (es. fideiussione)",
         "cauzione"])

    sentenza.append(feature_19)

    # feature_20

    if feature_19 == "cauzione":
        feature_20 = np.random.choice(3, p=[0.7, 0.15, 0.15]) + 1
    else:
        feature_20 = "no"

    sentenza.append(feature_20)

    # feature_21

    feature_21 = random.choice(["si", "no"])

    sentenza.append(feature_21)

    # feature_22

    if feature_21 == "si" and feature_2 == "persona fisica":
        if feature_7 <= 40 or feature_13 <= 20000:
            feature_22 = random.randrange(1000, 50000, 100)
        elif 40 < feature_7 <= 70 or 20000 < feature_13 <= 30000:
            feature_22 = random.randrange(50000, 100000, 100)
        elif 70 < feature_7 or 30000 < feature_13:
            feature_22 = random.randrange(100000, 150000, 100)
    elif feature_21 == "si" and feature_2 == "ente":
        if feature_7 <= 40 or feature_13 <= 20000:
            feature_22 = random.randrange(2000, 50000, 100)
        elif 40 < feature_7 <= 70 or 20000 < feature_13 <= 30000:
            feature_22 = random.randrange(50000, 100000, 100)
        elif 70 < feature_7 or 30000 < feature_13:
            feature_22 = random.randrange(100000, 150000, 100)
    else:
        feature_22 = "no"

    sentenza.append(feature_22)

    # feature_23

    feature_23 = random.choice(["si", "no"])

    sentenza.append(feature_23)

    # feature_24

    if feature_23 == "no":
        feature_24 = "no"
    else:
        if feature_10 == "55.2":
            feature_24 = 50
        else:
            feature_24 = np.random.choice([60, 20], p=[0.95, 0.05])

    sentenza.append(feature_24)

    return sentenza

n_sent = 1000

data = []

columns = ["Natura del locatore", "Natura del conduttore", "Qualità del locatore", "Qualità del conduttore",
           "Unica fonte di reddito?", "Percentuale dell’affitto rispetto a reddito totale",
           "Percentuale di perdita degli incassi rispetto al totale dei redditi del conduttore", "Quantifica riduzione richiesta?",
           "Percentuale di riduzione richiesta rispetto al totale della rata", "Destinazione del locale commerciale (ATECO)", "Descrizione attività",
           "Comune del locale", "Importo affitto mensile", "Periodicità del canone", "Importo pagamento del canone", "Per quante rate si chiede la riduzione",
           "Eventuale diritto di recesso", "Eventuale clausola risolutiva", "Eventuale presenza di garanzie",
           "Natura delle garanzie", "Mensilità cauzione", "Eventuali misure di sostegno", "Importo misure di sostegno",
           "Eventuale credito d’imposta", "Percentuale credito d'imposta"]

for i in range(n_sent):
  data.append(gen_sent())

df = pd.DataFrame(data, columns=columns)

df.to_excel('Sentenze_Random.xlsx')

