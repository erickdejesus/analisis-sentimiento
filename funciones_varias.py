# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 13:12:16 2016

@author: edejc
"""

import pandas as pd


def f(row):
    try:
      if(row["PALABRA_ORIGINAL"].index('!')>0):
         return 2
    except:
        return 1
        
def encuentra_admiracion(tabla,origen):          
    tabla["ADM"] = tabla.apply(f, axis=1)
    aux = tabla[tabla['ADM'] ==2]
    index=aux.index
    for i in index:
       aux1 = tabla[(tabla['EVENT_ID_NO']==aux['EVENT_ID_NO'][i])&(tabla['POSICION']<aux['POSICION'][i])]
       index1=aux1.index
       for j in index1:
         tabla.loc[(tabla['EVENT_ID_NO']==aux1['EVENT_ID_NO'][j])&(tabla['POSICION']==aux1['POSICION'][j]) , 'ADM'] = 2 
    return (tabla)
