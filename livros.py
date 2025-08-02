#Básicamente faz com que um objeto nao seja criado diretamente da classe mãe e sim das Heranças
from abc import ABC, abstractclassmethod

class Imovel(ABC):
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        self._nome = nome #1 anderline protegido, dois anderline atributos privados.
        self.uf = uf
        self.valor = valor
        self.endereco = endereco
        self.area = area


#=================== Encapsulamento no python =======================

    @property  
    def nome(self): #get
        return self._nome

    @nome.setter #set -  Utiliza metodos como atributos
    def nome(self, nome):
        self._nome = nome
    
#=================== Encapsulamento no python =======================





#==================== Forma convencional, utilizado nas outras liguagens ===============================
#    def getNome(self):       #metodo para pegar o valor do nome
#       return self.nome

#    def setNome(self, nome):  #metodo para setar o nome
#        self.nome = nome
#==================== Forma convencional, utilizado nas outras liguagens ===============================



    def detalhar(self):            
        print(self.__dict__)
        
    
    def calcularImposto(self):
        return self.valor * 0.02
    
    @abstractclassmethod #metodo abstrato
    def aluguelsugerido(self): 
        ...

"""
imovel = Imovel('Solar do Cerrado', 'DF', 500000)
imovel.detalhar()
imovel.endereco = 'ABC'
imovel.area = '20000'
"""

class ImovelResidencial(Imovel):
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        super().__init__(nome, uf, valor, endereco = '', area = '')
        self.quartos = 0
        self.piscina = False
        
    def aluguelsugerido(self): 
        return self.valor * 0.01    
    
class ImovelComercial(Imovel):
    def aluguelsugerido(self): 
        return self.valor * 0.015    
    


class ImovelRural():
    def __init__(self, hectares = '', curral = '', produtiva = True):
        self.hectares = hectares
        self.curral = curral
        self.produtiva = produtiva
        
    def mesPlantacao(self, mes):
        match int(self, mes):
            case 1: print('Milho')
            case 2: print('Feijão')
            case 3: print('Soja')
            case other: print('Algodão')
                
class Fazeda(Imovel, ImovelRural):
    def aluguelsugerido(self): 
        return self.valor * 0.025    
    

"""
fazenda = Fazeda('teste 1 ', 'per', 304598)
fazenda.endereco = 'daskd'
fazenda.area = 'dsappko'
fazenda.detalhar()
"""

casa = ImovelResidencial('teste 1 ', 'per', 304598)
casa.nome = "Casa muito  Bonita"
"""
casa.endereco = 'daskd'
casa.area = 'dsappko'
"""
casa.detalhar()
#print(casa.getNome())