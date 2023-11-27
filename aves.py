from animais import Animais

class Ave(Animais):
    def __init__(self, nome, tamanho, patas, cor, ambiente, pena):
          super().__init__(self, nome, tamanho, patas, cor, ambiente)
          self.pena=pena

    def exibir_info(self):
     super().exibir_info()
     print(f"Tipo de pena: {self.pena}")
