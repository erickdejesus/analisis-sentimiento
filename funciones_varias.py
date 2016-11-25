# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 13:12:16 2016

@author: edejc
"""
import pandas as pd
import numpy as np

def f(row):
    var=0
    if(row["PALABRA_ORIGINAL"].find('!')>=0):
         var= 2
    else:
        var= 0
    return var
        
def encuentra_admiracion(tabla):          
    tabla["ADM"] = tabla.apply(f, axis=1)
    return (tabla)

#==============================================================================
#         funciones validan una cadena con la lista de rompedores    
#==============================================================================
def columna_breaks(DFrame,S_negation_breaks):
    index=DFrame.index
    new_column_values=[]
    for i in index:
##########Se crean los valores de la columna nueva
        new_column_values+=[esta_n_breaks(DFrame['PALABRA_ORIGINAL'][i],S_negation_breaks)]
    DFrame['ROMPEDOR_F']=new_column_values
    return(DFrame)
    
def esta_n_breaks(PALABRA_ORIGINAL,S_negation_breaks):
    cnt=0
    if PALABRA_ORIGINAL in list(S_negation_breaks):
        cnt=cnt+1
    else:
        for j in PALABRA_ORIGINAL:
            if j in ['y','o','ó']:
                continue
            else:
                if j in list(S_negation_breaks):
                    cnt=cnt+1
    if cnt > 0:
        return(1)
    else:
        return(0)
        
        
#==============================================================================
#         funciones para pasar una lista de Dataframes en un excel
#==============================================================================
def Salida_n_Excel(DFrame_list,Names_DFrame_list):
    band=0
    writer=pd.ExcelWriter('Salida_Ananlisis_sentimiento.xlsx',engine='xlsxwriter')
    for i in DFrame_list:
        try:
            i=cambiar_formato_numero(i.fillna(0))
        except Exception as inst:
            print('cambiar_formato_numero().'+'\t'+str(inst))
        i.to_excel(writer,sheet_name=Names_DFrame_list[band],index=False)
        workbook  = writer.book
        worksheet = writer.sheets[Names_DFrame_list[band]]
        format1 = workbook.add_format({'num_format': '#,##0.00'})
        worksheet.set_column('E:I', 18, format1)
        band=band+1
    writer.save()

    
def find_sentiment_phrase(tabla, sent):
    index=tabla.index
    sent_ind= sent.index
    tabla['MENSAJE_C'] = tabla.apply(upp, axis=1)
    EVENT=[]
    PALABRA=[]
    SENT=[]
    pib=[]
    count =0
    try:
        for i in index:
            ##########Se crean los valores de la columna nueva
            for j in sent_ind:
#            print(encuentra_palabra(tabla['MENSAJE_C'][i],sent['palabra'][j]))
                count+=1
                if(encuentra_palabra(tabla['MENSAJE_C'][i],sent['palabra'][j])>0):
                    EVENT+=[tabla['EVENT_ID_NO'][i]]
                    PALABRA+=[sent['palabra'][j]]
                    SENT+=[sent['valor'][j]]
#                    pib+=[tabla['EVENT_ID_NO'][i],sent['palabra'][j],sent['valor'][j]]
#                   print('1',pib)
    except Exception as inst:
        print('ocurrio un error',inst,count)
        print('event_i',EVENT)
        print('palabra',PALABRA)
        print('sentimiento',SENT)
        pib = {'EVENT_ID_NO':EVENT,'PALABRA':PALABRA,'SENTIMIENTO': SENT}
#    print(pib)
    tab = pd.Series(pib)
    return tab
    
def upp(row):
    return row['MENSAJE'].upper()

def encuentra_palabra(post,palabra):
    try:
        if(post.index(palabra)>0):
            return 1
    except:
        return -1
        
def cambiar_formato_numero(DFrame):
    M4_cols=DFrame.columns
    for j in M4_cols:
        if j in ['EVENT_ID_NO','PALABRA_LIMPIA','PALABRA_ORIGINAL','MENSAJE','MENSAJE_SPL']:
            continue
        else:
            try:
                DFrame[j]=DFrame[j].astype(np.float)
                DFrame[j]=pd.to_numeric(DFrame[j],errors='ignore')
            except Exception as inst:
                print('def cambiar_formato_numero():'+'\t'+str(inst))
    return(DFrame)