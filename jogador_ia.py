# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            

    def getJogada(self) -> (int, int):
        lista = []
        for l in range(0,3): #percorre linha, l é a variavel que contem a linha atual do loop
            for c in range(0,3): #percorre coluna
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO: #verifica se a casa atual, com base em l e c, esta disponivel
                    lista.append((l, c))
                    
        if(len(lista) > 0): #verifica se o comprimento da lista e maior que 0
            #R1.Checar marcacoes em sequencia e marcar o quadrado restante
            jogada = self.verifica_jogada_vertical(Tabuleiro.JOGADOR_0)
            if jogada != None:
                return jogada
            
            jogada = self.verifica_jogada_vertical(Tabuleiro.JOGADOR_X)
            if jogada != None:
                return jogada
            
            jogada = self.verifica_jogada_horizontal(Tabuleiro.JOGADOR_0)
            if jogada != None:
                return jogada
            
            jogada = self.verifica_jogada_horizontal(Tabuleiro.JOGADOR_X)
            if jogada != None:
                return jogada
            
            jogada = self.verifica_jogada_diagonal(Tabuleiro.JOGADOR_0)
            if jogada != None:
                return jogada
            
            jogada = self.verifica_jogada_diagonal(Tabuleiro.JOGADOR_X)
            if jogada != None:
                return jogada

            #R2.Se houver uma jogada que crie duas sequencias de marcacoes

            #R3.Se o quadrado central estiver livre, marque-o:
            if (1,1) in lista: #se a posicao central esta contida nas casas disponiveis 
               return (1,1)
            
            #R4.Se o jogador tiver marcado um dos cantos marcar o canto oposto

            #R5.Se houver um canto vazio marcar

            #R6.Marcar arbitrariamente um canto vazio
            
            p = randint(0, len(lista)-1)
            return lista[p]
        else:
           return None
        
    def verifica_jogada_horizontal(self, tipo_jogador):
        jogada = None

        for linha in range(0,3):
            casas_marcadas = 0
            casas_disponiveis = [(linha,0),(linha,1),(linha,2)]
            
            for coluna in range(0,3):
                if self.matriz[linha][coluna] == tipo_jogador:
                    casas_marcadas +=1
                    item_remover = (linha, coluna)
                    casas_disponiveis = list(filter(lambda x: x != item_remover, casas_disponiveis))

                if (casas_marcadas == 2 and Tabuleiro.DESCONHECIDO in self.matriz[linha] ):
                        jogada = casas_disponiveis[0]
                        break
        
        if jogada != None:
            return jogada
        
    def verifica_jogada_vertical(self, tipo_jogador):
        jogada = None

        for coluna in range(0,3):
            casas_marcadas = 0
            casas_disponiveis = [(0, coluna),(1, coluna),(2, coluna)]
            
            for linha in range(0,3):
                if self.matriz[linha][coluna] == tipo_jogador:
                    casas_marcadas +=1
                    item_remover = (linha, coluna)
                    casas_disponiveis = list(filter(lambda x: x != item_remover, casas_disponiveis))
                
                print (casas_disponiveis)
                
                #Verifica se tem duas casas marcadas e uma disponivel na coluna
                if (casas_marcadas == 2 and Tabuleiro.DESCONHECIDO in [self.matriz[coluna] for i in range(0,3)] ):
                        jogada = casas_disponiveis[0]
                        break
        
        if jogada != None:
            return jogada
        
    def verifica_jogada_diagonal(self, tipo_jogador):
        #Verificando a diagonal principal
        casas_marcadas = 0
        casas_disponiveis = [(0,0), (1,1), (2,2)]
        for i in range(0,3):
            if self.matriz[i][i] == tipo_jogador:
                casas_marcadas +=1
                casas_disponiveis.remove((i, i))
        if casas_marcadas == 2 and any(self.matriz[i][i] == Tabuleiro.DESCONHECIDO for i in range(0,3)):
            return casas_disponiveis[0]
        
        # Diagonal secundária
        casas_marcadas = 0
        casas_disponiveis = [(0, 2), (1, 1), (2, 0)]
        for i in range(3):
            if self.matriz[i][2 - i] == tipo_jogador:
                casas_marcadas += 1
                casas_disponiveis.remove((i, 2 - i))
        if casas_marcadas == 2 and any(self.matriz[i][2 - i] == Tabuleiro.DESCONHECIDO for i in range(3)):
            return casas_disponiveis[0]

        return None
        
