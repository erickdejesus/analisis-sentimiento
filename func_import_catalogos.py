# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:37:18 2016

@author: AAREYESC
"""

import os
import pandas as pd
import codecs;

chncker_intens_file='intensifiers.dat'
chncker_negation_file='negations.dat'
chncker_neg_break='negationbreaks.dat'
sentmn_general='general.hsd'
dir_base=os.getcwd()+os.sep
dir_us_chucker=dir_base+'user\\chunker'+os.sep
dir_sal_sentmnt=dir_base+'user\\salience\\sentiment'+os.sep

def CorroboraExistencia(k):
    a=os.path.exists(k)
    if a == False:
        print(k,a)
    return(a)
    
def Contarexlucion(x):
    Contadorexclude=0
    for letra in x:
        if letra == '~':
            Contadorexclude=Contadorexclude + 1
    return(Contadorexclude)

def dict_tabdelim_NnameColum(nfile):
    f=codecs.open(nfile,'r',encoding='latin_1')
    palabra=[]
    valor=[]
    for i in f:
        if Contarexlucion(i) == 0:
            interm=i.split('\t')
            palabra+=[interm[0].replace('\n','').replace('\r','')]
            valor+=[interm[1].replace('\n','').replace('\r','')]
                    
    dict_salida={
                         'palabra':pd.Series(palabra),
                         'valor':pd.Series(valor)
                         }
    df_salida=pd.DataFrame(dict_salida)   
    return(df_salida)  
        
def Import_Catalogs():
    verf_archs_ruta=[]
    verf_archs_ruta=[dir_sal_sentmnt+sentmn_general,dir_us_chucker+chncker_intens_file,dir_us_chucker+chncker_negation_file,dir_base,dir_sal_sentmnt,dir_us_chucker]
    cnt_errores=0
    for k in verf_archs_ruta:
        if CorroboraExistencia(k) == False:
            cnt_errores=cnt_errores+1
    if cnt_errores == 0:
        df_sentimiento=dict_tabdelim_NnameColum(dir_sal_sentmnt+sentmn_general)
        df_intensifiers=dict_tabdelim_NnameColum(dir_us_chucker+chncker_intens_file)
        df_negation=dict_tabdelim_NnameColum(dir_us_chucker+chncker_negation_file)
        return(df_sentimiento,df_intensifiers,df_negation)
    else:
        return()


