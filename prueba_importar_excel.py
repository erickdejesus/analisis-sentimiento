# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 17:29:12 2016

@author: AAREYESC
"""

import os
import pandas as pd
import codecs;

a=pd.read_excel('sentimiento_gal_rs.xlsx','Sheet1',enconding='latin_1')
a=a[['EVENT_ID_NO','MENSAJE']]

EVENT_ID_NO=[]
PALABRA=[]
#EVENT_ID_NO=a['EVENT_ID_NO']
band=0

def f(row):
    return row["MENSAJE"].split(' ')
a["MENSAJE_SPL"] = a.apply(f, axis=1)
salida=a[['EVENT_ID_NO','MENSAJE_SPL']]

