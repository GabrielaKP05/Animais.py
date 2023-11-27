from animais import Animais
from mamiferos import Mamifero
from aves import Ave
from peixes import Peixe

def exibir_relatorio(animais):
 if isinstance(animais, Animais):
  animais.exibir_info()
 else:
  print("Objeto não é uma instância válida de Animal.")

# Exemplos de uso:

animal1 = Animais("Leão", "Grande", 4, "Amarelo", "Savana")
exibir_relatorio(animal1)

mamifero1 = Mamifero("Golfinho", "Médio", 0, "Cinza", "Oceano", "Peixes")
exibir_relatorio(mamifero1)

ave1 = Ave("Papagaio", "Pequeno", 2, "Colorido", "Floresta", "Coloridas")
exibir_relatorio(ave1)

peixe1 = Peixe("Salmão", "Médio", 0, "Prata", "Oceano", "Especial")
exibir_relatorio(peixe1)