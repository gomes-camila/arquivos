#Crie um programa que leia um livro no formato de texto em um idioma diferente do inglês.
#Crie o gráfico de barras com a frequência das letras nesse idioma.
#O gráfico deve conter Título, e os rótulos dos valores de cada barra.
#Opcionalmente, inclua mais um ou 2 idiomas e faça gráficos de barras múltiplos, de forma a comparar as frequências de letras nos diversos idiomas.
#O programa pode ser feito no formato de um script python (.py) ou no Google Colab.
#No caso do programa feito no Google Colab, ele deve ser feito em um arquivo novo, estar completo numa única caixa de código e ser compartilhado com o professor.
#Se for feito em um arquivo .py, deve ser colocado no github de forma pública e utilizar o poetry para a instalação dos pacotes necessários.

from collections import Counter
import matplotlib.pyplot as plt

#PORTUGUÊS

#abrir arquivo localmente
with open("helena.txt", encoding="cp437", errors="ignore") as file:
  texto_pt = file.read().lower()

print("Livro: Helena \nAutor: Machado de Assis \nIdioma: Português")

#limpando string
letras_pt = [c for c in texto_pt if c.isalpha()]

#criando abjeto counter
frequencia_letras_pt = Counter(letras_pt)

#quantidade de letras identificadas e lista de aparição das letras
print (f"{len(frequencia_letras_pt)} letras únicas identificadas")

for letra, qtde in frequencia_letras_pt.most_common():
    print (f"{letra}: {qtde}")

#grafico das letras mais frequentes
rotulos, valores = zip(*frequencia_letras_pt.most_common())
plt.title("Frequência de letras em portugês")
plt.bar(rotulos, valores)
plt.show()
