# -*- coding: utf-8 -*-
"""Adapter-Calibrador.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oXfQL5vFMyuusNXMscPnBmEameXPc-FI
"""

import random

class MedidorPressaoPSI:
  '''
  Interface/Implementação de um Medidor de Pressão
  que retorna a medida em Libras (PSI)
  '''

  def calculaPressao(self) -> float:
    '''
    Retorna o valor da pressão em Libras
    '''
    medicao = random.randint(0, 100)
    ##  ar contido no Pneu, entre 0 e 100, onde 0 é vazio,
     #  e 100 o maximo suportado pelo volume

    pressaoCompleta = 50
    ##  valor em PSI quando o sensor retorna 100%
    
    pressao = round((medicao / 100) * pressaoCompleta, 2)
    print(f"A pressão é {pressao} Libras")
    return pressao

class MedidorPressaoATM:
  '''
  Interface/Implementação de um Medidor de Pressão
  que retorna a medida em ATM
  '''
  
  def calculaPressao(self) -> float:
    '''
    Retorna o valor da pressão em ATM
    '''
    medicao = random.randint(0, 100)
    ##  ar contido no Pneu, entre 0 e 100, onde 0 é vazio,
     #  e 100 o maximo suportado pelo volume

    pressaoCompleta = 3.4
    ##  valor em PSI quando o sensor retorna 100%

    pressao = round((medicao / 100) * pressaoCompleta, 2)
    print(f"A pressão é {pressao} ATM")
    return pressao

class AdaptadorMedidorAtm(MedidorPressaoPSI):
  def __init__(self, medidor: MedidorPressaoATM):
    self._medidorATM = medidor

  def calculaPressao(self):
    pressaoATM = self._medidorATM.calculaPressao()
    pressaoConvertida = round(pressaoATM * 14.6959488036)

    print(f"{pressaoATM} ATM em Libras é: {pressaoConvertida}")
    return pressaoConvertida

class Calibrador:
  '''
  Dispositivo que envia/puxa ar para a mangueira
  de acordo com a pressão endicada pelo medidor,
  que deve fornecer a pressão em Libras (PSI)
  '''
  def __init__(self, medidor: MedidorPressaoPSI):
    self._medidor = medidor
  
  def __liberarAr(self, qtd):
    print(f"Liberando {qtd} Libras ...")

  def __adicionarAr(self, qtd):
    print(f"Adicionando {qtd} Libras ...")
  
  def calibrar(self, pressaoDesejada: int):
    pressaoAtual = self._medidor.calculaPressao()

    diferenca = pressaoDesejada - pressaoAtual
    
    if (diferenca > 0):
      self.__adicionarAr(diferenca)
      pressaoAtual += diferenca
    elif (diferenca < 0):
      self.__liberarAr(-1 * diferenca)
      pressaoAtual += diferenca
    
    print(f"\nSeu pneu está cheio ({pressaoAtual} Libras)")

if __name__ == "__main__":
  medidorAtm = MedidorPressaoATM()
  adaptador = AdaptadorMedidorAtm(medidorAtm)

  calibradorPneu = Calibrador(adaptador)
  calibradorPneu.calibrar(32)