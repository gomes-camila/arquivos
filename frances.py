from collections import Counter
import matplotlib.pyplot as plt

#FRANCÊS

def main():
#abrir arquivo localmente
  with open("les_miserables.txt", encoding="cp437", errors="ignore") as file:
    texto_fr = file.read().lower()
  print("Livro: Les Misérables \nAutor: Victor Hugo \nIdioma: Francês")

  grafico_letras_fr(conta_letras_fr(limpa_string_fr(texto_fr)))


def limpa_string_fr(par_texto_fr):
#limpando string
  letras_fr = [c for c in par_texto_fr if c.isalpha()]
  return letras_fr


def conta_letras_fr(par_letras_fr):
#criando abjeto counter
  frequencia_letras_fr = Counter(par_letras_fr)
  print (f"{len(frequencia_letras_fr)} letras únicas identificadas")
  return frequencia_letras_fr


def lista_letras_fr(par_frequencia_letras_fr):
#lista de aparição das letras
  for letra, qtde in par_frequencia_letras_fr.most_common():
    print (f"{letra}: {qtde}")

def grafico_letras_fr(par_frequencia_letras_fr):
#grafico das letras mais frequentes
  rotulos, valores = zip(*par_frequencia_letras_fr.most_common())
  plt.title("Frequência de letras em francês")
  plt.bar(rotulos, valores)
  plt.show()

main()