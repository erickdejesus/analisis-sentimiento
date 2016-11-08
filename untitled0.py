# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 18:08:31 2016

@author: edejc
"""
import pandas as pd
import func_import_catalogos as catalogs
import importar_excel as impex

print ('holamundo')

df_sentimiento,df_intensificadores,df_negadores=catalogs.Import_Catalogs()
df_negocio,df_layout1=impex.importar_excel_negocio()

ejr1=pd.merge(df_layout1,df_sentimiento,left_on='PALABRA_LIMPIA',right_on='palabra',how='left')
