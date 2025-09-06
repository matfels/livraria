from datetime import datetime
#classe Livros=======================================================================
class Livros:
    def __init__(self, titulo, autor, npagina, status = 'Disponível'):
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
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Numero de páginas: {self.npagina}")
        print(f"Status: {self.status}")
#classe Livros=======================================================================

#classe Emprestimo==================================================================    
class Emprestimos:
    def __init__(self, livro, data_emprestimo):
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = None
        
    def registrar_devolucao(self):
        self.data_devolucao = datetime.now()
        
    def __str__(self):
        status_devolucao = f"Devolvido em: {self.data_devolucao.strftime('%d/%m/%Y')}" if self.data_devolucao else 'Não devolvido'
        return f"Livro: '{self.livro.titulo}' (Empréstimo: {self.data_emprestimo.strftime('%d/%m/%Y %H:%M')}, {status_devolucao})"
#classe Emprestimo==================================================================
        
#Classe usuário=====================================================================
class Usuarios:
    def __init__(self, nome, id, historico = None):
        self.nome = nome
        self.id = id
        self.historico = historico if historico is not None else []

    def emprestimo(self,livro):
        if livro.status == "Disponivel":
            livro.statuss("Emprestado")
            data_emprestimo = datetime.now()
            novo_emprestimo = Emprestimos(livro, data_emprestimo)
            self.historico.append(novo_emprestimo)
            print(f"'{livro.titulo} emprestado para {self.nome}")
        else:
            print(f"O livro '{livro.titulo}' não está disponível para emprestimo.")
            
    def devolverLivro(self,livro): #Melhoar, da para só adicionar a data de devolução do livro
        encontrado = False
        for emprestimo_obj in self.historico:
            if emprestimo_obj.livro == livro and emprestimo_obj.data_devolucao is None:
                emprestimo_obj.registrar_devolucao()
                livro.statuss("Disponivel")
                print(f"'{livro.titulo}' devolvido por {self.nome}")
                encontrado = True
                break
        if not encontrado:
            print(f"O livro '{livro.titulo} não foi encontrado como emprestado para {self.nome} ou já foi devolvido.")
                     
    def exibir(self):
        cont = 0
        print(f"Histórico de empréstimo de {self.nome} (ID: {self.id}): ")
        if not self.historico:
            print("Nenhum livro no historico.")
        else:
            for i, emprestimo_obj in enumerate(self.historico):
                print(f"{i+1} - {emprestimo_obj}")
#Classe usuário=====================================================================
        
    
            
            



   
# OBJETOS LIVROS
livro1 = Livros('1 - livro', 'Chico', 2500, 'Disponivel') 
livro2 = Livros('2 - livro', 'asd', 250, 'Disponivel') 
livro3 = Livros('3 - livro', 'gdf', 2400, 'Disponivel') 
livro4 = Livros('4 - livro', 'gfd', 2030, 'Disponivel') 


# OBJETO USUARIO
usuario1 = Usuarios('Matheus', 123)                              

# Emprestimo livro
usuario1.emprestimo(livro1)
usuario1.emprestimo(livro2)
#usuario1.emprestimo(livro3)
usuario1.emprestimo(livro4)


# Devolução livro
usuario1.devolverLivro(livro3)

# Exibir histórico
usuario1.exibir()
