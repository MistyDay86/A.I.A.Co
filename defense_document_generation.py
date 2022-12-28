import random
import os
import string
import pandas as pd
import numpy as np

from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.forms.text_field import TextField
from borb.pdf.canvas.color.color import HexColor
from decimal import Decimal
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.forms.drop_down_list import DropDownList
from pathlib import Path

from borb.pdf.canvas.layout.text.chunks_of_text import HeterogeneousParagraph
from borb.pdf.canvas.layout.text.chunk_of_text import ChunkOfText
from borb.pdf.page.page import Page, TextAnnotationIconType
from borb.pdf.page.page_size import PageSize
from borb.pdf.canvas.color.color import HexColor
from borb.pdf.canvas.geometry.rectangle import Rectangle

n_sent = 1000
df = pd.read_excel('Sentenze_Random.xlsx')
df.drop('Unnamed: 0', inplace=True, axis=1)

def ita(x):

  return format(x,',d').replace(",",".")

for i in range(n_sent):
  pdf = Document()
  page = Page()
  pdf.append_page(page)
  layout: PageLayout = SingleColumnLayout(page,
  horizontal_margin=Decimal(30),
  vertical_margin=Decimal(12),)
  layout.add(Paragraph("Caso", font="Helvetica-Bold", text_alignment=Alignment.CENTERED))
  #layout.add(Paragraph(" ", font="Helvetica-Bold"))
  layout.add(Paragraph("Premesso che:", font="Helvetica"))

  if df.loc[i, "Natura del conduttore"]=='persona fisica' and df.loc[i, "Unica fonte di reddito?"]=="si":
    chunks_of_text = [
    ChunkOfText(
    " - il Sig. Marco Rossi, soggetto ", font="Helvetica"
    ),
    ChunkOfText(
    "%s" %df.loc[i, "Qualità del conduttore"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    ", è conduttore del locale commerciale sito in ", font="Helvetica"
    ),
    ChunkOfText(
    "%s," %df.loc[i, "Comune del locale"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    " nel quale esercita l'attività di ", font="Helvetica"
    ),
    ChunkOfText(
    "  %s" %df.loc[i, "Descrizione attività"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    " (codice ATECO ", font="Helvetica"
    ),
    ChunkOfText(
    "%s" %df.loc[i, "Destinazione del locale commerciale (ATECO)"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    "), ", font="Helvetica"
    ),
    ChunkOfText(
    "fonte unica del suo reddito;", font="Helvetica-Bold"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - il Sig. Marco Rossi, soggetto %s, è conduttore del locale commerciale sito in %s, nel quale esercita l'attività di %s (codice ATECO %s);" %(value_0,df.loc[i, "Comune del locale"], df.loc[i, "Descrizione attività"], df.loc[i, "Destinazione del locale commerciale (ATECO)"]), font="Helvetica"))
  elif df.loc[i, "Natura del conduttore"]=='persona fisica' and df.loc[i, "Unica fonte di reddito?"]=="no":
    chunks_of_text = [
    ChunkOfText(
    " - il Sig. Marco Rossi, soggetto ", font="Helvetica"
    ),
    ChunkOfText(
    "%s" %df.loc[i, "Qualità del conduttore"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    ", è conduttore del locale commerciale sito in ", font="Helvetica"
    ),
    ChunkOfText(
    "%s," %df.loc[i, "Comune del locale"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    " nel quale esercita l'attività di ", font="Helvetica"
    ),
    ChunkOfText(
    "  %s" %df.loc[i, "Descrizione attività"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    " (codice ATECO ", font="Helvetica"
    ),
    ChunkOfText(
    "%s" %df.loc[i, "Destinazione del locale commerciale (ATECO)"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    "), ", font="Helvetica"
    ),
    ChunkOfText(
    "fonte unica del suo reddito;", font="Helvetica-Bold"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
  elif df.loc[i, "Natura del conduttore"]=='ente' and df.loc[i, "Unica fonte di reddito?"]=="no":
    chunks_of_text = [
    ChunkOfText(
    " - l'Ente Gamma, soggetto ", font="Helvetica"
    ),
    ChunkOfText(
    "%s" %df.loc[i, "Qualità del conduttore"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    ", è conduttore del locale commerciale sito in ", font="Helvetica"
    ),
    ChunkOfText(
    "%s" %df.loc[i, "Comune del locale"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    ", nel quale esercita l'attività di ", font="Helvetica"
    ),
    ChunkOfText(
    "  %s" %df.loc[i, "Descrizione attività"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    " (codice ATECO ", font="Helvetica"
    ),
    ChunkOfText(
    "%s" %df.loc[i, "Destinazione del locale commerciale (ATECO)"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    "), ", font="Helvetica"
    ),
    ChunkOfText(
    "fonte unica del suo reddito;", font="Helvetica-Bold"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - l'Ente Gamma, soggetto %s, è conduttore del locale commerciale sito in %s, nel quale esercita l'attività di %s (codice ATECO %s);" %(df.loc[i, "Qualità del conduttore"],df.loc[i, "Comune del locale"], df.loc[i, "Descrizione attività"], df.loc[i, "Destinazione del locale commerciale (ATECO)"]), font="Helvetica"))
  else:
    chunks_of_text = [
    ChunkOfText(
    " - l'Ente Gamma, soggetto ", font="Helvetica"
    ),
    ChunkOfText(
    "%s" %df.loc[i, "Qualità del conduttore"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    ", è conduttore del locale commerciale sito in ", font="Helvetica"
    ),
    ChunkOfText(
    "%s" %df.loc[i, "Comune del locale"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    ", nel quale esercita l'attività di ", font="Helvetica"
    ),
    ChunkOfText(
    "  %s" %df.loc[i, "Descrizione attività"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    " (codice ATECO ", font="Helvetica"
    ),
    ChunkOfText(
    "%s" %df.loc[i, "Destinazione del locale commerciale (ATECO)"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    "), ", font="Helvetica"
    ),
    ChunkOfText(
    "fonte unica del suo reddito;", font="Helvetica-Bold"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))


  if df.loc[i, "Natura del locatore"]=='persona fisica':
    chunks_of_text = [
    ChunkOfText(
    " - il locatore è il sig. Mario Bianchi, soggetto ", font="Helvetica"
    ),
    ChunkOfText(
    "%s" %df.loc[i, "Qualità del locatore"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    ";", font="Helvetica"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - il locatore è il sig. Mario Bianchi, soggetto %s;" %df.loc[i, "Qualità del locatore"], font="Helvetica"))
  else:
    chunks_of_text = [
    ChunkOfText(
    " - il locatore è l'Ente Alfa, soggetto ", font="Helvetica"
    ),
    ChunkOfText(
    "%s" %df.loc[i, "Qualità del locatore"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    ";", font="Helvetica"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - il locatore è l'Ente Alfa, soggetto %s;" %df.loc[i, "Qualità del locatore"], font="Helvetica"))


  value_1 = ita(df.loc[i, "Importo affitto mensile"])
  value_2 = ita(df.loc[i, "Importo pagamento del canone"])
  value_3 = df.loc[i, "Periodicità del canone"]

  chunks_of_text = [
  ChunkOfText(
  " - il contratto prevede un canone mensile di Euro ", font="Helvetica"
  ),
  ChunkOfText(
  "%s,00" %value_1, font="Helvetica-Bold"
  ),
  ChunkOfText(
  ", da corrispondersi in rate ", font="Helvetica"
  ),
  ChunkOfText(
  "%s" %value_3, font="Helvetica-Bold"
  ),
  ChunkOfText(
  " pari a Euro ", font="Helvetica"
  ),
  ChunkOfText(
  "%s,00" %value_2, font="Helvetica-Bold"
  ),
  ChunkOfText(
  ";", font="Helvetica"
  )
  ]
  layout.add(HeterogeneousParagraph(chunks_of_text))

  #layout.add(Paragraph(' - il contratto prevede un canone mensile di Euro %s,00, da corrispondersi in rate %s pari a Euro %s,00;' %(value_1, value_3, value_2), font="Helvetica"))

  if df.loc[i, "Unica fonte di reddito?"]=="si" and df.loc[i, "Qualità del conduttore"]=="privato":
    layout.add(Paragraph(" - detto canone di locazione costituisce l'unica fonte di reddito per il locatore;", font="Helvetica"))
  elif df.loc[i, "Unica fonte di reddito?"]=="no" and df.loc[i, "Qualità del conduttore"]=="privato":
    chunks_of_text = [
    ChunkOfText(
    " - detto canone di locazione costituisce il ", font="Helvetica"
    ),
    ChunkOfText(
    "%s" %df.loc[i, "Percentuale dell’affitto rispetto a reddito totale"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    "% del reddito annuale complessivo del locatore;", font="Helvetica"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - detto canone di locazione costituisce il %s%% del reddito totale del locatore;" %df.loc[i, "Percentuale dell’affitto rispetto a reddito totale"], font="Helvetica"))

  if df.loc[i, "Eventuale diritto di recesso"]=="si" and df.loc[i, "Eventuale clausola risolutiva"]=="si":
    chunks_of_text = [
    ChunkOfText(
    " - il contratto di locazione ", font="Helvetica"
    ),
    ChunkOfText(
    "prevede il diritto di recesso del conduttore", font="Helvetica-Bold"
    ),
    ChunkOfText(
    " (oltre a quello previsto dall’art. 27, comma 8, l. n. 392 del 1978), e ", font="Helvetica"
    ),
    ChunkOfText(
    " contempla, inoltre, una", font="Helvetica-Bold"
    ),
    ChunkOfText(
    " clausola risolutiva espressa, in caso di inadempimento del", font="Helvetica-Bold"
    ),
    ChunkOfText(
    " pagamento del canone;", font="Helvetica-Bold"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - il contratto di locazione prevede il diritto di recesso del conduttore (oltre a quello previsto dall’art. 27, comma 8, l. n. 392 del 1978), e contempla, inoltre, una clausola risolutiva espressa, in caso di inadempimento del pagamento del canone;", font="Helvetica"))
  elif df.loc[i, "Eventuale diritto di recesso"]=="si" and df.loc[i, "Eventuale clausola risolutiva"]=="no":
    chunks_of_text = [
    ChunkOfText(
    " - il contratto di locazione ", font="Helvetica"
    ),
    ChunkOfText(
    "prevede il diritto di recesso del conduttore", font="Helvetica-Bold"
    ),
    ChunkOfText(
    " (oltre a quello previsto dall’art. 27, comma 8, l. n. 392 del 1978), e ", font="Helvetica"
    ),
    ChunkOfText(
    " non contempla una clausola risolutiva espressa, in caso di inadempimento del", font="Helvetica-Bold"
    ),
    ChunkOfText(
    " pagamento del canone;", font="Helvetica-Bold"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - il contratto di locazione prevede il diritto di recesso del conduttore (oltre a quello previsto dall’art. 27, comma 8, l. n. 392 del 1978), e non contempla una clausola risolutiva espressa, in caso di inadempimento del pagamento del canone;", font="Helvetica"))
  elif df.loc[i, "Eventuale diritto di recesso"]=="no" and df.loc[i, "Eventuale clausola risolutiva"]=="no":
    chunks_of_text = [
    ChunkOfText(
    " - il contratto di locazione ", font="Helvetica"
    ),
    ChunkOfText(
    "non prevede il diritto di recesso del conduttore", font="Helvetica-Bold"
    ),
    ChunkOfText(
    " (oltre a quello previsto dall’art. 27, comma 8, l. n. 392 del 1978), e ", font="Helvetica"
    ),
    ChunkOfText(
    "non contempla una clausola risolutiva espressa, in caso di inadempimento del", font="Helvetica-Bold"
    ),
    ChunkOfText(
    " pagamento del canone;", font="Helvetica-Bold"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - il contratto di locazione non prevede il diritto di recesso del conduttore (oltre a quello previsto dall’art. 27, comma 8, l. n. 392 del 1978), e non contempla una clausola risolutiva espressa, in caso di inadempimento del pagamento del canone;", font="Helvetica"))
  elif df.loc[i, "Eventuale diritto di recesso"]=="no" and df.loc[i, "Eventuale clausola risolutiva"]=="si":
    chunks_of_text = [
    ChunkOfText(
    " - il contratto di locazione ", font="Helvetica"
    ),
    ChunkOfText(
    "non prevede il diritto di recesso del conduttore", font="Helvetica-Bold"
    ),
    ChunkOfText(
    " (oltre a quello previsto dall’art. 27, comma 8, l. n. 392 del 1978), e ", font="Helvetica"
    ),
    ChunkOfText(
    " contempla, inoltre, una", font="Helvetica-Bold"
    ),
    ChunkOfText(
    " clausola risolutiva espressa, in caso di inadempimento del", font="Helvetica-Bold"
    ),
    ChunkOfText(
    " pagamento del canone;", font="Helvetica-Bold"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - il contratto di locazione non prevede il diritto di recesso del conduttore (oltre a quello previsto dall’art. 27, comma 8, l. n. 392 del 1978), e contempla, inoltre, una clausola risolutiva espressa, in caso di inadempimento del pagamento del canone;", font="Helvetica"))

  if df.loc[i, "Eventuale presenza di garanzie"]=="no":
    chunks_of_text = [
    ChunkOfText(
    " - il contratto di locazione, per l’adempimento delle obbligazioni poste a carico del", font="Helvetica"
    ),
    ChunkOfText(
    " conduttore, ", font="Helvetica"
    ),
    ChunkOfText(
    "non prevede garanzie", font="Helvetica-Bold"
    ),
    ChunkOfText(
    ";", font="Helvetica"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - il contratto di locazione, per l’adempimento delle obbligazioni poste a carico del conduttore, non prevede garanzie;", font="Helvetica"))
  elif df.loc[i,"Eventuale presenza di garanzie"]=="si" and df.loc[i, "Natura delle garanzie"]=="cauzione":
    chunks_of_text = [
    ChunkOfText(
    " - il contratto di locazione, per l’adempimento delle obbligazioni poste a carico del", font="Helvetica"
    ),
    ChunkOfText(
    " conduttore, prevede una ", font="Helvetica"
    ),
    ChunkOfText(
    "%s" %df.loc[i, "Natura delle garanzie"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    " di importo pari a n. ", font="Helvetica"
    ),
    ChunkOfText(
    "%s mensilità;" %df.loc[i, "Mensilità cauzione"], font="Helvetica-Bold"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - il contratto di locazione, per l’adempimento delle obbligazioni poste a carico del conduttore, prevede una %s di importo pari a n. %s mensilità;" %(df.loc[i, "Natura delle garanzie"], df.loc[i, "Mensilità cauzione"]), font="Helvetica"))
  else:
    chunks_of_text = [
    ChunkOfText(
    " - il contratto di locazione, per l’adempimento delle obbligazioni poste a carico del", font="Helvetica"
    ),
    ChunkOfText(
    " conduttore, prevede una ", font="Helvetica"
    ),
    ChunkOfText(
    "%s" %df.loc[i, "Natura delle garanzie"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    ";", font="Helvetica"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - il contratto di locazione, per l’adempimento delle obbligazioni poste a carico del conduttore, prevede una %s;" %df.loc[i, "Natura delle garanzie"], font="Helvetica"))
  if df.loc[i, "Per quante rate si chiede la riduzione"]!="no":
    chunks_of_text = [
    ChunkOfText(
    " - a seguito della diffusione del Covid-19 e dell’applicazione delle conseguenti misure di", font="Helvetica"
    ),
    ChunkOfText(
    "contenimento adottate dall’Autorità,  ", font="Helvetica"
    ),
    ChunkOfText(
    "  il reddito del conduttore si è ridotto in %s mesi del %s%%" %(df.loc[i, "Per quante rate si chiede la riduzione"], df.loc[i, "Percentuale di perdita degli incassi rispetto al totale dei redditi del conduttore"]), font="Helvetica-Bold"
    ),
    ChunkOfText(
    ";", font="Helvetica"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - a seguito della diffusione del Covid-19 e dell’applicazione delle conseguenti misure di contenimento adottate dall’Autorità, il reddito del conduttore si è ridotto del %s%%;" %df.loc[i, "Percentuale di perdita degli incassi rispetto al totale dei redditi del conduttore"], font="Helvetica"))
  else:
    chunks_of_text = [
    ChunkOfText(
    " - a seguito della diffusione del Covid-19 e dell’applicazione delle conseguenti misure di", font="Helvetica"
    ),
    ChunkOfText(
    "contenimento adottate dall’Autorità,  ", font="Helvetica"
    ),
    ChunkOfText(
    "  il reddito del conduttore si è ridotto del %s%%" %df.loc[i, "Percentuale di perdita degli incassi rispetto al totale dei redditi del conduttore"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    ";", font="Helvetica"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))

  if df.loc[i, "Eventuali misure di sostegno"]=="si":
    value_4 = ita(df.loc[i, "Importo misure di sostegno"])
    chunks_of_text = [
    ChunkOfText(
    " - il conduttore ha, pertanto, beneficiato di ", font="Helvetica"
    ),
    ChunkOfText(
    "misure di sostegno del reddito per Euro %s,00" %value_4, font="Helvetica-Bold"
    ),
    ChunkOfText(
    ";", font="Helvetica"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - il conduttore ha, pertanto, beneficiato di misure di sostegno del reddito per Euro %s,00;" %value_4, font="Helvetica"))
  else:
    chunks_of_text = [
    ChunkOfText(
    " - il conduttore ", font="Helvetica"
    ),
    ChunkOfText(
    "non ha beneficiato di alcuna misura di sostegno del reddito", font="Helvetica-Bold"
    ),
    ChunkOfText(
    ";", font="Helvetica"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - il conduttore non ha beneficiato di alcuna misura di sostegno del reddito;", font="Helvetica"))

  if df.loc[i, "Eventuale credito d’imposta"]=="si":
    chunks_of_text = [
    ChunkOfText(
    " - il conduttore ha, infine, ottenuto - per il periodo previsto dalla normativa -  ", font="Helvetica"
    ),
    ChunkOfText(
    "un credito di imposta pari al %s%% dei ai canoni di locazione interamente versati;" %df.loc[i, "Percentuale credito d'imposta"], font="Helvetica-Bold"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - il conduttore ha, infine, ottenuto un credito di imposta pari al %s%% dei canoni di locazione versati;" %df.loc[i, "Percentuale credito d'imposta"], font="Helvetica"))
  else:
    chunks_of_text = [
    ChunkOfText(
    " - il conduttore ", font="Helvetica"
    ),
    ChunkOfText(
    "non ha ottenuto alcun credito di imposta", font="Helvetica-Bold"
    ),
    ChunkOfText(
    " rispetto ai canoni di locazione già versati;", font="Helvetica"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - il conduttore non ha ottenuto alcun credito di imposta rispetto ai canoni di locazione versati;", font="Helvetica"))

  if df.loc[i, "Quantifica riduzione richiesta?"]=="si":
    chunks_of_text = [
    ChunkOfText(
    " - in difetto di accordo tra le parti in ordine alla rinegoziazione del contratto, il conduttore", font="Helvetica"
    ),
    ChunkOfText(
    " chiede a codesta Autorità Giudiziaria ", font="Helvetica"
    ),
    ChunkOfText(
    "  la riduzione, per %s mensilità (non ancora versate), del %s%% dell’importo del canone" %(df.loc[i, "Per quante rate si chiede la riduzione"],df.loc[i, "Percentuale di riduzione richiesta rispetto al totale della rata"]), font="Helvetica-Bold"
    ),
    ChunkOfText(
    " di locazione mensile.", font="Helvetica"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - in difetto di accordo tra le parti in ordine alla rinegoziazione del contratto, il conduttore chiede a codesta Autorità Giudiziaria la riduzione del %s%% dell’importo del canone di locazione mensile." %df.loc[i, "Percentuale di riduzione richiesta rispetto al totale della rata"], font="Helvetica"))
  else:
    chunks_of_text = [
    ChunkOfText(
    " - in difetto di accordo tra le parti in ordine alla rinegoziazione del contratto, il conduttore", font="Helvetica"
    ),
    ChunkOfText(
    " chiede a codesta Autorità Giudiziaria ", font="Helvetica"
    ),
    ChunkOfText(
    "  la riduzione, per %s mensilità (non ancora versate), dell’importo del canone di locazione" %df.loc[i, "Per quante rate si chiede la riduzione"], font="Helvetica-Bold"
    ),
    ChunkOfText(
    " mensile da determinarsi in via equitativa", font="Helvetica-Bold"
    ),
    ChunkOfText(
    ".", font="Helvetica"
    )
    ]
    layout.add(HeterogeneousParagraph(chunks_of_text))
    #layout.add(Paragraph(" - in difetto di accordo tra le parti in ordine alla rinegoziazione del contratto, il conduttore chiede a codesta Autorità Giudiziaria la riduzione dell’importo del canone di locazione mensile da determinarsi in via equitativa.", font="Helvetica"))

  #layout.add(Paragraph(" ", font="Helvetica"))
  layout.add(Paragraph("P.Q.M.", font="Helvetica-Bold", text_alignment=Alignment.CENTERED))
  layout.add(Paragraph("Il Giudice, preso atto, ", font="Helvetica-Bold"))
  layout.add(DropDownList(
    possible_values=[
                    "NON DISPONE la riduzione del canone di locazione mensile",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 5%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 10%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 15%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 20%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 25%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 30%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 35%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 40%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 45%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 50%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 55%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 60%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 65%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 70%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 75%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 80%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 85%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 90%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 95%",
                    "DISPONE la riduzione del canone di locazione mensile nella misura del 100%"
                    ]
))


  page_width: Decimal = PageSize.A4_PORTRAIT.value[0]
  page_height: Decimal = PageSize.A4_PORTRAIT.value[1]
  s: Decimal = Decimal(100)
  page.append_text_annotation(Rectangle(page_width / Decimal(4) + 4*s,
                                        page_height / Decimal(4),
                                        s,
                                        s),
                              contents='Il legislatore ha previsto a favore dei soggetti che esercitano una attività di impresa misure di sostegno al reddito nella forma del contributo a fondo perduto, erogato in funzione del calo del fatturato rispetto al 2019, partendo da un minimo di Euro 1.000,00 (per le persone fisiche) o Euro 2.000,00 (per i soggetti diversi dalle persone fisiche) fino a un massimo di Euro 150.000 [per approfondimenti:  https://www.mef.gov.it/covid-19/Decreti-ristori-le-misure-a-favore-di-chi-e-in-difficolta/]',
                              text_annotation_icon=TextAnnotationIconType.COMMENT,
                              color=HexColor("f1cd2e"))
  page.append_text_annotation(Rectangle(page_width / Decimal(4) + 4*s,
                                        page_height / Decimal(4) - s/2,
                                        s,
                                        s),
                              contents='Al fine di bilanciare gli effetti negativi derivanti dalle misure di prevenzione e contenimento connesse alla emergenza sanitaria da Covid-19, il legislatore ha previsto a favore dei conduttori di immobili a uso commerciale - su istanza degli interessati e in percentuale variabile in base al calo del fatturato subito rispetto al precedente anno - un credito di imposta rispetto ai canoni di locazione versati in alcune mensilità del 2020 e del 2021 [per approfondimenti: https://www.ecnews.it/credito-dimposta-canoni-di-locazione-evoluzione-normativa/]',
                              text_annotation_icon=TextAnnotationIconType.COMMENT,
                              color=HexColor("f1cd2e"))

  with open(Path('Memoria_%s.pdf' %i), "wb") as pdf_file_handle:
    PDF.dumps(pdf_file_handle, pdf)