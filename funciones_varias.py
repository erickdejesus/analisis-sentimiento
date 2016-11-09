# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 13:12:16 2016

@author: edejc
"""

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
    if PALABRA_ORIGINAL == 'y':
        PALABRA_ORIGINAL=PALABRA_ORIGINAL.replace('y',' y ')
    if PALABRA_ORIGINAL == 'o' or  PALABRA_ORIGINAL == 'ó':
        PALABRA_ORIGINAL=PALABRA_ORIGINAL.replace('o',' o ').replace('ó',' o ')
    cnt=0
    for j in PALABRA_ORIGINAL:
#        print(j)
        if j in list(S_negation_breaks):
            cnt=cnt+1
#            print(cnt)
    if cnt > 0:
        return(1)
    else:
        return(0)