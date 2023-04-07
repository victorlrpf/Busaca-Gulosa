class Vertice:

  def __init__(self, rotulo, distancia_objetivo):
    self.rotulo = rotulo
    self.visitado = False
    self.distancia_objetivo = distancia_objetivo
    self.adjacentes = []

  def adiciona_adjacente(self, adjacente):
    self.adjacentes.append(adjacente)

  def mostra_adjacentes(self):
    for i in self.adjacentes:
      print(i.vertice.rotulo, i.custo)

class Adjacente:
  def __init__(self, vertice, custo):
    self.vertice = vertice
    self.custo = custo

class Grafo:
  portoUniao = Vertice("Porto União", 203)
  pauloFrontin = Vertice("Paulo Frontin", 172)
  canoinhas = Vertice("Canoinhas", 141)
  irati = Vertice("Irati", 139)
  palmeira = Vertice("Palmeira", 59)
  campoLargo = Vertice("Campo Largo", 27)
  curitiba = Vertice("Curitiba", 0)
  balsaNova = Vertice("Balsa Nova", 41)
  araucaria = Vertice("Araucária", 23)
  saoJose = Vertice("São José dos Pinhais", 13)
  contenda = Vertice("Contenda", 39)
  mafra = Vertice("Mafra", 94)
  tijucas = Vertice("Tijucas do Sul", 56)
  lapa = Vertice("Lapa", 74)
  saoMateus = Vertice("São Mateus do Sul", 123)
  tresBarras = Vertice("Três Barras", 131)


  portoUniao.adiciona_adjacente(Adjacente(pauloFrontin, 46))  
  portoUniao.adiciona_adjacente(Adjacente(canoinhas, 78))
  portoUniao.adiciona_adjacente(Adjacente(saoMateus, 87))
       
  pauloFrontin.adiciona_adjacente(Adjacente(portoUniao, 46))
  pauloFrontin.adiciona_adjacente(Adjacente(irati, 75))
    
  canoinhas.adiciona_adjacente(Adjacente(portoUniao, 78))
  canoinhas.adiciona_adjacente(Adjacente(tresBarras, 12))
  canoinhas.adiciona_adjacente(Adjacente(mafra, 66))
    
  irati.adiciona_adjacente(Adjacente(pauloFrontin, 75))
  irati.adiciona_adjacente(Adjacente(palmeira, 75))
  irati.adiciona_adjacente(Adjacente(saoMateus, 57))
    
  palmeira.adiciona_adjacente(Adjacente(irati, 75))
  palmeira.adiciona_adjacente(Adjacente(saoMateus, 77))
  palmeira.adiciona_adjacente(Adjacente(campoLargo, 55))
    
  campoLargo.adiciona_adjacente(Adjacente(palmeira, 55))
  campoLargo.adiciona_adjacente(Adjacente(balsaNova, 22))
  campoLargo.adiciona_adjacente(Adjacente(curitiba, 29))
    
  curitiba.adiciona_adjacente(Adjacente(campoLargo, 29))
  curitiba.adiciona_adjacente(Adjacente(balsaNova, 51))
  curitiba.adiciona_adjacente(Adjacente(araucaria, 37))
  curitiba.adiciona_adjacente(Adjacente(saoJose, 15))
    
  balsaNova.adiciona_adjacente(Adjacente(curitiba, 51))
  balsaNova.adiciona_adjacente(Adjacente(campoLargo, 22))
  balsaNova.adiciona_adjacente(Adjacente(contenda, 19))
    
  araucaria.adiciona_adjacente(Adjacente(curitiba, 37))
  araucaria.adiciona_adjacente(Adjacente(contenda, 18))
    
  saoJose.adiciona_adjacente(Adjacente(curitiba, 15))
  saoJose.adiciona_adjacente(Adjacente(tijucas, 49))
    
  contenda.adiciona_adjacente(Adjacente(balsaNova, 19))
  contenda.adiciona_adjacente(Adjacente(araucaria, 18))
  contenda.adiciona_adjacente(Adjacente(lapa, 26))

  mafra.adiciona_adjacente(Adjacente(tijucas, 99))
  mafra.adiciona_adjacente(Adjacente(lapa, 57))
  mafra.adiciona_adjacente(Adjacente(canoinhas, 66))
    
  tijucas.adiciona_adjacente(Adjacente(mafra, 99))
  tijucas.adiciona_adjacente(Adjacente(saoJose, 49))

  lapa.adiciona_adjacente(Adjacente(contenda, 26))
  lapa.adiciona_adjacente(Adjacente(saoMateus, 60))
  lapa.adiciona_adjacente(Adjacente(mafra, 57))
    
  saoMateus.adiciona_adjacente(Adjacente(palmeira, 77))
  saoMateus.adiciona_adjacente(Adjacente(irati, 57))
  saoMateus.adiciona_adjacente(Adjacente(lapa, 60))
  saoMateus.adiciona_adjacente(Adjacente(tresBarras, 43))
  saoMateus.adiciona_adjacente(Adjacente(portoUniao, 87))
    
  tresBarras.adiciona_adjacente(Adjacente(saoMateus, 43))
  tresBarras.adiciona_adjacente(Adjacente(canoinhas, 12))

grafo = Grafo()

import numpy as np
class VetorOrdenado:
  
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=object)

  def insere(self, vertice):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return
    posicao = 0
    for i in range(self.ultima_posicao + 1):
      posicao = i
      if self.valores[i].distancia_objetivo > vertice.distancia_objetivo:
        break
      if i == self.ultima_posicao:
        posicao = i + 1
    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      x -= 1
    self.valores[posicao] = vertice
    self.ultima_posicao += 1

  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i].rotulo, ' - ', self.valores[i].distancia_objetivo)

vetor = VetorOrdenado(5)
vetor.insere(grafo.palmeira)
vetor.insere(grafo.lapa)
vetor.insere(grafo.campoLargo)
vetor.insere(grafo.curitiba)

print("Vetor Ordenado")
vetor.imprime()

vetor.valores[0], vetor.valores[0].rotulo


class Gulosa:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False

  def buscar(self, atual):
    print('------------------------------')
    print('Atual: {}'.format(atual.rotulo))
    atual.visitado = True

    if atual == self.objetivo:
      self.encontrado = True
    else:
      vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
      for adjacente in atual.adjacentes:
        if adjacente.vertice.visitado == False:
          adjacente.vertice.visitado == True
          vetor_ordenado.insere(adjacente.vertice)
      vetor_ordenado.imprime()

      if vetor_ordenado.valores[0] != None:
        self.buscar(vetor_ordenado.valores[0])

busca_gulosa = Gulosa(grafo.curitiba)
busca_gulosa.buscar(grafo.portoUniao)