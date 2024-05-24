from Conta import Conta
from interface_transacao import Transacao

class Cliente:
  
  def __init__(self, endereco):
    self._endereco = endereco
    self._contas = []
    
  @property
  def endereco(self):
    return self._endereco
  
  @endereco.getter
  def endereco(self, novo_endereco):
    self._endereco = novo_endereco
    
  def realizar_trasacao(self, conta, transacao):
    transacao.registrar(conta)
    
  def adicionar_conta(self, conta):
    self._contas.append(conta)
  