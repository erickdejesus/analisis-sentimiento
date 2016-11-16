# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:55:16 2016

@author: AAREYESC
"""

import pandas as pd
import numpy as np
import funciones_varias as enc

#==============================================================================
#     FUNCIONES DE AYUDA
#==============================================================================
def hay_mayor_q_A_en_B(valorX,list_romp):
    cnt=0
    for i in list_romp:
        if i > valorX:
            cnt=cnt+1
    return(int(cnt))
    
def siguiente_mayor_n_B(valorX,list_romp):
    valsM=[]
    for i in list_romp:
        if i > valorX:
            valsM+=[i]
    return(int(valsM[0]))
        
def hay_menor_q_A_en_B(valorX,list_romp):
    cnt=0
    for i in list_romp:
        if i < valorX:
            cnt=cnt+1
    return(int(cnt))
    
def siguiente_menor_n_B(valorX,list_romp):
    valsM=[]
    for i in list_romp:
        if i < valorX:
            valsM+=[i]
    return(valsM[len(valsM)-1])
    
#==============================================================================
#         FUNCION PRINCIPAL
#==============================================================================

def correr_valor_multiplicador(x1):
    x1=enc.cambiar_formato_numero(x1)
    list_romp=x1['POSICION'][x1['ROMPEDOR_F']>0]
    list_romp=list(list_romp)
    list_intns=x1['POSICION'][x1['INTENSIFICADOR']>0]
    list_intns=list(list_intns)
    list_neg=x1['POSICION'][x1['Negadores']!=0]
    list_neg=list(list_neg)
    list_ADM=x1['POSICION'][x1['ADM']!=0]
    list_ADM=list(list_ADM)
    
#     CORRER INTENSIFICADORES

    if len(list_intns) > 0 and len(list_romp) > 0:
        for i in list_intns:
            CntMys=hay_mayor_q_A_en_B(i,list_romp)
            if CntMys > 0:
                pos_init=int(i)
                pos_fin=siguiente_mayor_n_B(i,list_romp)
                x1.iloc[int(pos_init):int(pos_fin)+1,5]=float(x1['INTENSIFICADOR'][x1['POSICION'] == pos_init])
            else:
                pos_init=int(i)
                x1.ix[x1.POSICION >= pos_init,'INTENSIFICADOR'] = float(x1['INTENSIFICADOR'][x1['POSICION'] == pos_init])
    elif len(list_intns) > 0 and len(list_romp) == 0:
        if len(list_intns) == 1:
            pos_init=int(list_intns[0])
            x1.ix[x1.POSICION >= pos_init,'INTENSIFICADOR'] = float(x1['INTENSIFICADOR'][x1['POSICION'] == pos_init])
        else:
            for i in list_intns:
                pos_init=int(i)
                x1.ix[x1.POSICION >= pos_init,'INTENSIFICADOR'] = float(x1['INTENSIFICADOR'][x1['POSICION'] == pos_init])
    else: 
        pass

#     CORRER SIGNOS DE ADMIRACION!

    if len(list_ADM) > 0 and len(list_romp) > 0:
        for i in list_ADM:
            CntMns=hay_menor_q_A_en_B(i,list_romp)
            if CntMns > 0:
                pos_init=siguiente_menor_n_B(i,list_romp)
                pos_fin=int(i)
                x1.iloc[int(pos_init):int(pos_fin),7]=float(x1['ADM'][x1['POSICION'] == pos_fin])
            else:
                pos_init=0
                pos_fin=int(i)
                x1.iloc[int(pos_init):int(pos_fin),7]=float(x1['ADM'][x1['POSICION'] == pos_fin])
    elif len(list_ADM) > 0 and len(list_romp) == 0:
        if len(list_intns) == 1:
            pos_init=0
            pos_fin=int(list_ADM[0])
            x1.iloc[int(pos_init):int(pos_fin),7]=float(x1['ADM'][x1['POSICION'] == pos_fin])
        else:
#                hay que trabajar en este caso
             pos_init=0
             pos_fin=int(i)
             x1.iloc[int(pos_init):int(pos_fin),7]=float(x1['ADM'][x1['POSICION'] == pos_fin])
    else:
        pass
    
#     CORRER Negadores
    
    if len(list_neg) > 0 and len(list_romp) > 0:
        for i in list_neg:
            CntMys=hay_mayor_q_A_en_B(i,list_romp)
            if CntMys > 0:
                pos_init=int(i)
                pos_fin=siguiente_mayor_n_B(i,list_romp)
                x1.iloc[int(pos_init):int(pos_fin)+1,6]=float(x1['Negadores'][x1['POSICION'] == pos_init])
            else:
                pos_init=int(i)
                x1.ix[x1.POSICION >= pos_init,'Negadores'] = float(x1['Negadores'][x1['POSICION'] == pos_init])
    elif len(list_neg) > 0 and len(list_romp) == 0:
        if len(list_neg) == 1:
            pos_init=int(list_neg[0])
            x1.ix[x1.POSICION >= pos_init,'Negadores'] = float(x1['Negadores'][x1['POSICION'] == pos_init])
        else:
            for i in list_neg:
                pos_init=int(i)
                x1.ix[x1.POSICION >= pos_init,'Negadores'] = float(x1['Negadores'][x1['POSICION'] == pos_init])
    else: 
        pass
    
#    Calculo de columna RESULTADO_DESMENUZADO

    return(x1)
    
