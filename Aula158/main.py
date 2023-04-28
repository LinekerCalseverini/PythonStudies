"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas correntes tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Cliente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da Classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas tem agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstracção e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from conta_banco import ContaCorrente, ContaPoupanca
from cliente import Cliente
from banco import Banco


conta_corrente = ContaCorrente('0000', '0000000', 0.0, 200.0)
conta_poupanca = ContaPoupanca('0000', '1000000', 0.0)


conta_corrente.sacar(200.0)
print(conta_corrente)
print()
print(conta_poupanca.saldo)
conta_poupanca.depositar(100.0)
conta_poupanca.sacar(50.0)
print(conta_poupanca.saldo)

print()
print(conta_corrente)
print()
print(conta_poupanca)
print()

cliente_a = Cliente('Lineker', 27)
cliente_b = Cliente('Filipe', 28)
banco = Banco()

banco.adicionar_conta(cliente_a, conta_corrente)
banco.adicionar_conta(cliente_a, conta_poupanca)

banco.adicionar_conta(cliente_b, ContaCorrente('0000', '0000001', 0.0, 1500.0))
banco.adicionar_conta(cliente_b, ContaPoupanca('0000', '1000001', 0.0))

banco.listar_clientes()

banco.buscar_clientes('Lineker')
banco.buscar_agencia('0000')
print()
banco.buscar_conta('0000001')
