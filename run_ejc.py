# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:51:11 2016

@author: edejc
"""

import pandas as pd
import func_import_catalogos as catalogs
import importar_excel as impex
import funciones_varias as enc
import frase_sentimiento as fr

df_sentimiento,df_intensificadores,df_negadores,S_negation_breaks=catalogs.Import_Catalogs()
df_negocio,df_layout1=impex.importar_excel_negocio()

exit1 = fr.encuentra_modificadores(df_negocio['MENSAJE_SPL'][105],df_negadores,df_sentimiento,S_negation_breaks,df_intensificadores)
#entrada,negadores,sentimiento, n_breaks, intensificadores
print (exit1)
#Layout_Sentimiento=pd.merge(df_layout1,df_sentimiento,left_on='PALABRA_LIMPIA',right_on='palabra',how='left')

#salida_pb1 = enc.find_sentiment_phrase(df_negocio,df_sentimiento)

##Layout_ADM = enc.encuentra_admiracion(Layout_Sentimiento,df_negocio)
##Layout_ADM=Layout_ADM[['EVENT_ID_NO', 'PALABRA_LIMPIA', 'PALABRA_ORIGINAL','POSICION','ADM']]
#Layout_Sentimiento=Layout_Sentimiento[['EVENT_ID_NO', 'PALABRA_LIMPIA', 'PALABRA_ORIGINAL', 'POSICION','valor']]
#Layout_Sentimiento=Layout_Sentimiento.fillna(0)
#Layout_Sentimiento.rename(columns={'valor':'SENTIMIENTO_PALABRA'}, inplace=True)
#
#Layout_Intensificador=pd.merge(df_layout1,df_intensificadores,left_on='PALABRA_LIMPIA',right_on='palabra',how='left')
#Layout_Intensificador=Layout_Intensificador[['EVENT_ID_NO', 'PALABRA_LIMPIA', 'PALABRA_ORIGINAL', 'POSICION','valor']]
#Layout_Intensificador=Layout_Intensificador.fillna(1)
#Layout_Intensificador.rename(columns={'valor':'INTENSIFICADOR'}, inplace=True)
#
#Layout_Negadores=pd.merge(df_layout1,df_negadores,left_on='PALABRA_LIMPIA',right_on='palabra',how='left')
#Layout_Negadores=Layout_Negadores[['EVENT_ID_NO', 'PALABRA_LIMPIA', 'PALABRA_ORIGINAL', 'POSICION','valor']]
#Layout_Negadores=Layout_Negadores.fillna(1)
#Layout_Negadores.rename(columns={'valor':'Negadores'}, inplace=True)
#
#Merg1=pd.merge(Layout_Sentimiento,Layout_Intensificador,on=['EVENT_ID_NO','PALABRA_LIMPIA','PALABRA_ORIGINAL','POSICION'],how='left')
#Merg2=pd.merge(Merg1,Layout_Negadores,on=['EVENT_ID_NO','PALABRA_LIMPIA','PALABRA_ORIGINAL','POSICION'],how='left')
##Merg3=pd.merge(Merg2,Layout_ADM,on=['EVENT_ID_NO','PALABRA_LIMPIA','PALABRA_ORIGINAL','POSICION'],how='left')
#Merg4=enc.columna_breaks(Merg2,S_negation_breaks)
#
#DFrame_list=[df_negocio,Merg4]
#Names_DFrame_list=['df_negocio','Merg4']
#enc.Salida_n_Excel(DFrame_list,Names_DFrame_list)