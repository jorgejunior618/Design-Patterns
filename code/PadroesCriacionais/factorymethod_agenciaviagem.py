"""FactoryMethod-AgenciaViagem.py

Exemplo de código de utilização do Design Pattern Factory Method
"""

from abc import ABC, abstractmethod

class PassagemAbs(ABC):
  '''
  Interface que define a estrutura de uma passagem genérica
  '''
  def __init__(self, partida, destino, ida, distancia):
    self.partida = partida
    self.destino = destino
    self.ida = ida
    self.tempoViagem = 0

## Implementação da Interface Passagem para os tipos de passagem Aereas

class PassagemAereaEconomica(PassagemAbs):
  def __init__(self, partida, destino, ida, distancia):
    self.partida = partida
    self.destino = destino
    self.ida = ida
    self.tempoViagem = distancia / 800
    # Considerando distância em Km Velocidade media do aviao de 800Km/h
  
  def __str__(self):
    return ("Viagem de Avião Econômica marcada \n" +
      f"  - Saindo {self.ida} de {self.partida} para {self.destino}\n"+
      f"  - Tempo estimado de viagem {self.tempoViagem} Horas")
    
class PassagemAereaClasse(PassagemAbs):
  def __init__(self, partida, destino, ida, distancia):
    self.partida = partida
    self.destino = destino
    self.ida = ida
    self.tempoViagem = distancia / 800
    # Considerando distância em Km Velocidade media do aviao de 800Km/h
  
  def __str__(self):
    return ("Viagem de Avião 1ª Classe marcada \n" +
      f"  - Saindo {self.ida} de {self.partida} para {self.destino}\n"+
      f"  - Tempo estimado de viagem {self.tempoViagem} Horas")

## Implementação da Interface Passagem para os tipos de passagem de Ônibus

class PassagemOnibusComParadas(PassagemAbs):
  def __init__(self, partida, destino, ida, distancia):
    self.partida = partida
    self.destino = destino
    self.ida = ida
    self.tempoViagem = distancia / 60
    # Considerando distância em Km Velocidade media do onibus de 60Km/h
  
  def __str__(self):
    return ("Viagem de Ônibus marcada \n" +
      f"  - Saindo {self.ida} de {self.partida} para {self.destino}\n"+
      f"  - Tempo estimado de viagem {self.tempoViagem} Horas")

class PassagemOnibusExpresso(PassagemAbs):
  def __init__(self, partida, destino, ida, distancia):
    self.partida = partida
    self.destino = destino
    self.ida = ida
    self.tempoViagem = distancia / 60
    # Considerando distância em Km Velocidade media do onibus de 60Km/h
  
  def __str__(self):
    return ("Viagem de Ônibus Expressa marcada \n" +
      f"  - Saindo {self.ida} de {self.partida} para {self.destino}\n"+
      f"  - Tempo estimado de viagem {self.tempoViagem} Horas")

class FabricaPassagem(ABC):
  '''
  Interface das classes que implementarão as fabricas para criação das passagens
  '''
  def __init__(self):
    pass
  
  @abstractmethod
  def criarPassagem(self, partida, destino, distancia, ida, economica):
    pass

class ViagemOnibus(FabricaPassagem):
  '''
  Fábrica que instancia as passagens de Ônibus
  '''
  def __init__(self):
    pass
  
  def criarPassagem(self, partida, destino, distancia, ida, economica):
    '''
    Método que contém as regras de que tipo de passagens de Ônibus será instanciada
    '''
    if (economica):
        return PassagemOnibusComParadas(partida, destino, ida, distancia)
    else:
        return PassagemOnibusExpresso(partida, destino, ida, distancia)

class ViagemAviao(FabricaPassagem):
  '''
  Fábrica que instancia as passagens de Avião
  '''
  def __init__(self):
    pass
  
  def criarPassagem(self, partida, destino, distancia, ida, economica):
    '''
    Método que contém as regras de que tipo de passagens de Avião será instanciada
    '''
    if (economica):
        return PassagemAereaEconomica(partida, destino, ida, distancia)
    else:
        return PassagemAereaClasse(partida, destino, ida, distancia)

class FabricaViagem(ABC):
  '''
  Interface da classe que implementará a fábrica para criação das passagens
  '''
  def __init__(self):
    pass
  
  @abstractmethod
  def marcarViagem(self, partida, destino, ida, distancia, tipo, economica):
    pass

class AgenciaViagem(FabricaViagem):
  '''
  Fábrica que instancia as passagens
  '''
  def __init__(self):
    pass
  
  def marcarViagem(self, partida, destino, ida, distancia, tipo, economica):
    '''
    Método que define se será instanciada a viagem de Avião ou Ônibus
    '''
    tiposViagem = {
        'Aviao': ViagemAviao,
        'Onibus': ViagemOnibus,
    }

    return tiposViagem[tipo].criarPassagem(partida, destino, ida, distancia, tipo, economica)

## Código do cliente

agencia = AgenciaViagem()

viagemIda = agencia.marcarViagem('Fortaleza', 'Sao Paulo', '10/02/2023', 3000, 'Aviao', True)
print(viagemIda)

viagemVolta = agencia.marcarViagem(
    'São Paulo',
    'Fortaleza',
    '17/02/2023',
    3000,
    'Onibus',
    False,
  )
print(viagemVolta)