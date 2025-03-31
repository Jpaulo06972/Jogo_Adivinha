# Trabalho do jogo do adivinha.
#   Data de Entrega: 13/04/2025

# Membros:
#   . Gustavo Antônio Mariano 
#   . João Paulo Ferreira 
#   . Leonardo Gambaroni ALves 

# Biblioteca para gerar números aleatórios. 
import random 
# Biblioteca para limpar o prompt de comando. 
import os

newGame = 1 

while newGame == 1:
    # Desenvolvimento da tela de inicial.
    print()
    print("=> Bem Vindo ao Jogo do Adivinha !|! <=\n")
    print("Você tem 10 tentativas para acertar o número secreto entre [1000 e 9999]\n"
          "a partir da 5a. tentativa o jogo irá te ajudar, dando dicas \n")
    
    # Limpar o prompt de comando
    input("                                             << Tecle algo >>")     
    # Passar para cls pois é o comando para windows como estou no mac ele está com clear
    os.system("cls")
    
    # Sorteio do número a ser adivinhado.
    numSorteado = random.randint(1000,9999) 
    #numSorteado = 4895 

    # Adiciona cada digito em uma variavel para ser comparada com número digitado.
    sortDig1 = numSorteado % 10
    sortDig2 = ((numSorteado - sortDig1) % 100) // 10
    sortDig3 = ((numSorteado - (sortDig1 + sortDig2)) % 1000) // 100
    sortDig4 = ((numSorteado - (sortDig1 + sortDig2 + sortDig3)) % 10000) // 1000  

    
    # Declaração dos digitos.
    Dig1 = 0
    Dig2 = 0
    Dig3 = 0
    Dig4 = 0
    
    # Declara o contador para controlar o número de tentativas. 
    cont = 0
    fim  = 0
    
    # Auxiliar na soma de acertos, para que ele apenas contabilize os acertos daquela rodada
    aux1  = 0
    aux2  = 0
    aux3  = 0
    aux4  = 0
    
    # Gera os teste para verificar se o número é certo.
    while (cont < 10) and (fim == 0):
        
        # Valor da tentativa 
        valor = int(input("Digite sua tentativa de código: "))
        
        # Verifica se o valor digitado está dentro de 1000 e 9999.
        while valor < 1000 or valor > 9999:
            # Mensagem que o valor digitado está incorreto. 
            print("     ATENÇÃO! ! ! !\n")
            print("             Número Invalido!")
            print("             Digite um valor entre 1000 e 9999\n")
            
            input("                                             << Tecle algo >>")    
            # Passar para cls pois é o comando para windows como estou no mac ele está com clear
            os.system("cls")
            
            # Faz o usuário digitar novamente o valor.
            valor = int(input("Digite sua tentativa de código: "))
            
            
        
        # Verifica se o usuário já não acertou o código secreto
        if (numSorteado == valor):
            
            # Condição para finalizar o programa
            fim = 1
            
            # Imprime o fim do programa com a quantidade de tentativas
            print(f"=> P A R A B É N S ! ! !\n")
            print(f"Você acertou o código: {sortDig4} {sortDig3} {sortDig2} {sortDig1}")
            print(f"em {cont + 1} tentativas...\n")
            
            # Limpar o prompt de comando
            input("                                             << Tecle algo >>")    
            # Passar para cls pois é o comando para windows como estou no mac ele está com clear
            os.system("cls")
            
        # Executa se o usuário não acertou o código ainda     
        else: 

            # Adiciona cada digito da tentativa para comparar com número sorteado.
            valoDig1 = valor % 10
            valoDig2 = ((valor - valoDig1) % 100) // 10
            valoDig3 = ((valor - (valoDig1 + valoDig2)) % 1000) // 100
            valoDig4 = ((valor - (valoDig1 + valoDig2 + valoDig3)) % 10000) // 1000
        
            # Condição que verifica se ele acertou o algum número 
            if sortDig1 == valoDig1:
                
                # Se o digito for igual ao sorteado ele passa para varial que aparece na tela
                Dig1 = valoDig1
                
                # Auxiliar que roda uma vez apenas para não contabilizar os acertos das 
                # tentativas anteriores.
                if aux1 == 0:
                    aux1 = 1 
            else: 
                # Se não ele aparece apenas o traço           
                Dig1 = "_"
                
            if sortDig2 == valoDig2:
                
                # Se o digito for igual ao sorteado ele passa para varial que aparece na tela
                Dig2 = valoDig2
                
                # Auxiliar que roda uma vez apenas para não contabilizar os acertos das 
                # tentativas anteriores.
                if aux2 == 0:
                    aux2 = 1 
            else:            
                Dig2 = "_"    
                            
            if sortDig3 == valoDig3:
                
                # Se o digito for igual ao sorteado ele passa para varial que aparece na tela
                Dig3 = valoDig3
                
                # Auxiliar que roda uma vez apenas para não contabilizar os acertos das 
                # tentativas anteriores.
                if aux3 == 0:
                    aux3 = 1
            else:            
                Dig3 = "_"
                
            if sortDig4 == valoDig4:
                
                # Se o digito for igual ao sorteado ele passa para varial que aparece na tela
                Dig4 = valoDig4
                
                # Auxiliar que roda uma vez apenas para não contabilizar os acertos das 
                # tentativas anteriores.
                if aux3 == 0:
                    aux3 = 1
            else:            
                Dig4 = "_"   
            
            
            # Falta desenvolver a quantidade de acertos
            #print(f"Você acertou {} dígito(s) dessa vez...")
            
            # Verifica a quantidade de tentativas
            if cont < 5:
                print(f"Faltam {9 - cont} tentativas...")
                
            # Falta desenvolver um as dicas
            else:
                print(f"Faltam {9 - cont} tentativas...")
                print()
                
                
            # O digitos ficam invertidos por conta do processo para descobrir os digitos    
            print(f"Seu código é: {Dig4} {Dig3} {Dig2} {Dig1}\n") 
            
            # Limpar o prompt de comando
            input("                                             << Tecle algo >>") 
            # Passar para cls pois é o comando para windows como estou no mac ele está com clear
            os.system("cls")   
            
                         
                

        # Contador de tentativas    
        cont += 1




    # Condição para rodar o jogo novamente.
    newGame = int(input("Deseja jogar mais uma vez?? 1 = Sim e 0 = Não: "))
    
    # Passar para cls pois é o comando para windows como estou no mac ele está com clear
    os.system("cls")
    
    # Condição caso o valor inserido seja diferente de 1 e 0.
    while (newGame != 1) and (newGame != 0):
        newGame = int(input("Valor Inválido!! Digite apenas 1 ou 0 ->  1 = Sim e 0 = Não: "))
    


