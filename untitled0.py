# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 18:08:31 2016

@author: edejc
"""
import pandas as pd
import func_import_catalogos as catalogs
import importar_excel as impex
import funciones_varias as enc
import consultas as consulta
import correr_valores_v2 as correr
import os

os.environ['NLS_LANG'] ='.UTF8'
os.remove('TStage2.csv');os.remove('Salida_Ananlisis_sentimiento.xlsx')

df_sentimiento,df_intensificadores,df_negadores,S_negation_breaks=catalogs.Import_Catalogs()
df_negocio,df_layout1=impex.importar_excel_negocio()

Layout_Sentimiento=pd.merge(df_layout1,df_sentimiento,left_on='PALABRA_LIMPIA',right_on='palabra',how='left')
Layout_ADM = enc.encuentra_admiracion(Layout_Sentimiento)
Layout_ADM=Layout_ADM[['EVENT_ID_NO', 'PALABRA_LIMPIA', 'PALABRA_ORIGINAL','POSICION','ADM']]
Layout_Sentimiento=Layout_Sentimiento[['EVENT_ID_NO', 'PALABRA_LIMPIA', 'PALABRA_ORIGINAL', 'POSICION','valor']]
Layout_Sentimiento=Layout_Sentimiento.fillna(0)
Layout_Sentimiento.rename(columns={'valor':'SENTIMIENTO_PALABRA'}, inplace=True)

Layout_Intensificador=pd.merge(df_layout1,df_intensificadores,left_on='PALABRA_LIMPIA',right_on='palabra',how='left')
Layout_Intensificador=Layout_Intensificador[['EVENT_ID_NO', 'PALABRA_LIMPIA', 'PALABRA_ORIGINAL', 'POSICION','valor']]
Layout_Intensificador=Layout_Intensificador.fillna(0)
Layout_Intensificador.rename(columns={'valor':'INTENSIFICADOR'}, inplace=True)

Layout_Negadores=pd.merge(df_layout1,df_negadores,left_on='PALABRA_LIMPIA',right_on='palabra',how='left')
Layout_Negadores=Layout_Negadores[['EVENT_ID_NO', 'PALABRA_LIMPIA', 'PALABRA_ORIGINAL', 'POSICION','valor']]
Layout_Negadores=Layout_Negadores.fillna(0)
Layout_Negadores.rename(columns={'valor':'Negadores'}, inplace=True)

Merg1=pd.merge(Layout_Sentimiento,Layout_Intensificador,on=['EVENT_ID_NO','PALABRA_LIMPIA','PALABRA_ORIGINAL','POSICION'],how='left')
Merg2=pd.merge(Merg1,Layout_Negadores,on=['EVENT_ID_NO','PALABRA_LIMPIA','PALABRA_ORIGINAL','POSICION'],how='left')
Merg3=pd.merge(Merg2,Layout_ADM,on=['EVENT_ID_NO','PALABRA_LIMPIA','PALABRA_ORIGINAL','POSICION'],how='left');Merg3=Merg3.fillna(0)
Merg4=enc.columna_breaks(Merg3,S_negation_breaks);Merg4=Merg4.fillna(0)

clasificacion,df_negocio = consulta.post_un_sentimiento(Merg4,df_negocio)
df_negocio=df_negocio.fillna(0)

with open('TStage2.csv','a') as appn:
    new_index=list(df_negocio['EVENT_ID_NO'][df_negocio['cont_sent_pal']==1])
    band=0
    for m in new_index:
        m5=Merg4[Merg4['EVENT_ID_NO']==m]
        m5=m5.fillna(0)
        x2=correr.main_correr_valores(m5)
        if band==0:
            try:
                x2.to_csv(appn,index=False,enconding='latin_1')
            except Exception as inst:
                print(str(m)+': '+str(inst))
            band=band+1
        else:
            try:
                x2.to_csv(appn,header=False,index=False,enconding='latin_1')
            except Exception as inst:
                print(str(m)+': '+str(inst)) 
            band=band+1

Merg5=pd.read_csv('TStage2.csv',encoding='latin_1')
Merg5=Merg5.drop_duplicates()
Merg5=Merg5.reindex()
            
#==============================================================================
#          SALIDA EN FORMATO EXCEL
#==============================================================================
DFrame_list=[df_negocio,Merg4,Merg5]
Names_DFrame_list=['df_negocio','Merg4','Merg5']
enc.Salida_n_Excel(DFrame_list,Names_DFrame_list)

