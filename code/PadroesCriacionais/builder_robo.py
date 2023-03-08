"""FactoryMethod-AgenciaViagem.py

Exemplo de código de utilização do Design Pattern Builder
"""

from abc import ABC, abstractmethod

class Robo:
  '''
  Classe do Robô concreto que será construído pelo Builder
  '''
  def __init__(self):
    self.parts = [] # Array das partes que compoem o robô
  
  def adicionarParte(self, part):
    '''
    Método usado para adicionar uma nova parte do robô a cada passo
    '''
    self.parts.append(part)
  
  def mostrarPartes(self):
    print("Seu Robô possui:")
    for part in self.parts:
      print(f" - {part}")

class RoboBuilder(ABC):
  '''
  Interface que padroniza o comportamento genérico de um Construtor de Robôs
  '''
  @abstractmethod
  def _reset(self):
    '''
    Método que redefine o robô que será construido pelo Builder
    '''
    pass
  
  @abstractmethod
  def adicionarCabeca(self):
    pass
  
  @abstractmethod
  def adicionarCorpo(self):
    pass
  
  @abstractmethod
  def adicionarBracos(self):
    pass
  
  @abstractmethod
  def adicionarPernas(self):
    pass

  @abstractmethod
  def obterRobo(self) -> Robo:
    '''
    Método que retorna o robo construído com as partes adicionadas pelo Builder
    e reseta o robo de sua estrutura para que um outro possa ser construido
    '''
    pass

class BuilderBasicoRobo(RoboBuilder):
  '''
  Builder que define os passos para a construção de um Robô Básico
  '''
  def __init__(self):
    self._reset()

  def _reset(self):
    self._robo = Robo()

  def adicionarCabeca(self):
    self._robo.adicionarParte("Cabeça Comum")
      
  def adicionarCorpo(self):
    self._robo.adicionarParte("Corpo Básico")
      
  def adicionarBracos(self):
    self._robo.adicionarParte("Braços Básicos")
      
  def adicionarPernas(self):
    self._robo.adicionarParte("Pernas Básicas")
    
  def obterRobo(self) -> Robo:
    roboFinalizado = self._robo
    self._reset()
    return roboFinalizado

class BuilderAvancadoRobo(RoboBuilder):
  '''
  Builder que define os passos para a construção de um Robô Sofisticado
  '''
  def __init__(self):
    self._reset()

  def _reset(self):
    self._robo = Robo()

  def adicionarCabeca(self):
    self._robo.adicionarParte("Cabeça com auto-falantes")
      
  def adicionarCorpo(self):
    self._robo.adicionarParte("Corpo Reforçado")
      
  def adicionarBracos(self):
    self._robo.adicionarParte("Braços com pinça nas mãos")
      
  def adicionarPernas(self):
    self._robo.adicionarParte("Pernas com rodas nos pés")
    
  def obterRobo(self) -> Robo:
    roboFinalizado = self._robo
    self._reset()
    return roboFinalizado

class Director:
  def __init__(self, builder: RoboBuilder):
    self.builder = builder
      
  def buildRobo(self):
    self.builder.adicionarCabeca()
    self.builder.adicionarCorpo()
    self.builder.adicionarBracos()
    self.builder.adicionarPernas()
    return self.builder.obterRobo()

def cliente(builder: RoboBuilder) -> Robo:
  diretor = Director(builder)
  novoRobo = diretor.buildRobo()
  novoRobo.mostrarPartes()

# Exemplo de utilização
if __name__ == "__main__":
  print("Construindo um Robo Básico:")
  cliente(BuilderBasicoRobo())

  print("\nConstruindo um Robo Avançado:")
  cliente(BuilderAvancadoRobo())