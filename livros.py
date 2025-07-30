from datetime import datetime
#classe livro, definido os atributos e metodos permitem ver disponibilidade, status e exibir informações do livro.
class Livros:
    def __init__(self, titulo, autor, npagina, status):
        self.titulo = titulo
        self.autor = autor
        self.npagina = npagina
        self.status = status


    def verDisp(self):
        match self.status:
            case 'Disponivel':
                print('Livro esta Disponivel')
            case 'Indisponivel':
                print('Livro esta Indisponivel')
            case other:
                print('Erro no status')
                

    def statuss(self, status1):
        self.status = status1

    def exibir(self):
        print(self.__dict__)
    
'''
livro1 = Livros('Chapeu vermelho', 'Chico', 200, 'Indisponivel')
livro1.exibir()
livro1.verDisp()
livro1.statuss('Disponivel')
'''

class data:
    def __init__(self, pegar1 = '', devolver1 = ''):
        self.pegar1 = pegar1
        self.devolver1 = devolver1
        
    def pegar():
        ...
    def devolver():
        ... 



class Livro:
    def __init__(self, livro, dataemprestimo = '', datadevolucao = ''):
        self.livro = livro
        self.dataemprestimo = dataemprestimo
        self.datadevolucao = datadevolucao


    def emprestimo(self,):
        emprestimo = datetime.now()
        self.dataemprestimo = emprestimo
        

         
    def devolucao():
        ...

    
teste = Livro("Livro")
teste.emprestimo()
print(teste.__dict__)



#Classe usuário, definido os atributos e os metodos de pegar, devolver livro e exibir histórico de livro.
class Usuarios:
    def __init__(self, nome, id, historico = '' ):
        self.nome = nome
        self.id = id
        self.historico = historico()
        self.data = data()
    def emprestarLivro(self,hisLivro):
        self.historico.append(hisLivro)
        
    def devolverLivro(self,hisLivro):
        self.historico.remove(hisLivro)
        
    def exibir(self):
        cont = 0
        print("Historico:")
        for item in self.historico:
            cont += 1
            print(f'{cont} - {item}')

    def emprestimo(self):
        ...

"""
usuario1 = Usuarios('Matheus', 123,  )
usuario1.emprestarLivro('Chapeu vermelho')
usuario1.emprestarLivro('Ocho')
usuario1.emprestarLivro('não identificado')
"""

#usuario1.devolverLivro('Chapeu vermelho')
#usuario1.exibir()


