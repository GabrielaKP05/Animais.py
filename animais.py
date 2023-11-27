class Animais:
 def  __init__(self, nome, tamanho, patas, cor, ambiente):
      self.nome = nome
      self.tamanho = tamanho
      self.patas = patas
      self.cor = cor
      self.ambiente = ambiente


 def exibir_info(self):
         print(f"Nome: {self.nome}\\n Tamanho: {self.tamanho}\\Número de patas: {self.patas}\\n Cor{self.cor}\\nAmbiente: {self.ambiente}")