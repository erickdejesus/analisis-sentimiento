# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 11:15:46 2016

@author: edejc
"""
import pandas as pd

def post_un_sentimiento(tabla,total):
    aux = tabla[tabla['SENTIMIENTO_PALABRA']!=0]
    aux1 = aux.groupby('EVENT_ID_NO')['SENTIMIENTO_PALABRA'].count()
#    print(aux1)
#    for k in aux1:
        
#    ase = pd.Series(aux1.values)
#    aux1=aux.merge(total, aux, on='EVENT_ID_NO', how='left')
#    aux[aux['SENTIMIENTO_PALABRA']==1]
    
    return aux1
    