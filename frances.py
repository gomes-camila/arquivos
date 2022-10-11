from collections import Counter
import matplotlib.pyplot as plt

#FRANCÊS

#abrir arquivo localmente
with open("les_miserables.txt", encoding="cp437", errors="ignore") as file:
  texto_fr = file.read().lower()

print("Livro: Les Misérables \nAutor: Victor Hugo \nIdioma: Francês")

#limpando string
letras_fr = [c for c in texto_fr if c.isalpha()]

#criando abjeto counter
frequencia_letras_fr = Counter(letras_fr)

#quantidade de letras identificadas
print (f"{len(frequencia_letras_fr)} letras únicas identificadas")

#lista de aparição das letras
for letra, qtde in frequencia_letras_fr.most_common():
    print (f"{letra}: {qtde}")

#grafico das letras mais frequentes
rotulos, valores = zip(*frequencia_letras_fr.most_common())
plt.title("Frequência de letras em francês")
plt.bar(rotulos, valores)
plt.show()
