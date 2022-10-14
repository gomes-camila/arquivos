from collections import Counter
import matplotlib.pyplot as plt

#PORTUGUÊS

def main():
#abrir arquivo localmente
  with open("helena.txt", encoding="cp437", errors="ignore") as file:
    texto_pt = file.read().lower()
  print("Livro: Helena \nAutor: Machado de Assis \nIdioma: Português")

  grafico_letras_pt(conta_letras_pt(limpa_string_pt(texto_pt)))
  lista_letras_pt

def limpa_string_pt(par_texto_pt):
#limpando string
  letras_pt = [c for c in par_texto_pt if c.isalpha()]
  return letras_pt


def conta_letras_pt(par_letras_pt):
#criando abjeto counter
  frequencia_letras_pt = Counter(par_letras_pt)
  print (f"{len(frequencia_letras_pt)} letras únicas identificadas")
  return frequencia_letras_pt


def lista_letras_pt(par_frequencia_letras_pt):
#lista de aparição das letras
  for letra, quantidade in par_frequencia_letras_pt.most_common():
    print (f"{letra}: {quantidade}")


def grafico_letras_pt(par_frequencia_letras_pt):
#grafico das letras mais frequentes
  rotulos, valores = zip(*par_frequencia_letras_pt.most_common())
  plt.title("Frequência de letras em portugês")
  plt.ylabel("Frequência")
  plt.xlabel("Letras")
  plt.legend
  plt.bar(rotulos, valores)
  plt.show()


main()