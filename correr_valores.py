# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:55:16 2016

@author: AAREYESC
"""

import pandas as pd
import numpy as np
import funciones_varias as enc

def corre_valor_intensificador(x1):
    x1=enc.cambiar_formato_numero(x1)
#    pos_init=x1['POSICION'].min() 
#    pos_fin=x1['POSICION'].max()
    list_romp=x1['POSICION'][x1['ROMPEDOR_F']>0]
    list_romp=list(list_romp)
    list_intns=x1['POSICION'][x1['INTENSIFICADOR']>0]
    list_intns=list(list_intns)
    list_neg=x1['POSICION'][x1['Negadores']!=0]
    list_neg=list(list_neg)
    list_ADM=x1['POSICION'][x1['ADM']!=0]
    list_ADM=list(list_ADM)
#    val_aux=0
    if len(list_intns) > 0 and len(list_romp) > 0:
        band=0
        for i in list_romp:
            print(i)
            print(int(list_intns[0]))
            print(int(list_romp[band]))
            if int(list_intns[0]) < int(list_romp[band]):
                for j in range(int(list_intns[0]),int(list_romp[band])):
                    print(j)
                    x1.loc[x1['POSICION']>=j,'INTENSIFICADOR']=float(x1['INTENSIFICADOR'][x1['POSICION']==list_intns[0]])
                    band=band+1
            else:
                band=band+1
                continue
    if len(list_romp) == 0:
        x1.ix[x1.POSICION >= list_intns[0],'INTENSIFICADOR'] = float(x1['INTENSIFICADOR'][x1['POSICION']==list_intns[0]])
    return(x1)