from abc import ABC, abstractmethod, abstractclassmethod

class Transacao(ABC):
  
  @property
  @abstractmethod
  def valor(self):
    pass
  
  @abstractclassmethod
  def registrar(self, conta):
    pass