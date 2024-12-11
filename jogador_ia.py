# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            

    def getJogada(self) -> (int, int):
        lista = []
        for l in range(0,3): #percorre linha, l é a variavel que contem a linha atua do loop
            for c in range(0,3): #percorre coluna
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO: #verifica se a casa atual, com base em l e c, esta disponivel
                    lista.append((l, c))
                    
        if(len(lista) > 0): #verifica se o comprimento da lista e maior que 0
            #R1.Checar marcacoes em sequencia
            jogada = self.verifica_jogada_vertical(Tabuleiro.JOGADOR_0)
            if jogada != None:
                return jogada
            
            jogada = self.verifica_jogada_vertical(Tabuleiro.JOGADOR_X)
            if jogada != None:
                return jogada

            #R3.Se o quadrado central estiver livre, marque-o:
            if (1,1) in lista: #se a posicao central esta contida nas casas disponiveis 
                return (1,1)
            
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
            casas_disponiveis = [(coluna,0),(coluna,1),(coluna,2)]
            
            for linha in range(0,3):
                if self.matriz[linha][coluna] == tipo_jogador:
                    casas_marcadas +=1
                    item_remover = (coluna, linha)
                    casas_disponiveis = list(filter(lambda x: x != item_remover, casas_disponiveis))
                print (casas_disponiveis)
                if (casas_marcadas == 2 and Tabuleiro.DESCONHECIDO in self.matriz[linha] ):
                        jogada = casas_disponiveis[0]
                        break
        
        if jogada != None:
            return jogada
        
