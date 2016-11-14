# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 11:15:46 2016

@author: edejc
"""
import pandas as pd

def post_un_sentimiento(tabla,total):
    aux = tabla[tabla['SENTIMIENTO_PALABRA']!=0]
    aux1= aux.groupby('EVENT_ID_NO')['SENTIMIENTO_PALABRA'].count()
    index = list(aux1.index)
    value_index=list(aux1)
    data = {'EVENT_ID_NO' : index, 
    'cont_sent_pal' : value_index}
    df = pd.DataFrame(data)
    total =pd.merge(total, df, on='EVENT_ID_NO', how='left')
    
    return df,total
    