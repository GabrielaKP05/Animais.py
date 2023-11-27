from animais import Animais

class Mamifero(Animais):
    def __init__(self, nome, tamanho, patas, cor, ambiente, alimento):
          super().__init__(self, nome, tamanho, patas, cor, ambiente)
          self.alimeto=alimento

    def exibir_info(self):
     super().exibir_info()
     print(f"Alimento: {self.alimento}")
