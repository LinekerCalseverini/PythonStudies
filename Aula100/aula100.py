# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# Dica: modulo copy e funções sorted ou list.sorted
import sys
sys.path.append('c:\\Users\\Link\\Documents\\Repositorios\\PythonStudies')
from copy import deepcopy
from modulos_extras import produtos

novos_produtos = [
    {**p, 'preco': round(p['preco']*1.1,2)}
    for p in deepcopy(produtos)
]

# Ordene os produtos por nome decrescente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    deepcopy(produtos),
    key=lambda produto: produto['nome'],
    reverse=True
)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(
    deepcopy(produtos),
    key=lambda produto: produto['preco']
)

print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')