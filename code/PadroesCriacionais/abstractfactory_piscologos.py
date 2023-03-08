"""FactoryMethod-AgenciaViagem.py

Exemplo de código de utilização do Design Pattern Abstract Factory
"""

## Rede de consultorios psicologicos: Infantil, e do Trabalho
## Os Psicologos realizam consulta,
 # e são classificados em traumas, e comportamento

from abc import ABC, abstractmethod

class PsicologoInfantil(ABC):
  '''
  Interface que define o comportamento do psicologo Infantil
  '''
  @abstractmethod
  def consultar(self):
    pass

class AnaliseTraumas(PsicologoInfantil):
  def consultar(self):
    return "Analizando possiveis traumas infantis ..."

class AnaliseComportamental(PsicologoInfantil):
  def consultar(self):
    return "Analizando o comportamento da criança ..."

class PsicologoTrabalhista(ABC):
  '''
  Interface que define o comportamento do psicologo Trabalhista
  '''
  @abstractmethod
  def consultar(self):
    pass

class AcompanhamentoTraumas(PsicologoTrabalhista):
  def consultar(self):
    return "Consultando funcionario sobre traumas pessoais ..."
  
class AcompanhamentoComportamental(PsicologoTrabalhista):
  def consultar(self):
    return "Analizando comportamentos indevidos de funcionarios ..."

# Fabrica abstrata
class ConsultorioPsicologico(ABC):
  '''
  Interface que padroniza a Fabrica (Consultorios)
  '''
  @abstractmethod
  def consultaTraumatologica(self) -> PsicologoInfantil:
    pass

  @abstractmethod
  def consultaComportamental(self) -> PsicologoTrabalhista:
    pass

## Fabrica Concreta
class ConsultorioInfantil(ConsultorioPsicologico):
  def consultaTraumatologica(self) -> PsicologoTrabalhista:
    return AnaliseTraumas()

  def consultaComportamental(self) -> PsicologoTrabalhista:
    return AnaliseComportamental()

## Fabrica Concreta
class ConsultorioTrabalhista(ConsultorioPsicologico):
  def consultaTraumatologica(self) -> PsicologoTrabalhista:
    return AcompanhamentoTraumas()

  def consultaComportamental(self) -> PsicologoTrabalhista:
    return AcompanhamentoComportamental()

def cliente(consultorio: ConsultorioPsicologico):
  ## Metodo que chama as fabricas
  consultaTrauma = consultorio.consultaTraumatologica()
  consultaComportamento = consultorio.consultaComportamental()

  print(f"{consultaTrauma.consultar()}")
  print(f"{consultaComportamento.consultar()}")

if __name__ == "__main__":
  print("Cliente sendo atendido pelo Consultorio Infantil")
  cliente(ConsultorioInfantil())

  print("\nCliente sendo atendido pelo Consultorio Trabalhista")
  cliente(ConsultorioTrabalhista())