# -*- coding: utf-8 -*-
"""
Created on Mon May 11 00:47:25 2020

@author: Henrique Marchioni
** Aplicação
"""


import teatro

#=== menu inicial ==========================================================================================
fileira=0
cadeira=0
menuinicial=0
while menuinicial!=3:

    print('''   \n     ===== Teatro menu inicial ======
        [1] inserir dados sobre as caracteristicas do teatro.
        [2] Iniciar o programa de controle de reservas.
        [3] Finalizar Programa
        
        ''')
   
    try:
        menuinicial=int(input("\n Digite sua opçaão :  "))
    except:
        print('\n Digite um numero Valido !! \n')
        
    else:
  
        if menuinicial==1:
            t= teatro.Teatro()
            fileira=(input("digite o numero de Fileiras que contem nesse estabelecimento :"))
            fileira=t.valido(fileira)
            cadeira=(input("digite o numero de Cadeiras que contem em cada fileira :"))
            cadeira=t.valido(cadeira)
            t.teatro(fileira,cadeira)
            continue

# menu controle de reserva================================================================================
        elif menuinicial==2 and (fileira or cadeira !=0):
            menucontrole=0
            while menucontrole!=6:
                t.exibeMatriz()
                print(''' \n  ======= Teatro Controle de Reservas =====
                  [1] Fazer uma reserva
                  [2] Cancelar uma reserva
                  [3] Trocar uma reserva
                  [4] Buscar reserva pelo nome do Cliente
                  [5] Resetar Controle de Reserva
                  [6] Finalizar programa de controle de reservas
                  ''')
                try:
                    menucontrole=int(input("\n Digite sua opçaão : "))
                except:
                    print('\n Digite um numero Valido !! \n')
                else:
            #==fazer reserva==================================================================
                    if menucontrole==1:
                        print("\n escolha um assento vago \n")
                        escolhafil=(input("Digite o numero da Fileira desejada : "))
                        escolhafil=t.valido(escolhafil)
                        escolhacad=(input("Digite o numero do assento desejado : "))
                        escolhacad=t.valido(escolhacad)
                        t.reserva(escolhafil,escolhacad)
            
            #==cancelar reserva========================================================
                    elif menucontrole==2:
                        print("\n escolha o assento a qual a reserva ira ser cancelada \n")
                        escolhafil=(input("Digite o numero da Fileira desejada : "))
                        escolhafil=t.valido(escolhafil)
                        escolhacad=(input("Digite o numero do assento desejado : "))
                        escolhacad=t.valido(escolhacad)
                        t.cancela(escolhafil,escolhacad)    
            
            #==trocar reserva========================================================
                    elif menucontrole==3:
                        print("\n Trocar a Reserva \n")
                        escolhafil=(input("Digite o numero da Fileira que esta reservada agora : "))
                        escolhafil=t.valido(escolhafil)
                        escolhacad=(input("Digite o numero do assento que esta reservado agora : "))
                        escolhacad=t.valido(escolhacad)
                        t.cancela(escolhafil,escolhacad)
               
                        if t.getProximo() == 1:
                            escolhafil=(input("Digite o numero da Fileira que deseja ocupar : "))
                            escolhafil=t.valido(escolhafil)
                            escolhacad=(input("Digite o numero do assento que deseja ocupar  : "))                                
                            escolhacad=t.valido(escolhacad)
                            t.reserva(escolhafil,escolhacad)
                
                            if t.getProximo() == 1:
                                print("\n SUA RESERVA FOI TROCADA COM SUCESSO !!\n")
                
                
             #==Buscar reserva pelo nome do cliente==================================================     
                    elif menucontrole==4:
                       nome=(input("Digite o nome do Cliente para busca:"))
                       if None == t.busca(nome):
                           print('''\nCliente não possui Reserva !!!
        Por favor digite o nome completo do Cliente para uma busca correta !!!''')
                       else:
                           print('\nReserva',t.busca(nome))
                
                
            #==resetar controle de reserva================================================   
                    elif menucontrole==5:    
                        reset=str(input("\n tem certeza que deseja resetar o contole S / N ?: "))
                        t.reset(reset)
                
                    elif menucontrole <= 0 or menucontrole > 6:
                        print('\n Digite um numero Valido !! \n')

#================================================================================================                
                
        elif menuinicial==3:
            print('Finalizando Programa!!')
        
        elif (fileira or cadeira ==0) and menuinicial==2:
            print("\n É necessario primeiro inserir as caracteristicas do teatro !!!  \n")       
    
        else:
             print('\n Digite um numero Valido !! \n')