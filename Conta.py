from Historico import Historico
from Cliente import Cliente

class Conta:
  
  def __init__(self, numero, cliente):
    self._saldo = 0 
    self._numero = numero
    self._agencia = "0001"
    self._cliente = cliente
    self._historico = Historico()
  
  @classmethod
  def novo_conta(cls, cliente, numero):
    return cls(numero, cliente)
  
  @property  
  def saldo(self):
    return self._saldo
  
  @property
  def numero(self):
    return self._numero
  
  @property
  def agencia(self):
    return self._agencia
  
  @property
  def cliente(self):
    return self._cliente
  
  @property
  def historico(self):
    return self._historico
  
  @saldo.getter
  def saldo(self, novo_saldo):
    self._saldo = novo_saldo
    
  def sacar(self, valor):
    if valor > self.saldo:
      print("\nOpereção falhou! Valor acima do saldo!")
      
    elif valor > 0:
      self.saldo -= valor
      print(f"\nSaque realizado com sucesso!\nSeu saldo agora é R${self.saldo}")
      return True
    
    else:
      print("\nOperação falhou! Valor informado é invalido!")
    
    return False
    
  def depositar(self, valor):
    if valor > 0:
      self.saldo += valor
      print(f'\nValor depositado com sucesso!\nSeu saldo agora é R${self.saldo}')

    else:
      print("\nOperação FALHOU!\nValor informado invalido! ")
      return False
    
    return True    
  