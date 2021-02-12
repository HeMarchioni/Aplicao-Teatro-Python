# -*- coding: utf-8 -*-
"""
Created on Mon May 11 00:47:17 2020

@author: Henrique Marchioni
**Classe Teatro
"""


class Teatro:
    def __init__(self):
        pass
        
    
    def valido (self,digito):
        while True:
            try:
                self.d=int(digito)
                if self.d<=0:
                    raise 
            except:
                print('\n Valor não Valido !! \n')
                digito=(input('digite um numero Valido :'))
            else:
                return self.d
                break
    
    
    def dicionario_res (self,v1,v2):
        self.value=[self.chave ,'fileira:',v1, 'cadeira',v2]
        
        
    def dicionario_canc (self,v1,v2):
        self.value=['fileira:',v1, 'cadeira',v2]
        for self.x in self.dic.values():
           if self.value in self.x:
               self.chave=self.x[0][0]
    
    
    def nome (self):
        self.name=self.name.title()
        self.name=self.name.strip()
        self.chave=self.name
    
    
    def teatro (self,fileira,cadeira):   
        self.f=fileira
        self.c=cadeira
        self.total=self.f*self.c
        self.disponivel=self.total
        self.dic={}
        
        self.matriz=[]
        for i in range(fileira):
            self.fileira1=[]
            for i in range(cadeira):
                self.fileira1.append('Vago')
            self.matriz.append(self.fileira1)    
    
   
    def reserva (self,escolhafil,escolhacad):
        self.proximo = 0
        while True:
           try:    
               if  "Ocupado" in self.matriz [escolhafil-1] [escolhacad-1]:
                   print("\n Este local Já esta Ocupado, Operação invalida !!! \n")
                   break
           except IndexError:
               print('valor fora do range fileira ou cadeira inexistente')        
               self.fil=(input('Digite um numero de Fileira existente: '))
               escolhafil=self.valido(self.fil)
               self.cad=(input('Digite um numero de Cadeira existente: '))
               escolhacad=self.valido(self.cad)
           else:   
                   self.matriz [escolhafil-1] [escolhacad-1] = "Ocupado"
                   self.disponivel-=1
                   self.name=(input('Digite o nome do cliente que fez a reserva: '))
                   self.nome()
                   self.dicionario_res(escolhafil,escolhacad)
                   self.dic[self.chave]=self.value
                   print("\n RESERVA EXECUTADA !! \n")
                   self.proximo = 1
                   break
    
   
    def cancela (self,escolhafil,escolhacad):
        self.proximo = 0
        while True:
           try: 
               if "Vago" in self.matriz [escolhafil-1] [escolhacad-1]:
                   print("\n Este local já esta Vago, Operação invalida !!!")
                   break
           except IndexError:
               print('valor fora do range fileira ou cadeira inexistente')        
               self.fil=(input('Digite um numero de Fileira existente: '))
               escolhafil=self.valido(self.fil)
               self.cad=(input('Digite um numero de Cadeira existente: '))
               escolhacad=self.valido(self.cad)             
        
           else:
               self.dicionario_canc(escolhafil,escolhacad)
               print("Deseja cancelar a reserva de:",self.dic[self.chave]," S / N ? ")
               self.apaga=(input(": "))
               if 'S' in (self.apaga.upper()):
                   self.matriz [escolhafil-1] [escolhacad-1] = "Vago"
                   self.disponivel+=1
                   self.dic.pop(self.chave)
                   print("\n RESERVA CANCELADA !! \n")
                   self.proximo = 1
                   break
               elif 'N' in (self.apaga.upper()):
                   print (" \n Reserva Mantida !!!")
                   break
               else:
                   print ("\n Não Valido tente Novamente !!!")    
                   
    
    def busca(self,nm):
        self.name=str(nm)
        self.nome()
        return self.dic.get(self.chave)
    
    
    def reset (self,reset):
        if 'S' in (reset.upper()):
            self.teatro(self.f,self.c)
            print (" \n CONTROLE RESETADO !!!")
        elif 'N' in (reset.upper()):
            print (" \n Reset Cancelado !!!")
        else:
            print ("\n Não Valido tente Novamente !!!")
    
    
    def getProximo (self):
        return self.proximo
    
    def getMatriz (self):
        return self.matriz
      
        
#parte Exibir a matriz com os lugares vagos ou ocupados
   
    def exibeMatriz(self):
        for fileiras in range(len(self.matriz)):
            print("\nFILEIRA",fileiras+1)
            for cadeiras in range(len(self.matriz[0])):
                print("Cadeira",cadeiras+1,'(',
                self.matriz[fileiras][cadeiras],')',end="  /  ")
            print('\n')
        
        print('\nCapacitade Maxima: ',self.total,'Lugares')
        print('Lugares Disponiveis: ',self.disponivel,'\n')
            