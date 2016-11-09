# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 18:08:31 2016

@author: edejc
"""
import pandas as pd
import func_import_catalogos as catalogs
import importar_excel as impex
import funciones_varias as enc

df_sentimiento,df_intensificadores,df_negadores,S_negation_breaks=catalogs.Import_Catalogs()
df_negocio,df_layout1=impex.importar_excel_negocio()

Layout_Sentimiento=pd.merge(df_layout1,df_sentimiento,left_on='PALABRA_LIMPIA',right_on='palabra',how='left')
Layout_ADM = enc.encuentra_admiracion(Layout_Sentimiento,df_negocio)
Layout_ADM=Layout_ADM[['EVENT_ID_NO', 'PALABRA_LIMPIA', 'PALABRA_ORIGINAL','POSICION','ADM']]
Layout_Sentimiento=Layout_Sentimiento[['EVENT_ID_NO', 'PALABRA_LIMPIA', 'PALABRA_ORIGINAL', 'POSICION','valor']]
Layout_Sentimiento=Layout_Sentimiento.fillna(0)
Layout_Sentimiento.rename(columns={'valor':'SENTIMIENTO_PALABRA'}, inplace=True)

Layout_Intensificador=pd.merge(df_layout1,df_intensificadores,left_on='PALABRA_LIMPIA',right_on='palabra',how='left')
Layout_Intensificador=Layout_Intensificador[['EVENT_ID_NO', 'PALABRA_LIMPIA', 'PALABRA_ORIGINAL', 'POSICION','valor']]
Layout_Intensificador=Layout_Intensificador.fillna(1)
Layout_Intensificador.rename(columns={'valor':'INTENSIFICADOR'}, inplace=True)

Layout_Negadores=pd.merge(df_layout1,df_negadores,left_on='PALABRA_LIMPIA',right_on='palabra',how='left')
Layout_Negadores=Layout_Negadores[['EVENT_ID_NO', 'PALABRA_LIMPIA', 'PALABRA_ORIGINAL', 'POSICION','valor']]
Layout_Negadores=Layout_Negadores.fillna(1)
Layout_Negadores.rename(columns={'valor':'Negadores'}, inplace=True)

Merg1=pd.merge(Layout_Sentimiento,Layout_Intensificador,on=['EVENT_ID_NO','PALABRA_LIMPIA','PALABRA_ORIGINAL','POSICION'],how='left')
Merg2=pd.merge(Merg1,Layout_Negadores,on=['EVENT_ID_NO','PALABRA_LIMPIA','PALABRA_ORIGINAL','POSICION'],how='left')
Merg3=pd.merge(Merg2,Layout_ADM,on=['EVENT_ID_NO','PALABRA_LIMPIA','PALABRA_ORIGINAL','POSICION'],how='left')
Merg4=enc.columna_breaks(Merg3,S_negation_breaks)

