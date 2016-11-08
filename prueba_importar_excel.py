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
salida=[]
for i in a:
    for k in a['EVENT_ID_NO']:
        pal+=[k]
    for j in a['MENSAJE']:
        x+=j.split(' ')
#    salida+=[k,x]