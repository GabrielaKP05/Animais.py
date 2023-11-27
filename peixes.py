from animais import Animais

class Peixe(Animais):
    def __init__(self, nome, tamanho, patas, cor, ambiente, escama):
          super().__init__(self, nome, tamanho, patas, cor, ambiente)
          self.escama= escama

    def exibir_info(self):
     super().exibir_info()
     print(f"Tipo de escama: {self.escama}")
