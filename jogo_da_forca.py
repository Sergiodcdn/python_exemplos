# JOGO DA FORCA - usando POO
import random

# Palco da Forca
palco = ['', 'O', 'O-', 'O-|', 'O-|-', 'O-|-<']


# Classe
class Forca:
    # Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_certas = []
        
    # Método para adivinhar a letra
    def adivinha(self, letra):
        if letra in self.palavra and letra not in self.letras_certas:
            self.letras_certas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True
    
    # Método para verificar se o jogo acabou
    def forca_acabou(self):
        if self.forca_venceu() or (len(self.letras_erradas) >= 5):
            return True
        return False
        
    # Método para verificar se o jogador venceu
    def forca_venceu(self):
        if '_' not in self.palavra_escondida():
            return True
        return False
        
    # Método para não mostrar a letra no palco
    def palavra_escondida(self):
        status = ''
        for letra in self.palavra:
            if letra not in self.letras_certas:
                status += '_'
            else:
                status += letra
        return status
        
    # Método para checar o status do jogo e imprimir o palco na tela
    def mostra_status_jogo(self):
        print(f'\n======= Jogo da Forca =======')
        print(palco[len(self.letras_erradas)])
        print(f'Palavra: {self.palavra_escondida()}')
        print(f'\nLetras erradas: ')
        for letra in self.letras_erradas:
            print(letra,)
        print(f'\nLetras Corretas: ')
        for letra in self.letras_certas:
            print(letra,)
            

# Função para ler uma palavra de forma aleatória do banco de palavras
def palavra_aleatoria():
    with open("palavra.txt", "rt") as f:
        banco = f.readlines()
    return banco[random.randint(0, len(banco))].strip()

            
# Função Main - Execução do Programa
def main():
    # Objeto
    jogo = Forca(palavra_aleatoria())
    
    # Enquanto o jogo não tiver terminado, mostrar do status,
    # solicitar uma letra e faz a leitura do caracter
    while not jogo.forca_acabou():
        jogo.mostra_status_jogo()
        letra_escolhida = input(f'\nDigite uma letra: ')
        jogo.adivinha(letra_escolhida)
    
    # Verifica o status do jogo
    jogo.mostra_status_jogo()
    
    # De acordo com o status, 
    if jogo.forca_venceu():
        print(f'\nParabéns! Você venceu!')
    else:
        print(f'Final do Jogo! YOU LOOSE!')
        print('A palavra era ' + jogo.palavra)
        
    print(f'\nFoi bom te ter no Mortal Kombat!\n Ops... no jogo da forca... Foi bom jogar com vc!')
    
    
# Executa o programa
if __name__ == "__main__":
    main()