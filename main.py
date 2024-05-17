class ContaBancaria:
  def __init__(self,nome):

    self.nome = nome
    
    self.MAX_TRANSACOES_DIA = 3
    self.MAX_VALOR_SAQUE = 500

    self.saldo = 0
    self.transacoes = Pilha()

    self.qtde_saques = 0

  
  def deposito(self,valor):
    if valor > 0:
      self.saldo += valor
      self.transacoes.empilhar(f'Deposito de {self.nome} \nValor: {formata_saque(valor)}')
      return self.transacoes.topo()
    return 'Valor inválido'
      

  
  def saque(self,valor):
    if qtde_saques >= MAX_TRANSACOES_DIA:
      return 'Limite de saques diário atingido'

    if valor > MAX_VALOR_SAQUE:
      return f'Limite de valor do saque: {self.MAX_VALOR_SAQUE}'

    if valor > self.saldo:
      return 'Saldo insuficiente'

    self.saldo -= valor
    self.transacoes.empilhar(f'Saque de {self.nome} \nValor: {formata_saque(valor)}')
    return self.transacoes.topo()
    
  def formata_saque(valor):
    return f'R$ {valor:.2f}'

  def extrato(self):
    self.transacoes.printa_pilha()
  



class Pilha:
  def __init__(self):
    self.dados = []

  def empilhar(self, elemento):
    self.dados.append(elemento)

  def desempilhar(self):
    if self.esta_vazia():
      return None
    return self.dados.pop()

  def esta_vazia(self):
    return len(self.dados) == 0

  def tamanho(self):
    return len(self.dados)

  def printa_pilha(self):
    for item in self.dados[::-1]:
      print(item)

  def topo(self):
    return self.dados[-1]

