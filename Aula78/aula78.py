# Aula 78
# * Sets - Conjuntos em Python (tipo set)
# * Conjuntos são ensinados na matemática
# * Representados graficamente pelo diagrama de Venn
# * Sets em Python são mutáveis, porém aceitam apenas
# *     tipos imutáveis como valor interno

# * Criando um set
# * set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set() # vazio
# s1 = {'Luiz', 1, 2, 3} # com dados
# print(s1)

# * Sets são eficientes para remover valores duplicados
# *     de iteráveis.
# * - eles não tem indexes;
# * - eles não garantem ordem;
# * - eles são iteráveis (for, in, not in);
l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
print(l2)

# * Métodos úteis:
# * add, update, clear, discard

# * Operadores úteis:
# * união | união (union) - Une
# * intersecção & (intersection) - Itens presentes em ambos
# * diferença - Itens presentes apenas no set da esquerda
# * diferença simétrica ^ - Itens que não estão em ambos