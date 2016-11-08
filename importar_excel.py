# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 17:29:12 2016

@author: AAREYESC
"""

import pandas as pd

def importar_excel_negocio():
    a=pd.read_excel('sentimiento_gal_rs.xlsx','Sheet1',enconding='latin_1')
    a=a[['EVENT_ID_NO','MENSAJE','SENTIMIENTO']]
    
    def f(row):
        return row["MENSAJE"].split(' ')
    a["MENSAJE_SPL"] = a.apply(f, axis=1)
    salida1=a[['EVENT_ID_NO','MENSAJE_SPL']]
    
    EVENT_ID_NO=[]
    PALABRA_ORIGINAL=[]
    PALABRA_LIMPIA=[]
    POSICION=[]
    index=salida1.index
    long_mensaje=0
    for i in index:
        long_mensaje=len(salida1['MENSAJE_SPL'][i])
        for j in range(long_mensaje):
            EVENT_ID_NO+=[salida1['EVENT_ID_NO'][i]]
            PALABRA_ORIGINAL+=[salida1['MENSAJE_SPL'][i][j]]
            PALABRA_LIMPIA+=[salida1['MENSAJE_SPL'][i][j].strip().replace('!','').replace('¡','').replace(',','').replace('.','').replace('¿','').replace('?','').upper()]
            POSICION+=[j]
    
    dict_salida1={
                'EVENT_ID_NO':pd.Series(EVENT_ID_NO),
                'PALABRA_ORIGINAL':pd.Series(PALABRA_ORIGINAL),
                'PALABRA_LIMPIA':pd.Series(PALABRA_LIMPIA),
                'POSICION':pd.Series(POSICION)
                }
    df_salida1=pd.DataFrame(dict_salida1)
    return(a,df_salida1)