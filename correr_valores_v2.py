# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:55:16 2016

@author: AAREYESC
"""

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
    
def rompedores(intens, rompedores):
    lista=[]
    lista=intens
    lista+=rompedores
#    print(lista)
    lista=quita_duplicados(lista)
    lista = ordena_lista(lista)
    return lista
    
def ordena_lista(lis):
    tam = len(lis)
    for i in range(1,tam):
        for j in range(0,tam-i):
            if(lis[j] > lis[j+1]):
                k = lis[j+1]
                lis[j+1] = lis[j]
                lis[j] = k;
    return lis

def quita_duplicados(lis):
    lista_nueva = []
    for i in lis:
        if i not in lista_nueva:
            lista_nueva.append(i)
    return lista_nueva
    
def calcula_resultado_valor(x2):
    row_result=[]   
    for i2 in x2['POSICION']:
        result_chain=''
        ban0=''
        ban1=''
        ban2=''
        ban3=''
        result=0
        try:
            if float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2]) != 0:
                ban0='1'
            else:
                ban0='0'
            if float(x2['INTENSIFICADOR'][x2['POSICION']==i2]) != 0:
                ban1='1'
            else:
                ban1='0'
            if float(x2['Negadores'][x2['POSICION']==i2]) != 0:
                ban2='1'
            else:
                ban2='0'
            if float(x2['ADM'][x2['POSICION']==i2]) != 0:
                ban3='1'
            else:
                ban3='0'
        except Exception as msg:
            print(msg)
        result_chain=ban0+ban1+ban2+ban3
#        print(result_chain)
        if result_chain == '1000':
            result=float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2])
        elif result_chain == '1001':
            result=float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2])*float(x2['ADM'][x2['POSICION']==i2])
        elif result_chain == '1010':
            if float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2]) < 0:
                result=float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2])*float(x2['Negadores'][x2['POSICION']==i2])*(-1)
            else:
                result=float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2])*float(x2['Negadores'][x2['POSICION']==i2])
        elif result_chain == '1011':
            if float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2]) < 0:
                result=float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2])*float(x2['Negadores'][x2['POSICION']==i2])*float(x2['ADM'][x2['POSICION']==i2])*(-1)
            else:
                result=float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2])*float(x2['Negadores'][x2['POSICION']==i2])*float(x2['ADM'][x2['POSICION']==i2])
        elif result_chain == '1100':
            result=float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2])*float(x2['INTENSIFICADOR'][x2['POSICION']==i2])
        elif result_chain == '1101':
            result=float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2])*float(x2['INTENSIFICADOR'][x2['POSICION']==i2])*float(x2['ADM'][x2['POSICION']==i2])
        elif result_chain == '1110':
            if float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2]) < 0:
                result=float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2])*float(x2['INTENSIFICADOR'][x2['POSICION']==i2])*float(x2['Negadores'][x2['POSICION']==i2])*(-1)
            else:
                result=float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2])*float(x2['INTENSIFICADOR'][x2['POSICION']==i2])*float(x2['Negadores'][x2['POSICION']==i2])
        elif result_chain == '1111':
            if float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2]) < 0:
                result=float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2])*float(x2['INTENSIFICADOR'][x2['POSICION']==i2])*float(x2['Negadores'][x2['POSICION']==i2])*float(x2['ADM'][x2['POSICION']==i2])*(-1)
            else:
                result=float(x2['SENTIMIENTO_PALABRA'][x2['POSICION']==i2])*float(x2['INTENSIFICADOR'][x2['POSICION']==i2])*float(x2['Negadores'][x2['POSICION']==i2])*float(x2['ADM'][x2['POSICION']==i2])
        else:
            result=0
#        print(result)
        row_result+=[result]
    x2["row_result"]=row_result
#    print(row_result)
    return(x2)

#==============================================================================
#         FUNCIONES PRINCIPALES
#==============================================================================


def main_correr_valores(Dframe):
    Dframe_aux=Dframe
    Dframe_aux=Dframe_aux.fillna(0)
    Dframe_aux=correr_valor_intensificador(Dframe_aux)
    Dframe_aux=correr_valor_Negador(Dframe_aux)
    x2=calcula_resultado_valor(Dframe_aux)
    return(x2)
    
def correr_valor_intensificador(Dframe_aux):
    x1=Dframe_aux;x1=x1.fillna(0)
    x1=enc.cambiar_formato_numero(x1)
    list_romp=x1['POSICION'][x1['ROMPEDOR_F']>0]
    list_romp=list(list_romp)
    list_intns=x1['POSICION'][x1['INTENSIFICADOR']!=0]
    list_intns=list(list_intns)

    list_romp2=rompedores(list_intns,list_romp)
    list_romp2=list(list_romp2)
    if len(list_intns) > 0 and len(list_romp2) > 0:
        for i in list_intns:
            pos_init=0
            pos_fin=0
            CntMys=hay_mayor_q_A_en_B(i,list_romp2)
            if CntMys > 0:
                pos_init=int(i)
                pos_fin=int(siguiente_mayor_n_B(i,list_romp2))
                x1.iloc[int(pos_init):int(pos_fin)+1,5]=float(x1['INTENSIFICADOR'][x1['POSICION'] == pos_init])
            else:
                try:
                    pos_init=int(i)
                    x1.ix[x1.POSICION >= pos_init,'INTENSIFICADOR'] = float(x1['INTENSIFICADOR'][x1['POSICION'] == pos_init])
                except Exception as msg:
                    print(msg)
    elif len(list_intns) > 0 and len(list_romp2) == 0:
        if len(list_intns) == 1:
            pos_init=int(list_intns[0])
            x1.ix[x1.POSICION >= pos_init,'INTENSIFICADOR'] = float(x1['INTENSIFICADOR'][x1['POSICION'] == pos_init])
        else:
            pass
    else: 
        pass
    return(x1)
 
    
#==============================================================================
#             modficar para correr negador
#==============================================================================

def correr_valor_Negador(Dframe_aux):
    x1=Dframe_aux;x1=x1.fillna(0)
    x1=enc.cambiar_formato_numero(x1)
    list_romp=x1['POSICION'][x1['ROMPEDOR_F']>0]
    list_romp=list(list_romp)
    list_neg=x1['POSICION'][x1['Negadores']!=0]
    list_neg=list(list_neg)
    
#     CORRER Negadores
    if len(list_neg) > 0 and len(list_romp) > 0:
        for i in list_neg:
            pos_init=0
            pos_fin=0
            CntMys=hay_mayor_q_A_en_B(i,list_romp)
            if CntMys > 0:
                pos_init=int(i)
                pos_fin=int(siguiente_mayor_n_B(i,list_romp))
                x1.iloc[int(pos_init):int(pos_fin)+1,6]=-1
            else:
                pos_init=int(i)
                x1.ix[x1.POSICION >= pos_init,'Negadores'] =-1
    elif len(list_neg) > 0 and len(list_romp) == 0:
        pos_init=int(list_neg[0])
        x1.ix[x1.POSICION >= pos_init,'Negadores'] =-1
    else: 
        pass
    return(x1)
    
