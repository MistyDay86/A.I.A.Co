from collections import OrderedDict
from PyPDF2 import PdfFileWriter, PdfFileReader
import os

n_sent = 1000

def _getFields(obj, tree=None, retval=None, fileobj=None):
    fieldAttributes = {'/FT': 'Field Type', '/Parent': 'Parent', '/T': 'Field Name', '/TU': 'Alternate Field Name',
                       '/TM': 'Mapping Name', '/Ff': 'Field Flags', '/V': 'Value', '/DV': 'Default Value'}
    if retval is None:
        retval = OrderedDict()
        catalog = obj.trailer["/Root"]
        # get the AcroForm tree
        if "/AcroForm" in catalog:
            tree = catalog["/AcroForm"]
        else:
            return None
    if tree is None:
        return retval

    obj._check_kids(tree, retval, fileobj)
    for attr in fieldAttributes:
        if attr in tree:
            # Tree is a field
            obj._build_field(tree, retval, fileobj, fieldAttributes)
            break

    if "/Fields" in tree:
        fields = tree["/Fields"]
        for f in fields:
            field = f.getObject()
            obj._build_field(field, retval, fileobj, fieldAttributes)

    return retval


def get_form_fields(infile):
    infile = PdfFileReader(open(infile, 'rb'))
    fields = _getFields(infile)
    return OrderedDict((k, v.get('/V', '')) for k, v in fields.items())



if __name__ == '__main__':
  from pprint import pprint
  label_0 = [None]*n_sent
  for i in range(n_sent):
    pdf_file_name = 'Memoria_%s.pdf' %i
    if os.path.exists(pdf_file_name) and i!=421:
      print(i)
      if get_form_fields(pdf_file_name)['Field 1']=="NON DISPONE la riduzione del canone di locazione mensile":
        label_0[i]=0
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 5%":
        label_0[i]=0.05
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 10%":
        label_0[i]=0.1
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 15%":
        label_0[i]=0.15
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 20%":
        label_0[i]=0.20
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 25%":
        label_0[i]=0.25
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 30%":
        label_0[i]=0.30
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 35%":
        label_0[i]=0.35
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 40%":
        label_0[i]=0.40
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 45%":
        label_0[i]=0.45
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 50%":
        label_0[i]=0.50
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 55%":
        label_0[i]=0.55
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 60%":
        label_0[i]=0.60
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 65%":
        label_0[i]=0.65
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 70%":
        label_0[i]=0.70
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 75%":
        label_0[i]=0.75
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 80%":
        label_0[i]=0.80
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 85%":
        label_0[i]=0.85
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 90%":
        label_0[i]=0.90
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 95%":
        label_0[i]=0.95
      elif get_form_fields(pdf_file_name)['Field 1']=="DISPONE la riduzione del canone di locazione mensile nella misura del 100%":
        label_0[i]=1

    df = pd.read_excel('Sentenze_Random.xlsx')
    df["Sentenza"] = label_0
    df.to_excel('Sentenze_Random_Labelled.xlsx')