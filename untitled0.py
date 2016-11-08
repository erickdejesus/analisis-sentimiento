# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 18:08:31 2016

@author: edejc
"""
import pandas as pd
import func_import_catalogos as catalogs
import importar_excel as impex
import funciones_varias as enc



print ('Inicia proceso')

df_sentimiento,df_intensificadores,df_negadores,df_negationbreaks=catalogs.Import_Catalogs()
df_negocio,df_layout1=impex.importar_excel_negocio()

ejr1=pd.merge(df_layout1,df_sentimiento,left_on='PALABRA_LIMPIA',right_on='palabra',how='left')
ejr2 = enc.encuentra_admiracion(ejr1,df_negocio)

   
   